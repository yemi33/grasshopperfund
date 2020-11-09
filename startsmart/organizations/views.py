from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import OrganizationForm
from .models import Organization


@login_required
def create_organization(request):
    form = OrganizationForm()

    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES)

        if form.is_valid():
            owner = form.cleaned_data["owner"]
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]

            new_organization = Organization(
                owner = owner,
                name = name,
                description = description,
                image = image,
            )

            new_organization.save()
            messages.success(request, "Organization Created")

            return redirect("view-organization", organization_name = name)

    context = {
        "form": form,
    }

    return render(
        request,
        "organizations/create_organization.html",
        context,
    )


def view_organization(request, organization_name:str):
    try:
        organization = Organization.objects.get(name=organization_name)
    except Organization.DoesNotExist:
        # 404 if organization doesn't exist
        return(HttpResponse(status=404))

    context = {
        'organization': organization
    }
    return render(request, 'organizations/view_organization.html', context)

@login_required
def update_organization(request, organization_name: str):
    try:
        organization = Organization.objects.get(name=organization_name)
    except Organization.DoesNotExist:
        # 404 if organization doesn't exist
        return(HttpResponse(status=404))

    form = OrganizationForm(instance=organization)

    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES, instance=organization)
        if form.is_valid():
            messages.success(request, 'Successfully Updated organization!')
            form.save()
        return redirect('startsmart-home')

    context = {
        'form': form,
    }

    return render(request, 'organizations/update_organization.html', context)

@login_required
def delete_organization(request, organization_name: str):
    try:
        organization = Organization.objects.get(name=organization_name)
    except Organization.DoesNotExist:
        # 404 if organization doesn't exist
        return(HttpResponse(status=404))

    if request.method == 'POST':
        organization.delete()
        messages.success(request, 'Successfully Removed organization!')
        return redirect('startsmart-home')

    context = {
        'organization': organization
    }
    return render(request, 'organizations/delete_organization.html', context)

def browse_organizations(request):
    organizations = Organization.objects.all()

    context = {
        'organizations': organizations,
    }
    return render(request, 'organizations/browse_organizations.html', context)
