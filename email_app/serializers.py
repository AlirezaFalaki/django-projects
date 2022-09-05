from rest_framework import serializers
from . models import Email


class EmailSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Email
        exclude = ['created']
