import re

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CampaignForm, TagsForm
from .models import Campaign
from ..tags.models import Tags
from ..organizations.models import Organization




@login_required
def create_campaign(request, organization_name: str):
    campaign_form = CampaignForm()
    tag_form = TagsForm()

    organization = Organization.objects.get(
        name = organization_name
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
                if Tags.objects.filter(name=tag_name).exists():
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
                # return render(request, 'campaigns/create_campaign.html', context)
            campaign_creator = campaign_form.cleaned_data['creator']
            campaign_title = campaign_form.cleaned_data['title']
            campaign_description = campaign_form.cleaned_data['description']
            campaign_target_money = campaign_form.cleaned_data['target_money']
            campaign_days_left = campaign_form.cleaned_data['days_left']
            campaign_image = campaign_form.cleaned_data['image']
            new_campaign = Campaign(
                creator = campaign_creator,
                organization = organization,
                title = campaign_title,
                description = campaign_description,
                target_money = campaign_target_money,
                days_left = campaign_days_left,
                image = campaign_image)
            new_campaign.save()
            for enter_tag_name in tag_list:
                tag_created = Tags(name=enter_tag_name)
                tag_created.save()
                new_campaign.tag.add(tag_created)
                tag_created.campaigns.add(new_campaign)
            if request.POST.get('tag') != None:
                for exist_tag in campaign_form.cleaned_data['tag']:
                    new_campaign.tag.add(exist_tag)
                    exist_tag.campaigns.add(new_campaign)
            messages.success(request, 'Campaign Created!')
            ##Uncomment campaign_form.save()
            ##form.save()
            return redirect('startsmart-home')
    context = {
        'form': campaign_form, 'form1' : tag_form
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

# login not required for this
def view_campaign(request, username:str, campaign_title:str):
    campaign = Campaign.objects.get(creator__username=username, title=campaign_title)

    context = {
        'campaign': campaign
    }
    return render(request, 'campaigns/view_campaign.html', context)
