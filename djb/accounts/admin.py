from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Account


class AccountCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all
    the required fields, plus a repeated password"""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two passwords match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AccountCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on 
    the user, but replaces the password field with admin's 
    password hash display field"""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'is_active', 
          'is_staff', 'is_admin', 'is_superuser')

    def clean_password(self):
        """Regardless of what the user provides, return the initial value.
        this is doen here, rather htan on the field, because the 
        field does not ahve access to the initial value"""
        return self.initial['password']


class AccountAdmin(UserAdmin):
    # The forms to add and change account instances
    form = AccountChangeForm
    add_form = AccountCreationForm

    # The fiesl to be used in displaying the Acocunt model
    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
      (None, {'fields': ('email', 'password')}),
      ('Personal Info', {'fields': ('first_name', 'last_name',)}),
      ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
      (None, {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new AccountAdmin
admin.site.register(Account, AccountAdmin)
# Unregister the Django Group model since we are not using it
admin.site.unregister(Group)

