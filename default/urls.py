from django.urls import path,include
from .views import *

urlpatterns = [
  path('',PollList.as_view()),
  path('<int:pk>/',PollDetail.as_view(), name='poll_view'),
  path('vote/<int:oid>/',PollVote.as_view()),
  path('create/',PollCreate.as_view()),
  path('<int:pk>/update/',PollUpdate.as_view()),
  path('<int:zzz>/create/',OptionCreate.as_view(), name='option_create'),
  path('option/<int:pk>/',OptionEdit.as_view(), name='option_edit'),
  path('option/<int:pk>/delete/', OptionDelete.as_view(), name='option_delete'),
  path('<int:pk>/delete/', PollDelete.as_view(),name='poll_delete')
]