import django_filters

from .models import Films


class FilmFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Films
        fields = ('name', )