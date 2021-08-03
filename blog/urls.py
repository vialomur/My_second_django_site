#BLOG
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'project_blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
