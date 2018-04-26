
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class RegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    description = forms.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'description',

        )

    def save(self,commit = True):
        user=super(RegForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.description = self.cleaned_data['description']

        if commit:
            user.save()

            return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            #'description'    ##unable to change description
            'password',
        )

class FriendInviteForm(forms.Form):
    name = forms.CharField(label="Friend's Name")
    email = forms.EmailField(label="Friend's Email")
    




