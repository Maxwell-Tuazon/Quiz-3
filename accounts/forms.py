from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@objor.com'):
            raise forms.ValidationError('Email must be @objor.com')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already taken')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken')
        return username

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone and CustomUser.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError('Phone number already taken')
        return phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data