from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from crew.forms import LoginForm
from crew.models import Crew
from django.contrib.auth import authenticate, login, logout

def LoginRequest(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/profile/')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        crew = authenticate(username=username, password=password)
                        if crew is not None:
                                login(request, crew)
                                return HttpResponseRedirect('/profile/')
                        else:
                                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
        logout(request)
        return HttpResponseRedirect('/')

@login_required
def UserProfile(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/login/')
        crew = request.user.profile.nickname
        first_name  = request.user.profile.first_name
        last_name   = request.user.profile.last_name
        nickname    = request.user.profile.nickname
        phone       = request.user.profile.phone
        department  = request.user.profile.department
        lang        = request.user.profile.lang
        superint    = request.user.profile.superint
        foreman     = request.user.profile.foreman
        estimator   = request.user.profile.estimator
        sales_rep   = request.user.profile.sales_rep
        crew_pic    = request.user.profile.crew_pic
        context     = {'crew': crew}
        return render_to_response('profile.html', context, context_instance=RequestContext(request))
