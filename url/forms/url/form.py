from django.forms import ModelForm
from url.models import Url


class LinkForm(ModelForm):
    class Meta:
        model = Url
        fields = '__all__'
        labels = {'shortened': 'Short Code', 'url_link': 'Full URL'}
        error_messages = {
            'shortened': {
                'max_length': 'Code should be maximum 5 characters long',
            },
        }
