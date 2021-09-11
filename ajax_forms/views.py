from django.views.generic.base import View
from ajax_forms.forms import CreateUser
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic.edit import CreateView

# Create your views here.
class UserSignUpView(CreateView):
    form_class = CreateUser
    template_name = "signup.html"


class ValidateUsername(View):
    def get(self, request):
        username = request.GET.get('username', None)

        data = {
            'is_present':
            User.objects.filter(username_iexact=username).exists()
        }
        return JsonResponse(data)