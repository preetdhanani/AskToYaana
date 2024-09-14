
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User, auth 
from django.contrib.auth.decorators import login_required   
from django.contrib import messages
from .forms import QueryForm, CustomUserCreationForm
from PIL import Image 
import os
from langchain_groq import ChatGroq
from django.utils.safestring import mark_safe
from .models import GeneratedText
from django.utils import timezone





GROQ_API_KEY = "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"
llm = ChatGroq(api_key=GROQ_API_KEY, model_name='llama-3.1-8b-instant')
pre_prompt = """
                you are a beauty expert and suggest advice to user based on skin problem with three to four beauty products with description, 
                usage and give price in doller and give daily routine to used these suggested product and give nutrition advice to ebhance user's skin
                """

def convert_to_bold(text):
            parts = text.split('**')
            result = ''
            bold = False
            for part in parts:
                if bold:
                    result += f'<strong>{part}</strong>'
                else:
                    result += part
                bold = not bold
            return mark_safe(result)

def process(text):
    full_prompt = f"{pre_prompt}\n\nUser: {text}"
    response = llm.invoke(full_prompt)
    response = convert_to_bold(response.content)
    response = mark_safe(response.replace('*', '•'))
    return response
    
    
@login_required(login_url='login')
def AskToYaana(request):
    
    if request.method == 'POST':

        text1 = request.POST.get('input_text')
        past_records = GeneratedText.objects.all().order_by('-created_at')
        if text1 is not None:
            response = process(text1)
            new_record = GeneratedText.objects.create(user=request.user, input_text=text1, text=response)
            past_records = GeneratedText.objects.filter(user=request.user).order_by('-created_at')
            return render(request, 'AskToYaana.html', {'response': response, 'past_records': past_records})
    past_records = GeneratedText.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'AskToYaana.html',{'past_records': past_records})


def registerpage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Registration successful! by '+ user)
            
            return redirect('login')


    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('AskToYaana')
        else:
            messages.warning(request, 'Invalid credentials')
            return render(request, 'login.html')    
    else:
        
        return render(request, 'login.html')
    
def logoutuser(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def record_detail(request, pk):
    
    text = GeneratedText.objects.get(id=pk)
    context = {'record': text}
    

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User, auth 
from django.contrib.auth.decorators import login_required   
from django.contrib import messages
from .forms import QueryForm, CustomUserCreationForm
from PIL import Image 
import os
from langchain_groq import ChatGroq
from django.utils.safestring import mark_safe
from .models import GeneratedText
from django.utils import timezone





GROQ_API_KEY = "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"
llm = ChatGroq(api_key=GROQ_API_KEY, model_name='llama-3.1-8b-instant')
pre_prompt = """
                you are a beauty expert and suggest advice to user based on skin problem with three to four beauty products with description, 
                usage and give price in doller and give daily routine to used these suggested product and give nutrition advice to ebhance user's skin
                """

def convert_to_bold(text):
            parts = text.split('**')
            result = ''
            bold = False
            for part in parts:
                if bold:
                    result += f'<strong>{part}</strong>'
                else:
                    result += part
                bold = not bold
            return mark_safe(result)

def process(text):
    full_prompt = f"{pre_prompt}\n\nUser: {text}"
    response = llm.invoke(full_prompt)
    response = convert_to_bold(response.content)
    response = mark_safe(response.replace('*', '•'))
    return response
    
    
@login_required(login_url='login')
def AskToYaana(request):
    
    if request.method == 'POST':

        text1 = request.POST.get('input_text')
        past_records = GeneratedText.objects.all().order_by('-created_at')
        if text1 is not None:
            response = process(text1)
            new_record = GeneratedText.objects.create(user=request.user, input_text=text1, text=response)
            past_records = GeneratedText.objects.filter(user=request.user).order_by('-created_at')
            return render(request, 'AskToYaana.html', {'response': response, 'past_records': past_records})
    past_records = GeneratedText.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'AskToYaana.html',{'past_records': past_records})


def registerpage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Registration successful! by '+ user)
            
            return redirect('login')


    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('AskToYaana')
        else:
            messages.warning(request, 'Invalid credentials')
            return render(request, 'login.html')    
    else:
        
        return render(request, 'login.html')
    
def logoutuser(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def record_detail(request, pk):
    
    text = GeneratedText.objects.get(id=pk)
    context = {'record': text}
    
    return render(request, 'record_detail.html', context)