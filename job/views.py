from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from job.models import Job
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from crew.models import Crew
from django.contrib.auth import authenticate, login, logout
from django.utils.html import urlize
from django.utils.safestring import mark_safe
import re

# Create your views here.

def Index(request):
        
        return render_to_response('index.html')



def JobsAll(request):
	jobs = Job.objects.all().order_by('job_number')
	context = {'jobs': jobs }
	return render_to_response('jobsall.html', context,  context_instance=RequestContext(request))


def SpecificJob(request, jobslug):
	job = Job.objects.get(slug=jobslug)
	context = { 'job': job }
	return render_to_response('singlejob.html', context, context_instance=RequestContext(request))


@login_required
def UserProfile(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/login/')
        crew = request.user.profile.name
        phone   = request.user.profile.phone
        context = {'crew': crew}
        return render_to_response('jobsall.html', context, context_instance=RequestContext(request))

