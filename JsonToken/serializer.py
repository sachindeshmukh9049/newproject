from JsonToken.models import Student,Branch
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields='__all__'