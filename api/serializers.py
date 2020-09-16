from rest_framework import serializers
from api.models import Todo, Achievements


class AchievementsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Achievements
        fields = ('id', 'owner', 'todo', 'objective', 'created_at',
                  'updated_at', 'is_public', 'task')


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    achievements = AchievementsSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Todo
        fields = ('id', 'objective', 'owner', 'created_at', 'updated_at',
                  'task', 'achievements')
