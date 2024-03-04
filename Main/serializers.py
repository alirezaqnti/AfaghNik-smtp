from rest_framework import serializers

from .models import EmailTable


class EmailTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTable
        fields = [
            "Email",
        ]
