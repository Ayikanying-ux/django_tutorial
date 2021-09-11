from django.urls import path
from ajax_forms.views import UserSignUpView, ValidateUsername

urlpatterns = [
    path("", UserSignUpView.as_view(), name="signup"),
    path('ajax/validate-username/', ValidateUsername.as_view(), name='simple_ajax_validate'),
]