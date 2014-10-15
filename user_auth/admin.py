from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm
from user_auth.models import MyUser


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        else:
            return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = ('email', 'password', 'is_active', 'is_admin')


class MyUserAdmin(UserAdmin):
    form     = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin')
    list_filter  = ('is_admin', )
    fieldsets    = (
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_admin', 'perm')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1','password2',),}
        ),
    )

    search_fields     = ('email',)
    ordering          = ('email',)
    filter_horizontal = ()
    


admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)
