from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserLoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import Record
from django.contrib import messages

# -Homepage
def index(request):
    
    # return HttpResponse('Hello world')
    
    return render(request, 'webapp/index.html')


# -Create user
def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Account created successfully')
            return redirect('webapp:login')
            
    context = {'form':form}
    
    return render(request, 'webapp/register.html', context=context)

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('webapp:dashboard')
            else:
                print("Authentication failed. User is None.")
        else:
            print("Form is invalid. Errors:", form.errors)

    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "webapp/login.html", context=context)


@login_required(login_url='webapp:login')
def dashboard(request):
    records = Record.objects.all()
    context = {'records': records}
    return render(request, 'webapp/dashboard.html', context)


@login_required(login_url='webapp:login')
def create_record(request):
    form = CreateRecordForm()
    img_obj = None
    
    if request.method =="POST":
        form = CreateRecordForm(request.POST, request.FILES)
        
        
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            
            messages.success(request, 'Record created successfully')
            return redirect('webapp:dashboard')
            
    context = {'form':form,
               'img':img_obj}
    
    return render(request, 'webapp/create_record.html', context=context)


@login_required(login_url='webapp:login')
def update_record(request, pk):
    
    record = Record.objects.get(id=pk)
    
    form = UpdateRecordForm(instance=record)
    
    if request.method == "POST":
        print("Form submitted successfully")
        form = UpdateRecordForm(request.POST, request.FILES, instance=record)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully')
            return redirect('webapp:record',record.pk)
        else:
            print(form.errors)

            
            # return redirect('webapp:dashboard')
    
    context = {'form':form}
    
    return render(request, 'webapp/update_record.html', context=context)
            
            
        
        

@login_required(login_url='webapp:login')
def view_record(request, pk):
    
    record = Record.objects.get(id=pk)
    context = {'record':record}
    
    return render(request, 'webapp/view_record.html', context=context)


@login_required(login_url='webapp:login')
def delete_record(request, pk):
    
    record = Record.objects.get(id=pk)
    
    record.delete()
    
    messages.success(request, 'Record deleted successfully')
    return redirect('webapp:dashboard')


@login_required(login_url='webapp:login')
def user_logout(request):
    auth.logout(request)
    
    messages.success(request, 'You have been logged out')
    return redirect("webapp:login")