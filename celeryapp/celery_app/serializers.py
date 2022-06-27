from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from .models import ApiResponse


class ApiResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiResponse
        fields = "__all__"
