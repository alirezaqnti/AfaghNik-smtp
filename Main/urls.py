from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexTemplateView.as_view(), name="IndexTemplateView"),
    path("send-email/", views.SendEmail.as_view(), name="SendEmail"),
]
