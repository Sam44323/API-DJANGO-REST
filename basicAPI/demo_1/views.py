from django.shortcuts import render
from demo_1.models import AccessRecord, Topic, Webpage
from . import forms

# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'demo_1/index.html', context=date_dict)


def form_name_view(request):
    form = forms.NewUser()

    if request.method == 'POST':
        form = forms.NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # redirecting to route present in the index function
            return index(request)
        else:
            print('FORM IS INVALID')

    return render(request, 'demo_1/forms.html', {'form': form})
