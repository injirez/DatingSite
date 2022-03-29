import django_filters
from .models import Client

class UsersFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'gender']