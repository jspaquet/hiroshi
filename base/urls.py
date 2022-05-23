from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r'bookmarks', views.BookmarkViewSet, basename='bookmarks')
router.register(r'users', views.UserViewSet, basename='users')
#
# app_name = 'base'

urlpatterns = [
    # path('settings/', views.settings, name='settings'),
    # path('about/', views.about, name='about'),
    # path('api/', include(router.urls)),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
]
