from django.db.models import Q
from django.http import Http404, HttpResponse, HttpResponseServerError
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from JsonToken.models import Student,Branch
from JsonToken.serializer import StudentSerializer,BranchSerializer

class StudentAPIView(APIView):
    permission_classes=(IsAuthenticated,)
    
    def get(self,request):
        queryset=Student.objects.all()
        serializer=StudentSerializer(queryset,many=True)
        return Response(serializer.data)



class BranchAPIView(APIView):
    permission_classes=(IsAuthenticated,)
    
    def get(self,request):
        queryset=Branch.objects.all()
        serializer=BranchSerializer(queryset,many=True)
        return Response(serializer.data)