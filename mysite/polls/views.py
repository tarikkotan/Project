from django.db import connection
from django.shortcuts import render,redirect
from .forms import CreatePollForm, NewUserForm
from django.http import HttpResponse
from .models import Poll
from django.contrib import messages
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    try:
        poll = Poll.objects.latest('id')
    except:
        return HttpResponse('Exception: Data Not Found')
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count +=1
        elif selected_option == 'option2':
            poll.option_two_count +=1
        elif selected_option == 'option3':
            poll.option_three_count +=1
        else:
            return HttpResponse(400,'Invalid form')
        
        poll.save()
        
        return redirect('home')     
    
    
    context = {'form' : form}
    context = {
        'poll' : poll,
    }
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'poll/create.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/home.html', context)

def vote(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count +=1
        elif selected_option == 'option2':
            poll.option_two_count +=1
        elif selected_option == 'option3':
            poll.option_three_count +=1
        else:
            return HttpResponse(400,'Invalid form')
        
        poll.save()
        
        return redirect('home')     
    context = {
        'poll' : poll
    }
    return render(request, 'poll/home.html', context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Kayıt Başarılı." )
            return redirect("/")
        messages.error(request, "Başarısız kayıt olma. Yanlış bilgi girdiniz.")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"{username} kullanıcı adı ile giriş yapıldı.")
                return redirect("/")
            else:
                messages.error(request,"Geçersiz kullanıcı adı veya şifre.")
        else:
            messages.error(request,"Geçersiz kullanıcı adı veya şifre.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Başarılı bir şekilde çıkış yapıldı.") 
    return redirect("/")