from django.shortcuts import render
from .models import *

def index(request):
    about = About.objects.get(pk=1)
    social = Social.objects.all()
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    project = Project.objects.all()
    contact = Contact.objects.all()
    context = {'about':about,
               'social':social,
               'experience':experience,
               'skill':skill,
               'project': project,
               'contact':contact,
               }
    return render(request, 'base/index.html', context)

