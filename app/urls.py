from django.urls import path
from . import views as app_views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

app_name = 'app'

urlpatterns = [
    path('auth/register/',app_views.UserSignUpView.as_view(),name = 'signup'),
    path('auth/token/',TokenObtainPairView.as_view(),name = 'token'),
    path('auth/token/refresh/',TokenRefreshView.as_view(),name = 'token_refresh'),
]