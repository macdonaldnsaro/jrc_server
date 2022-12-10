from django import forms
from django.core.exceptions import ValidationError

from jrc_server.settings import ALLOWED_SIGNUP_DOMAINS
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
User = get_user_model()


def SignupDomainValidator(value):
    if '*' not in ALLOWED_SIGNUP_DOMAINS:
        try:
            domain = value[value.index("@"):]
            if domain not in ALLOWED_SIGNUP_DOMAINS:
                raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501

        except Exception:
            raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501


def ForbiddenUsernamesValidator(value):
    forbidden_usernames = [
        'admin', 'settings', 'news', 'about', 'help', 'signin', 'signup', 'signout', 'terms', 'privacy', 'cookie',
        'new', 'login', 'logout', 'administrator', 'join', 'account', 'username', 'root', 'blog', 'user', 'users', 
        'billing', 'subscribe', 'reviews', 'review', 'blog', 'blogs', 'edit', 'mail', 'email', 'home', 'job', 'jobs', 
        'contribute', 'newsletter', 'shop', 'profile', 'register', 'auth', 'authentication', 'campaign', 'config', 'delete', 
        'remove', 'forum', 'forums', 'download', 'downloads', 'contact', 'blogs', 'feed', 'feeds', 'faq', 'intranet', 'log', 
        'registration', 'search', 'explore', 'rss', 'support', 'status', 'static', 'media', 'setting', 'css', 'js', 'follow', 
        'activity', 'questions', 'articles', 'network','celebtiry','pornstar' ]

    if value.lower() in forbidden_usernames:
        raise ValidationError('This is a reserved word.')


def InvalidUsernameValidator(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('Enter a valid username.')


def UniqueEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


def UniqueUsernameIgnoreCaseValidator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this Username already exists.')


from django import forms
from django.contrib.auth.forms import UserCreationForm
CHOICES=GENDER_TYPES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Non Binary'),
    )
class SignupForm(UserCreationForm):
    # remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    firstname = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password1 = forms.CharField( widget=forms.TextInput(attrs={'type':'password','placeholder': 'password'}))
    password2 = forms.CharField( widget=forms.TextInput(attrs={'type':'password','placeholder': 'Retype password'}))
    date_of_birth = forms.CharField( widget=forms.TextInput(attrs={'type':'date','placeholder': 'Retype password'}))
    # gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    class Meta:
        model = User
        fields = ('firstname','lastname','username', 'email', 'password1', 'password2','date_of_birth')
    def __init__(self, *args, **kwargs):
        # if not self.cleaned_data.get('remember_me'):
        #   self.request.session.set_expiry(0)
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        self.fields['username'].validators.append(InvalidUsernameValidator)
        self.fields['username'].validators.append(UniqueUsernameIgnoreCaseValidator)
        self.fields['email'].validators.append(UniqueEmailValidator)
        self.fields['email'].validators.append(SignupDomainValidator)
        print (args ,kwargs ) 

    def clean(self):
        super(SignupForm, self).clean()
        password = self.cleaned_data.get('password1')
        confirm_password = self.cleaned_data.get('password2')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(
                ['Passwords don\'t match'])
        return self.cleaned_data

