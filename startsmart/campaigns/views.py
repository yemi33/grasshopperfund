from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CampaignForm
from .models import Campaign


@login_required
def create_campaign(request):
    form = CampaignForm()

    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Campaign Created!')
            form.save()
            return redirect('startsmart-home')

    context = {
        'form': form
    }

    return render(request, 'users/create_campaign.html', context)

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

    return render(request, 'users/update_campaign.html', context)

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
    return render(request, 'users/delete_campaign.html', context)

@login_required
def view_campaign(request, username:str, campaign_title:str):
    campaign = Campaign.objects.get(creator__username=username, title=campaign_title)

    context = {
        'campaign': campaign
    }
    return render(request, 'users/view_campaign.html', context)
