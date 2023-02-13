from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from emailproject.secret import user_email


def send_email(request):
    if request.method == 'POST':
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = user_email
        send_mail(subject, message, from_email, [to_email])
        messages.success(request, 'Email sent successfully!')
        return redirect('send_email')
    else:
        return render(request, 'senderapp/email_form.html')
