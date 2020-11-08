from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

# Create your views here.
from s4in.models import Projects
from s4in.models import *
from s4in.widgets import mailSubmit


def index(request):
    projects = Projects.objects.filter(showInMainPage=True)
    lastFiveProjects = Projects.objects.filter(showInMainPage=True).order_by('-id')[:5]
    projectsTypes=Projects._meta.get_field('type').choices
    projectsTypesList=[]
    for i in projectsTypes:
        projectsTypesList.append(i[0])

    sectors = Sectors.objects.all()
    mainPage=MainPage.objects.first()
    aboutUs=AboutUs.objects.first()
    services=Services.objects.all()
    whyUs=WhyUs.objects.first()
    advantages=Advantages.objects.all()
    address=Address.objects.first()
    mailSubmit(request)

    context= {'projects':projects,'sectors':sectors,
              'mainPage':mainPage,'aboutUs':aboutUs,'services':services,
              'whyUs':whyUs,'advantages':advantages,'address':address,
              'projectsTypesList':projectsTypesList,'lastFiveProjects':lastFiveProjects}
    return render(request,'index.html',context)

def detail(request,pk):
    projects = Projects.objects.filter(showInMainPage=True)
    thisProject = Projects.objects.get(id=pk)
    images = Pictures.objects.filter(project__id=pk)
    lastFiveProjects = Projects.objects.filter(showInMainPage=True).order_by('-id')[:5]
    projectsTypes = Projects._meta.get_field('type').choices
    projectsTypesList = []
    for i in projectsTypes:
        projectsTypesList.append(i[0])

    mailSubmit(request)
    address = Address.objects.first()

    context = {'thisProject':thisProject,'projects': projects, 'address': address,'images':images,
               'projectsTypesList': projectsTypesList, 'lastFiveProjects': lastFiveProjects}

    return render(request, 'details.html', context)


def references(request):
    projects = Projects.objects.filter(showInMainPage=True)
    lastFiveProjects = Projects.objects.filter(showInMainPage=True).order_by('-id')[:5]
    projectsTypes = Projects._meta.get_field('type').choices
    projectsTypesList = []
    for i in projectsTypes:
        projectsTypesList.append(i[0])
    mailSubmit(request)
    sectors = Sectors.objects.all()
    mainPage = MainPage.objects.first()
    aboutUs = AboutUs.objects.first()
    services = Services.objects.all()
    whyUs = WhyUs.objects.first()
    advantages = Advantages.objects.all()
    address = Address.objects.first()

    context = {'projects': projects, 'sectors': sectors,
               'mainPage': mainPage, 'aboutUs': aboutUs, 'services': services,
               'whyUs': whyUs, 'advantages': advantages, 'address': address,
               'projectsTypesList': projectsTypesList, 'lastFiveProjects': lastFiveProjects}
    return render(request, 'projects.html', context)


def contacts(request):
    projects = Projects.objects.filter(showInMainPage=True)
    lastFiveProjects = Projects.objects.filter(showInMainPage=True).order_by('-id')[:5]
    projectsTypes = Projects._meta.get_field('type').choices
    projectsTypesList = []
    for i in projectsTypes:
        projectsTypesList.append(i[0])
    mailSubmit(request)
    sectors = Sectors.objects.all()
    mainPage = MainPage.objects.first()
    aboutUs = AboutUs.objects.first()
    services = Services.objects.all()
    whyUs = WhyUs.objects.first()
    advantages = Advantages.objects.all()
    address = Address.objects.first()

    context = {'projects': projects, 'sectors': sectors,
               'mainPage': mainPage, 'aboutUs': aboutUs, 'services': services,
               'whyUs': whyUs, 'advantages': advantages, 'address': address,
               'projectsTypesList': projectsTypesList, 'lastFiveProjects': lastFiveProjects}
    return render(request, 'contact.html', context)


def aboutUs(request):
    projects = Projects.objects.filter(showInMainPage=True)
    lastFiveProjects = Projects.objects.filter(showInMainPage=True).order_by('-id')[:5]
    projectsTypes = Projects._meta.get_field('type').choices
    projectsTypesList = []
    for i in projectsTypes:
        projectsTypesList.append(i[0])

    sectors = Sectors.objects.all()
    mainPage = MainPage.objects.first()
    aboutUs = AboutUs.objects.first()
    services = Services.objects.all()
    whyUs = WhyUs.objects.first()
    advantages = Advantages.objects.all()
    address = Address.objects.first()
    mailSubmit(request)
    context = {'projects': projects, 'sectors': sectors,
               'mainPage': mainPage, 'aboutUs': aboutUs, 'services': services,
               'whyUs': whyUs, 'advantages': advantages, 'address': address,
               'projectsTypesList': projectsTypesList, 'lastFiveProjects': lastFiveProjects}
    return render(request, 'aboutus.html', context)
