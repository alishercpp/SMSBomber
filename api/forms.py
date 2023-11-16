from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class StudentCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "middle_name", "password1", "password2",)

class StudentChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "middle_name",)