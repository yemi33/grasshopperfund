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
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            c = form.cleaned_data['creator']
            t = form.cleaned_data['title']
            d = form.cleaned_data['description']
            t_money = form.cleaned_data['target_money']
            c_money = form.cleaned_data['current_money']
            d_left = form.cleaned_data['days_left']
            backers = form.cleaned_data['num_of_backers']
            images = form.cleaned_data['image']
            CampaignCreated = Campaign(creator = c, title = t, description = d, target_money = t_money,
                                       current_money = c_money, days_left = d_left, num_of_backers = backers,
                                       image = images)
            CampaignCreated.save()
            messages.success(request, 'Campaign Created!')
            ##Uncomment form.save()
            ##form.save()
            return redirect('startsmart-home')

    context = {
        'form': form
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
