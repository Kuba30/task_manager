from rest_framework import viewsets

from .models import Category, Tag, Task
from .serializers import (
    CategorySerializer,
    TagSerializer,
    TaskDetailSerializer,
    TaskListSerializer,
)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("category").prefetch_related("tags")

    def get_serializer_class(self):
        if self.action == "list":
            return TaskListSerializer
        return TaskDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


from django.shortcuts import render

# Create your views here.
