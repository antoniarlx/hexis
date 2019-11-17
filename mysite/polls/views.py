from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Populate

class Job:
    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.technical_skills = []
        self.intangible_skills = []

jobA = Job('skillsA', 'Army Infantry Man (11B)')
jobB = Job('skillsB', 'Aviation Ordnance man (AO)')
# jobC = Job('skillsC', 'Job C')

# Write the skills for Job A

jobA.technical_skills = ['Skill1', 'Skill2', 'Skill3']
jobB.technical_skills = ['Skill3', 'Skill4', 'Skill5']
# jobC.technical_skills = ['Skill6', 'Skill7', 'Skill8']

jobA.intangible_skills = ['Skill9', 'Skill10', 'Skill11']
jobB.intangible_skills = ['Skill12', 'Skill13', 'Skill14']
# jobC.intangible_skills = ['Skill15', 'Skill6', 'Skill17']


# Create your views here.

def index(request):

    template = loader.get_template('polls/index.html')

    jobs = [jobA, jobB]
    context = {'veteran_jobs': jobs}

    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse(template.render(context, request))

def skillsA(request):

    template = loader.get_template('polls/skillsA.html')

    technical_skills = jobA.technical_skills
    intangible_skills = jobA.intangible_skills

    context = {'veteran_job': jobA, 'veteran_skills_technical': technical_skills, 'veteran_skills_intangible': intangible_skills}

    return HttpResponse(template.render(context, request))

def skillsB(request):

    template = loader.get_template('polls/skillsB.html')

    technical_skills = jobB.technical_skills
    intangible_skills = jobB.intangible_skills

    context = {'veteran_job': jobB, 'veteran_skills_technical': technical_skills, 'veteran_skills_intangible': intangible_skills}

    return HttpResponse(template.render(context, request))

# def skillsC(request):
#
#     template = loader.get_template('polls/skillsC.html')
#
#     technical_skills = jobC.technical_skills
#     intangible_skills = jobC.intangible_skills
#
#     context = {'veteran_job': jobC, 'veteran_skills_technical': technical_skills, 'veteran_skills_intangible': intangible_skills}
#
#     return HttpResponse(template.render(context, request))
