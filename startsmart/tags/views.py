from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import TagsForm
from .models import Tags, Campaign

@login_required
def create_tags(request):
    form = TagsForm()
    if request.method == 'POST':
        form = TagsForm(request.POST)
        if form.is_valid():
            # print('Name: %s' % form.cleaned_data['name'])
            # print('Name: %s' % form.cleaned_data['campaign'])
            # if Tags.objects.filter(name=form.cleaned_data['name']).exists():
            #     print('Exists')
            # else:
            #     print('Does not exist')
            tag = Tags(name=form.cleaned_data['name'])
            tag.save()
            for campaign_num in form.cleaned_data['campaign']: tag.campaign.add(campaign_num)
            messages.success(request, 'Tag Created!')
            form = TagsForm()



    context = {'form': form}
    return render(request, 'tags/create_tags.html', context)

def filter_campaigns_from_tags(request, tagname:str):
    campaigns = Tags.objects.get(name=tagname).campaign.all()
    tags = Tags.objects.all()
    context = {'campaign': campaigns, 'tags': tags}
    return render(request, 'tags/filter_campaigns_from_tags.html', context)

# Create your views here.
