import re

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CampaignForm, TagsForm, DonationForm
from .models import Campaign, Donation
from ..tags.models import Tag
from ..organizations.models import Organization


@login_required
def create_campaign(request, organization_name: str):
    campaign_form = CampaignForm()
    tag_form = TagsForm()

    organization = Organization.objects.get(
        name=organization_name
    )
    count_same_tag = 0
    if request.method == 'POST':
        campaign_form = CampaignForm(request.POST, request.FILES)
        tag_form = TagsForm(request.POST)
        if all([campaign_form.is_valid(), tag_form.is_valid()]):
            tag_list = [tag_name for tag_name in re.split('[, ]',
                                                          tag_form.cleaned_data['enter_tags_you_would_like_to_include'])
                        if tag_name != '']
            for tag_name in tag_list:
                if Tag.objects.filter(name=tag_name).exists():
                    count_same_tag += 1
                    messages.success(request, 'Tag name %s exists' % tag_name)
                    tag_list.remove(tag_name)
            if count_same_tag != 0:
                result = ','.join(word for word in tag_list)
                tag_form = TagsForm(initial={'enter_tags_you_would_like_to_include': result})
                context = {
                    'form': campaign_form, 'form1': tag_form
                }

                # this seems incorrectly placed. commenting it out.
                # Used for re-rendering create campaigns page. 
                return render(request, 'campaigns/create_campaign.html', context)
            campaign_creator = campaign_form.cleaned_data['creator']
            campaign_title = campaign_form.cleaned_data['title']
            campaign_description = campaign_form.cleaned_data['description']
            campaign_target_money = campaign_form.cleaned_data['target_money']
            campaign_days_left = campaign_form.cleaned_data['days_left']
            campaign_image = campaign_form.cleaned_data['image']
            new_campaign = Campaign(
                creator=campaign_creator,
                organization=organization,
                title=campaign_title,
                description=campaign_description,
                target_money=campaign_target_money,
                days_left=campaign_days_left,
                image=campaign_image)
            new_campaign.save()
            for enter_tag_name in tag_list:
                tag_created = Tag(name=enter_tag_name)
                tag_created.save()
                new_campaign.tag.add(tag_created)
                tag_created.campaigns.add(new_campaign)
            if request.POST.get('tag') != None:
                for exist_tag in tag_form.cleaned_data['tag']:
                    new_campaign.tag.add(exist_tag)
                    exist_tag.campaigns.add(new_campaign)
            messages.success(request, 'Campaign Created!')
            ##Uncomment campaign_form.save()
            ##form.save()
            return redirect('startsmart-home')
    context = {
        'form': campaign_form, 'form1': tag_form
    }

    return render(request, 'campaigns/create_campaign.html', context)


@login_required
def update_campaign(request, pk):
    campaign = Campaign.objects.get(id=pk)
    form = CampaignForm(instance=campaign)

    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            messages.success(request, 'Successfully Updated Campaign!')
            form.save()
        return redirect('startsmart-home')

    context = {
        'form': form,
    }

    return render(request, 'campaigns/update_campaign.html', context)


@login_required
def delete_campaign(request, pk):
    campaign = Campaign.objects.get(id=pk)

    if request.method == 'POST':
        campaign.delete()
        messages.success(request, 'Successfully Removed Campaign!')
        return redirect('startsmart-home')

    context = {
        'campaign': campaign
    }
    return render(request, 'campaigns/delete_campaign.html', context)


def search_campaign(request):
    query_word = request.GET.get('search_query')
    query_result = [res_word for res_word in re.split('[, ]', query_word) if res_word != '']
    temp = Campaign.objects.none()
    number_of_campaigns = 0
    for word in query_result:
        res = Campaign.objects.filter(Q(tags__name__icontains=word) | Q(title__icontains=word))
        res1 = Campaign.objects.filter(title__in=list(res.values_list('title', flat=True).distinct()))
        if len(res1) == 0: messages.success(request, '%s does not exist' % word)
        temp |= res1
    if len(temp) == 0:
        campaign = Campaign.objects.all()
    else:
        campaign = temp
    number_of_campaigns = len(temp)
    tag = Tag.objects.all()
    campaign_list = campaign.order_by('title')
    pageinator = Paginator(campaign_list, 30)
    num_page = request.GET.get('page')
    page_res = pageinator.get_page(num_page)
    context = {
        'campaigns': campaign,
        'tags': tag,
        'number_of_campaigns': number_of_campaigns,
        'page_res': page_res
    }
    return render(request, 'users/home_page.html', context)


# login not required for this
def view_campaign(request, username: str, campaign_title: str):
    campaign = Campaign.objects.get(creator__username=username, title=campaign_title)
    donor = Donation.objects.filter(donor=request.user.id, campaign=campaign)
    progress = campaign.current_money / campaign.target_money

    context = {
        'campaign': campaign,
        'donor': donor,
        'progress': progress,
        'bar_width': int(progress * 100),
    }
    # git
    return render(request, 'campaigns/view_campaign.html', context)


@login_required
def make_donation(request, pk):
    campaign = Campaign.objects.get(id=pk)
    form = DonationForm()

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation_campaign = form.cleaned_data['campaign']
            donation_amount = form.cleaned_data['amount']
            donation_donor = form.cleaned_data['donor']

            donation = Donation(
                campaign=donation_campaign,
                amount=donation_amount,
                donor=donation_donor
            )

            donation.save()

            messages.success(request, 'Successfully Donated!')
            return redirect(reverse('view-campaign', args=(campaign.creator.username, campaign.title)))

    context = {
        'form': form,
        'campaign': campaign,
    }

    return render(request, 'campaigns/make_donation.html', context)
