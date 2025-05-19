from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.conf import settings
from django.core.mail import send_mail
from .models import OneTimeCode
from .forms import SignUpForm

def register_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("accounts:login")
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            # 1) generate & email the OTP
            otp = OneTimeCode.create_for_user(user)
            send_mail(
                'Your login code', 
                f'Use this code to complete login: {otp.code}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )
            # 2) stash the OTP id in session & go to verify page
            request.session['otp_id'] = otp.id
            return redirect('accounts:verify')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password.'
            })

    return render(request, 'accounts/login.html')


def verify_view(request):
    otp_id = request.session.get('otp_id')
    if not otp_id:
        return redirect('accounts:login')

    otp = OneTimeCode.objects.filter(id=otp_id).first()
    if request.method == 'POST':
        code = request.POST.get('code')
        if otp and otp.code == code and otp.is_valid():
            otp.used = True
            otp.save()
            auth_login(request, otp.user)
            return redirect('home')           # point to your landing page
        return render(request, 'accounts/verify.html', {
            'error': 'Invalid or expired code.'
        })

    return render(request, 'accounts/verify.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')