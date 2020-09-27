from django.urls import path

from accounts.views import SubmittablePasswordChangeView, SuccessMessagedLogoutView, \
    SubmittableLoginView, SignUpView

app_name = 'accounts'
urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', SuccessMessagedLogoutView.as_view(), name='logout'),
    path('passwordchange/', SubmittablePasswordChangeView.as_view(), name='password_change'),
    path('register/', SignUpView.as_view(), name='register_user'),
]