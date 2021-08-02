from demo_1.models import AccessRecord, Topic, Webpage
from faker import Faker
import random
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basicAPI.settings')

# configuring django for script

django.setup()


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
