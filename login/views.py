from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
from email.mime.text import MIMEText
from tkinter import E
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from login.models import User
import smtplib
from login_api import settings

from .serializers import UserSerializer


class userViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


def send_email(destinatario, subject):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)

        # Construimos el mensaje simple
        mensaje = MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = destinatario
        mensaje['Subject'] = subject

        content = render_to_string('send_email.html')
        mensaje.attach(MIMEText(content, 'html'))

        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST_USER,destinatario, mensaje.as_string())

    except Exception as e:
        print(e)
send_email('alexcs252002@gmail.com','Correo de recuperacion de datos')
