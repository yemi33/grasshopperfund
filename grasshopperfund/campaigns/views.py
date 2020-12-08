import re

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.views import View

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
            if request.POST.get('tag') != None:
                for exist_tag in tag_form.cleaned_data['tag']:
                    new_campaign.tags.add(exist_tag)
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
    x = 0
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
    pageinator = Paginator(campaign_list, 8 // 2)
    num_page = request.GET.get('page')
    if num_page == None:
        x = 1
    else:
        page_res = pageinator.get_page(num_page)
        x = page_res.number
    page_res = pageinator.get_page(num_page)
    campaign = campaign[(x - 1) * 4: x * 4]
    progress_dict = {campaign_x.title: int((campaign_x.current_money / campaign_x.target_money) * 100) for campaign_x in
                     campaign}
    context = {
        'campaigns': campaign,
        'tags': tag,
        'number_of_campaigns': number_of_campaigns,
        'page_res': page_res,
        'query_word': query_word,
        'progress_dict': progress_dict,
    }
    return render(request, 'campaigns/search_campaign.html', context)


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




def browse_campaigns(request):
    '''
    Browse campaigns based on selected tags
    These tags are queried via OR statements.
    '''
    # check for selected tags from the query parameter
    # should be a list of tag names
    queried_tags = request.GET.getlist('tag', [])

    # all existing tags
    all_tags = Tag.objects.all()

    # selected tags based on what was queried
    selected_tags = all_tags

    print(queried_tags)

    # check to filter by tag
    if len(queried_tags) > 0:

        # create quieries
        # filter is case insensitive
        queries = [Q(name__icontains=tag_name) for tag_name in queried_tags]

        # init the final query
        final_query = queries.pop()

        for query in queries:

            # join queries via OR statement
            final_query |= query

        # execute the final query
        selected_tags = all_tags.filter(final_query)
    # campaigns are accessible from tags
    context = {
        'all_tags': all_tags,
        'selected_tags': selected_tags,
    }

    return render(request, 'campaigns/browse_campaigns.html', context)

