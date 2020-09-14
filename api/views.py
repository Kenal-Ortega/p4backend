from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models import Todo, Achievements
from api.serializers import TodoSerializer, AchievementsSerializer


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # list  categories per current logged user
        queryset = Todo.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = TodoSerializer

    def create(self, request):
        # check if category already exists for current logged in user
        todo = Todo.objects.filter(
            name=request.data.get('objective'),
            owner=request.user
        )
        if todo:
            msg = 'Todo with that objective already exists'
            raise ValidationError(msg)
        return super().create(request)

        # user can only delete category

    def destroy(self, request, *args, **kwargs):
        todo = Todo.objects.get(pk=self.kwargs["pk"])
        if not request.user == todo.owner:
            raise PermissionDenied("You can not delete this objective")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SingleTodoAchievements(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.kwargs.get('todo_pk') and self.kwargs.get('pk'):
            todo = Todo.objects.get(pk=self.kwargs['todo_pk'])
            queryset = Achievements.objects.filter(
                pk=self.kwargs['pk'],
                owner=self.request.user,
                todo=todo
            )
            return queryset


class AchievementsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AchievementsSerializer

    def get_queryset(self):
        queryset = Achievements.objects.all().filter(owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create todos"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        achievements = Achievements.objects.get(pk=self.kwargs["pk"])
        if not request.user == achievements.owner:
            raise PermissionDenied(
                "You have no permissions to delete these achievements"
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        achievements = Achievements.objects.get(pk=self.kwargs["pk"])
        if not request.user == achievements.owner:
            raise PermissionDenied(
                "You have no permissions to edit this achievements"
            )
        return super().update(request, *args, **kwargs)
