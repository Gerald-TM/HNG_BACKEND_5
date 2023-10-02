from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_video_chunk, name='upload_video_chunk'),
    path('list/', views.VideoList.as_view(), name='video-rec-list')
    # path('transcribe/', views.transcribe_video, name='transcribe-video'),
]