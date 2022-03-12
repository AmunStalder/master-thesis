from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    #Use meta class to define which fields will be used
    class Meta():
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Make a new Label for the username
        self.fields['username'].label = 'Username'
        #Make a new Label for the mail address
        self.fields['email'].label = 'E-mail address'
