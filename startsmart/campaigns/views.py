from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CampaignForm, TagsForm1
from .models import Campaign
from ..tags.models import Tags

import re


@login_required
def create_campaign(request):
    form = CampaignForm()
    form1 = TagsForm1()
    count_same_tag = 0
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        form1 = TagsForm1(request.POST)
        if all([form.is_valid(), form1.is_valid()]):
            tag_list = [tag_name for tag_name in re.split('[, ]',
                        form1.cleaned_data['enter_tags_you_would_like_to_include'])
                        if tag_name != '']
            for tag_name in tag_list:
                if Tags.objects.filter(name=tag_name).exists():
                    count_same_tag += 1
                    messages.success(request, 'Tag name %s exists' % tag_name)
                    tag_list.remove(tag_name)
            if count_same_tag != 0:
                result = ','.join(word for word in tag_list)
                form1 = TagsForm1(initial={'enter_tags_you_would_like_to_include': result})
                context = {
                    'form': form, 'form1': form1
                }
                return render(request, 'campaigns/create_campaign.html', context)
            c = form.cleaned_data['creator']
            t = form.cleaned_data['title']
            d = form.cleaned_data['description']
            t_money = form.cleaned_data['target_money']
            d_left = form.cleaned_data['days_left']
            images = form.cleaned_data['image']
            CampaignCreated = Campaign(
                creator = c,
                title = t,
                description = d,
                target_money = t_money,
                days_left = d_left,
                image = images)
            CampaignCreated.save()
            for enter_tag_name in tag_list:
                tag_created = Tags(name=enter_tag_name)
                tag_created.save()
                CampaignCreated.tag.add(tag_created)
                tag_created.campaigns.add(CampaignCreated)
            if request.POST.get('tag') != None:
                for exist_tag in form1.cleaned_data['tag']:
                    CampaignCreated.tag.add(exist_tag)
                    exist_tag.campaigns.add(CampaignCreated)
            messages.success(request, 'Campaign Created!')
            ##Uncomment form.save()
            ##form.save()
            return redirect('startsmart-home')
    context = {
        'form': form, 'form1' : form1
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
