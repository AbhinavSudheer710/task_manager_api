import django_filters
from .models import Tasks


class TasksFilter(django_filters.FilterSet):
    status = django_filters.BooleanFilter(field_name='status')
    difficulty = django_filters.NumberFilter(field_name='difficulty')
    tag = django_filters.CharFilter(field_name='tags__name', lookup_expr='iexact')

    class Meta:
        model = Tasks
        fields = ['status', 'difficulty', 'tag']