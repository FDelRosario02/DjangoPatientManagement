from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpFrom, AddRecordForm, AddPatientForm
from .models import Record
from .models import Patient


# Create your views here.
def home(request):
    records= Record.objects.all()
    patients= Patient.objects.all()

    #Check de Loggin
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        #check if authentication is successful
        if user is not None:
            login(request,user)
            messages.success(request,"Bem vindo!")
            return redirect('home')
        else:
            messages.success(request,'Incorrect password or username')
            return redirect('home')
    else:
        return render(request, 'home.html',{'records' : records,  'patients' : patients})


    

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form= SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and Login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,f"Account created for {username}. You are now logged in.")
            return redirect('home')  
    else: 
        form=SignUpFrom()
        return render(request, 'register.html',{'form' :form})
    return render(request, 'register.html',{'form' :form})

def costumer_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        customer_record = Record.objects.get(id=pk) 
        return render(request, 'record.html',{'customer_record' :customer_record})
    else:
        messages.warning(request,"Please Log In to View Details")
        messages.success(request,f"Deberías de Loggearte bb")
        return redirect('home')  
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.error(request, f"Record deleted!")
        return redirect('home')
    else:
        messages.warning(request,"Please Log In to View Details")
        messages.success(request,f"Deberías de Loggearte bb")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                record = form.save()
                messages.success(request, f"New Record added!")
                return redirect('home')
        return render(request, 'add_record.html',{'form':form})
    else:
        messages.info(request,'You must be logged in to do that action')
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record) 
        if form.is_valid():
                form.save()
                messages.success(request, f"{current_record.first_name} has been updated.")
                return redirect('home')
        return render(request, 'update_record.html',{'form':form})
    else:
        messages.info(request,'You must be logged in to do that action')
        return redirect('home')
    
def patient_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        patient_record = Patient.objects.get(id=pk) 
        return render(request, 'patient.html',{'patient_record' :patient_record})
    else:
        messages.warning(request,"Please Log In to View Details")
        messages.success(request,f"Deberías de Loggearte bb")
        return redirect('home')
    
def add_patient(request):
    form = AddPatientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                record = form.save()
                messages.success(request, f"New patient added!")
                return redirect('home')
        return render(request, 'add_patient.html',{'form':form})
    else:
        messages.info(request,'You must be logged in to do that action')
        return redirect('home')