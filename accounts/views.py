from django.shortcuts import render,redirect
from django.core.mail import send_mail

from .forms import SignupForm,ActivateForm
from .models import Profile
from django.contrib.auth.models import User




def signup(request):
    
    '''
     - create new user
     - send email to this user
     - stop active this user
     - redirect to activate html

    '''
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            user=form.save(commit=False)
            user.is_active=False
            form.save()  # create profile
            # send email

            profile=Profile.objects.get(user__username=username)
            send_mail(
            "Activate code",
            f"welcome mr {username}\n pls use this code {profile.code}",
            "r_mido99@yahoo.com",
            [email],
            fail_silently=False,
                        )
            return redirect(f'/accounts/activate/{username}')
            

    else:
        form=SignupForm()

    
    return render(request,'accounts/signup.html',{'form':form})

def activate(request,username):
    '''
    - check this user
    - active this user
    - redirect login
    '''
    profile=Profile.objects.get(user__username=username)
    if request.method=='POST':
        form=ActivateForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code == profile.code:
                profile.code=''

                user=User.objects.get(username=username)
                user.is_active=True
                profile.save()
                user.save()

                return redirect('/accounts/login')
    else:
        form=ActivateForm()

    return render(request,'accounts/activate.html',{'form':form})

