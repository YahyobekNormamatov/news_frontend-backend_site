from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import apply

urlpatterns = [
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('community/', views.community, name='community'),
    path('team/<int:pk>/', views.team_detail, name='team_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('apply/', apply, name='apply'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


