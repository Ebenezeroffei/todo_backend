from django.urls import path
from . import views as app_views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'app'
API = 'api/v1/'
AUTH = 'auth/'

urlpatterns = [
    path(AUTH+'register/',app_views.UserSignUpView.as_view(),name = 'signup'),
    path(AUTH+'login/',app_views.UserSignInView.as_view(),name = 'signin'),
    path(AUTH+'token/refresh/',TokenRefreshView.as_view(),name = 'token_refresh'),
]