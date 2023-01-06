
from . import views
from django.urls import path


urlpatterns = [
    
    path("", views.home, name = 'home'),
    path("video_merger_tools", views.index, name = 'video_merger_tools'),
    path('preview', views.preview, name='preview'),
    path('templates', views.templates, name='templates'),
    path('output', views.output, name='output'),
    path('metadata_chengar', views.metadata, name='metadata_changer'),
    path('metadata_changed_video', views.meta_output, name='metadata_changed_video')
]
