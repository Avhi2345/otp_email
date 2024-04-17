# appname/views.py
from django.shortcuts import render,redirect
import random
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


# Function to generate a random 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

def my_view(request):
    if request.method == 'POST':
        email = request.POST['email']

        # Generate and send OTP
        otp = generate_otp()
        subject = 'OTP for Verification'
        message = f'Your OTP is: {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list =  [email]
        send_mail(subject, message, email_from, recipient_list)
        # Store OTP in the session
        request.session['otp'] = otp

        return redirect('verify_otp')

    return render(request, 'my_template.html')

def verify_otp(request):
    if request.method == 'POST':
        user_entered_otp = request.POST['otp']
        stored_otp = request.session.get('otp')
        print(stored_otp)

        if user_entered_otp == stored_otp:
            # OTP is correct, redirect to success page
            return redirect('otp_success')
        else:
            return render(request, 'otp_verification.html', {'message':'Invalid OTP. Please try again...'})

    return render(request, 'otp_verification.html')
def otp_success(request):
    return render(request, 'otp_success.html')

