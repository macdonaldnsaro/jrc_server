from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from core.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
User = get_user_model()
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST or None)
        if form.is_valid():
            print("this Form is valid")
            user = form.save(commit=False)
            user.is_active = False
            new_password = form.cleaned_data.get('password')
            user.set_password(new_password)
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('authentication/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your account In Bin Suleiman Systems.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

    else:
        if request.method == 'GET':
            form = SignupForm(request.POST or None)
            if form.is_valid()  :
                user = form.save(commit=False)
                user.is_active = False
                new_password = form.cleaned_data.get('password')
                user.set_password(new_password)
                user.save()
                current_site = get_current_site(request)
                message = render_to_string('authentication/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                mail_subject = 'Activate your account In Bin Suleiman Systems.'
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')

    return render(request, 'authentication/signup.html', {'form': form})
    # return render(request, 'signup.html', {'form': form})
from django.urls import reverse
def activate(request, uidb64, token: str):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        # return redirect(reverse('payment:process'))
        return render(request, 'authentication/thanx.html')
    else:
        return render(request, 'authentication/thanx.html')

