from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EmailTable
from .serializers import EmailTableSerializer


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class SendEmail(APIView):
    def post(self, request, *args, **kwargs):
        try:
            Email = request.data["Email"]
            Description = request.data["Description"]
            EMT = EmailTable.objects.get(Email=Email)
            subject = "Salary Information"
            message = f"""
{Description}

Your Salary: {EMT.Salary}
    """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [
                Email,
            ]
            send_mail(subject, message, email_from, recipient_list)
            stat = status.HTTP_200_OK
            report = "Email has been sent successfuly"
        except BaseException:
            stat = status.HTTP_400_BAD_REQUEST
            report = "Theres's been an error,try again later"

        return Response({"report": report}, status=stat)
