from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework import viewsets

# @api_view(['GET'])
# def student_list(request):
#     studentsobj = Student.objects.all()
#     student_serializer = StudentSerializer(studentsobj, many=True)
#     return Response(student_serializer.data)


# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request):
#         return self.list(request)

# class CreateStudent(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def post(self, request):
#         return self.create(request)

# class StudentList(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)
    
# class GetPutDelete(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, **kwargs):
#         return self.retrieve(request)
#     def put(self, request, **kwargs):
#         return self.update(request)
#     def delete(self, request, **kwargs):
#         return self.delete(request)
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer