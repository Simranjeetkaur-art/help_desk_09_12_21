



from django.core.mail import send_mail
import uuid
from django.conf import settings

def send_forget_password_mail(email , token ):
    # token =  str(uuid.uuid4())
    subject ="Your forget Password Link"
    message = f'hi, click on the link to reset ypur password http://127.0.0.1:8000/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list =[email]
    send_mail(subject,message, email_from, recipient_list)
    return True