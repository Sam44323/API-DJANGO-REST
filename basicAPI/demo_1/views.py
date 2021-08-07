from django.shortcuts import render
from demo_1.models import AccessRecord, Topic, Webpage
from . import forms

# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'demo_1/index.html', context=date_dict)


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("You are validated!")
            print("Name: {0}".format(form.cleaned_data["name"]))
            print("Email: {0}".format(form.cleaned_data["email"]))
            print("Text: {0}".format(form.cleaned_data["text"]))

    return render(request, 'demo_1/forms.html', {'form': form})
