from django.urls import path,include
from . import views

urlpatterns = [
  path('poll/',views.PollList.as_view()),
  path('poll/<int:pk>/',views.PollDetail.as_view())
]