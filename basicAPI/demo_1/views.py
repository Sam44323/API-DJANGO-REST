from django.shortcuts import render
from demo_1.models import AccessRecord, Topic, Webpage

# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    print(webpages_list)
    date_dict = {'access_records': webpages_list}
    return render(request, 'demo_1/index.html', context=date_dict)
