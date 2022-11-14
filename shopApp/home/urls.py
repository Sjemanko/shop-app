from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("<int:pk>/", views.board_topics, name='board_topics'),
    path("<int:pk>/new/", views.new_topic, name='new_topic')
]
