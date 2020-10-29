from django import forms
from django.contrib.auth.models import User

from . import models
from phonenumber_field.formfields import PhoneNumberField

class ProfileForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.EmailInput())
    confirm_email=forms.EmailField(widget=forms.EmailInput())
    phone_number = PhoneNumberField()

    class Meta:
        model = models.Profile
        fields = [
            'avatar',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'birth_date',
            'city',
            'country',
            'preferences',
            'cuisine',
            'diet'
        ]

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")


        if email != confirm_email:
            raise forms.ValidationError(
                "Emails must match!"
            )

