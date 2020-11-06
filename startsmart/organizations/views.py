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
    organization = Organization.objects.get(name=organization_name)

    context = {
        'organization': organization
    }
    return render(request, 'organizations/view_organization.html', context)
