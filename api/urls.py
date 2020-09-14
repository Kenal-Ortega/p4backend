from django.conf.urls import url
from rest_framework import routers
from api.views import TodoViewSet, TodoAchievements, SingleTodoAchievements, AchievementsViewSet

router = routers.DefaultRouter()
router.register('todo', TodoViewSet, basename='todo')
router.register('achievements', AchievementsViewSet, basename='achievements')


custom_urlpatterns = [
    url(r'todo/(?P<todo_pk>\d+)/achievements$', TodoAchievements.as_view(),
        name='todo_achievements'),
    url(r'todo/(?P<todo_pk>\d+)/achievements/(?P<pk>\d+)$', SingleTodoAchievements.as_view(),
        name='single_todo_achievements')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
