from django.http import HttpResponse
from django.shortcuts import render, redirect
from url.models import Url
from url.forms.url.form import LinkForm
from django.contrib import messages
# Create your views here.




def validate(short):
    obj = Url.objects.all().filter(shortened=short).first()
    return True if obj else False


def custom_redirect(request, short):
    if validate(short):
        obj = Url.objects.all().filter(shortened=short).first()
        return redirect(obj.url_link)
    return redirect(custom_redirect_main)


def custom_redirect_main(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            does_exist = form.cleaned_data.get('shortened')
            obj = Url.objects.filter(shortened=does_exist).first()
            if not obj:
                form.save()
                messages.success(request, f"Succesfully created {form.cleaned_data.get('shortened')}")
                return render(request, 'url/index.html')
            messages.error(request, f"{obj.shortened} already exists. Please choose another short code")

        form = LinkForm()
        return render(request, 'url/index.html', {'form': form})
    return render(request, 'url/index.html', {'form': LinkForm})

