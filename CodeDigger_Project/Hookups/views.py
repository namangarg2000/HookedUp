from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import ProjectForm
from .models import Project

def home(request):
	return render(request,'Hookup/home.html')

def signupuser(request):
	if request.method=='GET':
		return render(request,'Hookup/signupuser.html',{'form':UserCreationForm()})
	else:
		if request.POST['password1']==request.POST['password2']:
			try:
				user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
				user.save()
				login(request,user)
				return redirect('home')

			except IntegrityError:
				return render(request,'Hookup/signupuser.html',{'form':UserCreationForm(),'error':'UserName Already Taken'})

		else:
			return render(request,'Hookup/signupuser.html',{'form':UserCreationForm(),'error':'Password and Confirm Password is not same'})

def loginuser(request):
	if request.method=='GET':
		return render(request,'Hookup/loginuser.html',{'form':AuthenticationForm()})
	else:
		user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
		if user is None:
			return render(request,'Hookup/loginuser.html',{'form':AuthenticationForm(),'error':'Invalid UserName Or Password'})
		else:
			login(request,user)
			return redirect('home')

def logoutuser(request):
	if request.method=='POST':
		logout(request)
		return redirect('home')

def createprojects(request):
	if request.method=='GET':
		return render(request,'Hookup/createprojects.html',{'form':ProjectForm()})
	else:
		try:
			form= ProjectForm(request.POST)
			newproject = form.save(commit=False)
			newproject.user=request.user
			newproject.save()
			return redirect('myprojects')
		except ValueError:
			return render(request,'Hookup/createprojects.html',{'form':ProjectForm(),'error':'Bad data entered!'})

def myprojects(request):
	projects = Project.objects.filter(user=request.user)
	return render(request,'Hookup/myprojects.html',{'projects':projects})

def webdevelopment(request):
	projects = Project.objects.filter(categories='WebDevelopment')
	return render(request,'Hookup/webdevelopment.html',{'projects':projects})

def androiddevelopment(request):
	projects = Project.objects.filter(categories='AndroidDevelopment')
	return render(request,'Hookup/androiddevelopment.html',{'projects':projects})

def blockchain(request):
	projects = Project.objects.filter(categories='BlockChain')
	return render(request,'Hookup/blockchain.html',{'projects':projects})

def iot(request):
	projects = Project.objects.filter(categories='IOT')
	return render(request,'Hookup/iot.html',{'projects':projects})

def machinelearning(request):
	projects = Project.objects.filter(categories='MachineLearning')
	return render(request,'Hookup/machinelearning.html',{'projects':projects})

def iosdevelopment(request):
	projects = Project.objects.filter(categories='IosDevelopment')
	return render(request,'Hookup/iosdevelopment.html',{'projects':projects})

def datascience(request):
	projects = Project.objects.filter(categories='DataScience')
	return render(request,'Hookup/datascience.html',{'projects':projects})

def others(request):
	projects = Project.objects.filter(categories='Others')
	return render(request,'Hookup/others.html',{'projects':projects})

def viewprojects(request,Hookup_pk):
	hookup=get_object_or_404(Project, pk=Hookup_pk)
	return render(request,'Hookup/viewprojects.html',{'hookup':hookup})

def userviewproject(request,hookup_pk):
	hookup=get_object_or_404(Project, pk=hookup_pk,user=request.user)
	if request.method=='GET':
		form= ProjectForm(instance=hookup)
		return render(request,'Hookup/userviewproject.html',{'form':form})
	else:
		try:
			form= ProjectForm(request.POST,instance=hookup)
			form.save()
			return redirect('myprojects')
		except ValueError:
			return render(request,'Hookup/userviewproject.html',{'form':form,'error':'Bad Data Entered'})



