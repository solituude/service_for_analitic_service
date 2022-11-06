from django import forms

from scraping.models import City, Material, Conditions, Segment, HaveBalcony, CountRooms


class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  to_field_name='slug', required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Район')

    count_rooms = forms.ModelChoiceField(queryset=CountRooms.objects.all(),
                                     to_field_name='slug', required=False,
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label='Количество комнат')

    material = forms.ModelChoiceField(queryset=Material.objects.all(),
                                      to_field_name='slug', required=False,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Материал стен')

    conditions = forms.ModelChoiceField(queryset=Conditions.objects.all(),
                                        to_field_name='slug', required=False,
                                        widget=forms.Select(attrs={'class': 'form-control'}),
                                        label='Состояние квартиры')

    segment = forms.ModelChoiceField(queryset=Segment.objects.all(),
                                     to_field_name='slug', required=False,
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label='Сегмент')

    have_balcony = forms.ModelChoiceField(queryset=HaveBalcony.objects.all(),
                                          to_field_name='slug', required=False,
                                          widget=forms.Select(attrs={'class': 'form-control'}),
                                          label='Наличие балкона/лоджии')

