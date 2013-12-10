from django.contrib.auth import authenticate
from django.shortcuts import render, render_to_response, get_object_or_404

# Create your views here.
from django.contrib.auth import authenticate, login as lin, logout as lout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from web.forms import LoginForm
from django.forms.util import ErrorList
from django.utils.translation import ugettext_lazy as _
from web.models import Action


@login_required
def home(request):
    return render_to_response('index.html', {'actions': request.user.actions.order_by('name'),}, RequestContext(request=request))


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', {'form': form}, RequestContext(request=request))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    lin(request, user)
                    if 'next' in request.GET:
                        return redirect(request.GET['next'])
                    else:
                        return redirect('home')
                else:
                    form._errors["login"] = ErrorList(u'Account disabled')
                    return render_to_response('login.html', {'form': form})
            else:
                form._errors["login"] = ErrorList(u'Invalid login')

        # Return an 'invalid login' error message.
        return render_to_response('login.html', {'form': form}, RequestContext(request=request))


def logout(request):
    lout(request)

    return redirect('home')


def do(request, id):
    action = get_object_or_404(Action, id=id)
    if action:
        import subprocess
        p = subprocess.Popen(action.command, stdout=subprocess.PIPE, shell=True)
        output, err = p.communicate()

    return render_to_response('index.html', {'actions': request.user.actions.order_by('name'),'message': output.replace('\n','<br />')}, RequestContext(request=request))