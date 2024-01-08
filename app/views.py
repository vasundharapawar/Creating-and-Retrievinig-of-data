from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length

from django.db.models import Q

def display_topics(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('-topic_name')
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.all()[2:5:]
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by(Length('name'))
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by(Length('name').desc())
    QLWO=Webpage.objects.exclude(topic_name='Cricket').order_by('name')
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(name__startswith='V')
    
    QLWO=Webpage.objects.filter(url__endswith='com')
    
    QLWO=Webpage.objects.filter(name__contains='r')
    QLWO=Webpage.objects.filter(name__regex='\w+t$')
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') | Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(email__startswith='india'))
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name__startswith='R'))
    QLWO=Webpage.objects.all()
    
    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)



def insert_topic(request):
    tn=input('enter topic Name')

    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()

    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')

    TO=Topic.objects.get(topic_name=tn)

    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()

    return HttpResponse('Webpage is created')



def display_access(request):

    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(id__lte=4)
    QLAO=AccessRecord.objects.filter(date__lt='2023-12-19')
    
    QLAO=AccessRecord.objects.filter(date='2023-12-19')
    
    QLAO=AccessRecord.objects.filter(date__year='2023')
    
    QLAO=AccessRecord.objects.filter(date__month='12')
    
    QLAO=AccessRecord.objects.filter(date__day='19')
    
    QLAO=AccessRecord.objects.filter(pk__in=[3,6])
    
    QLAO=AccessRecord.objects.filter(date__year__gt='2022')












    
    
    d={'access':QLAO}
    return render(request,'display_access.html',d)









def update_webpage(request):

    #Webpage.objects.filter(topic_name='Volley').update(name='msd')
    #Webpage.objects.update_or_create(topic_name='Volley Ball',defaults={'name':'Virat'})
    #Webpage.objects.update_or_create(topic_name='Cricket',defaults={'name':'Virat'})
    #Webpage.objects.filter(name='Virat').update(topic_name='Cricket')
    #Webpage.objects.filter(name='Virat').update(topic_name='Volley Ball')
    #Webpage.objects.filter(name='Virat').update(url='https://harshad.in')
    CTO=Topic.objects.get_or_create(topic_name='Cricket')[0]
    CTO.save()

    #Webpage.objects.update_or_create(name='Virat',defaults={'topic_name':CTO})
    
    #Webpage.objects.update_or_create(topic_name='Cricket',defaults={'name':'harshad'})
    
    #Webpage.objects.update_or_create(name='Virat',defaults={'topic_name':'Foot Ball'})
    Webpage.objects.update_or_create(name='Suresh Raina',defaults={'url':'http://suresh.in','email':'suresh@gmail.com'})
    
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)



























