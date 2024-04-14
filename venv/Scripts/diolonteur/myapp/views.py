from django.shortcuts import render
from django.http import HttpResponse
from .models import Request, our_user
from .forms import PropositionForm, RequestForm, Proposition

def index(request):
    if '_auth_user_id' in request.session.keys():
        return render(
            request,
            "index.html",
            {
                'title': our_user.objects.get(id = request.session['_auth_user_id']).name.capitalize()
            }
        )
    else:
        return render(
            request,
            "index.html",
            {
                'title': 'Dionysus'
            }
        )
def volonteur(request):
    if '_auth_user_id' not in request.session.keys():
        return redirect('/register/')
    else:
        return render(request, 'volonteur.html', {'name': our_user.objects.get(id = request.session['_auth_user_id']).name.capitalize()})

def victims(request):
    if '_auth_user_id' not in request.session.keys():
        return redirect('/register/')
    else:
        return render(request, 'victim.html', {'name': our_user.objects.get(id =request.session['_auth_user_id']).name.capitalize() })

def requests(request,request_id ):
    r = Request.objects.get(id=request_id)
    print(r)
    return HttpResponse('You are watching request %s. Short desc: %s' % (r.title, r.short_description))




from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('/')  # перенаправлення на головну сторінку після реєстрації
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def add_proposition(request):
    if request.method == 'POST':
        form = PropositionForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            p = Proposition(user_id= request.session['_auth_user_id'], title = clean['title'], cat=clean['cat'], proposition_text= clean['proposition_text'])
            p.save()
            return redirect('/')
    else:
        form = PropositionForm()
    return render(request, 'proposition.html', {'form':form})

def add_req(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            r = Request(user_id=request.session['_auth_user_id'], title=clean['title'], cat=clean['cat'],
                            request_text=clean['request_text'])
            r.save()
            return redirect('/')
    else:
        form = RequestForm()
    return render(request, 'add_req.html', {'form':form})