from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post',]

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentSerializer(item)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def total_students(self, request):
        user_count = Student.objects.count()
        return Response(user_count)
