from django.db.models import Q
from django_filters import FilterSet
from .models import Hero
import django_filters

class heroFilter(FilterSet):
    class Meta:
        model = Hero
        fields = "__all__"
        exclude = ['image','name',]

    # class roleFilter(django_filters.FilterSet):
    #     q = django_filters.CharFilter(method='my_custom_filter')
    #
    #     class Meta:
    #         model = Hero
    #         fields = ['q']
    #
    #     def my_custom_filter(self,queryset,role,value):
    #         return Hero.objects.filter(
    #             Q(role_icontains=value),Q(role_carry_icontains=value),
    #             Q(role_mid_icontains=value),Q(role_offlaner_icontains=value),
    #             Q(role_soft_support_icontains=value),Q(role_hard_support_icontains=value),
    #         )
