from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from .filters import TasksFilter
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filterset_class = TasksFilter

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user).prefetch_related('tags')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        return TaskSerializer
    
    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        qs = Tasks.objects.filter(user = self.request.user).prefetch_related('tags')

        total_task = qs.count()
        completed_task = qs.filter(status=True).count()
        pending_task = qs.filter(status=False).count()

        return Response({
            'total_task':total_task,
            'completed_task':completed_task,
            'pending_task':pending_task
        })


    