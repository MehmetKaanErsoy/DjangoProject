from stajodev.models import fakulteeekle, bolumekle, sorumlu_ekle
import django_filters


class Fakulte(django_filters.FilterSet):
    class Meta:
        model = fakulteeekle
        fields = ['fakulte_ismii', ]


class Bolum(django_filters.FilterSet):
    class Meta:
        model = bolumekle
        fields = ['Bolum_ismi', ]


class Sorumlu(django_filters.FilterSet):
    class Meta:
        model = sorumlu_ekle
        fields = ['adisoyadi', ]
