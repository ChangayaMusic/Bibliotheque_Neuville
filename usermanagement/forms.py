from django import forms
from usermanagement.models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('nom', 'prenom', 'telephone', 'adresse')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the 'username' field if it exists
        if 'username' in self.fields:
            del self.fields['username']
        # Remove the 'password' fields if they exist
        if 'password1' in self.fields:
            del self.fields['password1']
        if 'password2' in self.fields:
            del self.fields['password2']
