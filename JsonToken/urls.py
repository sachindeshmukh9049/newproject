from django.urls import path
from JsonToken.views import StudentAPIView,BranchAPIView

urlpatterns = [
    path('student/', StudentAPIView.as_view()),
    path('branch/', BranchAPIView.as_view()),
]
