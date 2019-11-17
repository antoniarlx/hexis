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

# Write the skills for Job A

jobA.technical_skills = ['Coordinated joint activities with team to accomplish set goals within rigid deadlines.', 'Regularly participated in map reading and land navigation using satellite imaging.', 'Mastered the disassembly, cleaning, maintenance and reassembly of equipment.', 'Experienced in driving vehicles ranging in size from 4,000 to 10,000 pounds.', 'Competent in reviewing and implementing procedures for machine operation.', 'Performed safety tests using computerized simulators to prepare for real world environments.', 'Trained in basic first aid, triage and applications to emergency situations.', 'Assisted in relief efforts including transportation of people and delivery of supplies.', 'Maintained a personal fitness routine and provided instructions to team members.']

jobB.technical_skills = ['Managed mechanical and electrical repair tasks of aircraft', 'Managed the training and development of assigned electricians', 'Executed and adhered to Management of Change process with requests', 'Directed the activities of maintenance personnel with the accountability of safety, quality, and cost', 'Identified improvements to effectiveness and efficiency in projects', 'Directed preventive/predictive maintenance programs designed to reduced unscheduled downtime']

jobA.intangible_skills = ['Quickly adapts to new situations', 'Skilled at working with teams', 'Analytical and detail oriented', 'Performs well under pressure', 'Learns new tasks quickly', 'Eager to accept challenges']
jobB.intangible_skills = ['Ability to perform tasks with minimal supervision', 'Analytical and detailed oriented', 'Strong work ethic', 'Quickly adapts to new situations', 'Performs well under pressure', 'Eager to accept challenges']


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
