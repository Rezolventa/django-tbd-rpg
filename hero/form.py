from django import forms

from hero.models import StorageRow


class HeroForm(forms.Form):  # DEPRECATED
    """
    Строит селекторы.
    Но из-за того, что мы не можем навесить доп. логику, стала не актуально.
    Пусть побудет пока тут, потом удалить.
    """
    attrs = {'class': 'form-control'}
    helm = forms.ChoiceField(widget=forms.Select(attrs=attrs))

    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options')
        super().__init__(*args, **kwargs)
        self.fields['helm'].choices = [(helm_name, helm_name) for helm_name in self.options['helms']['choices']]
        self.initial['helm'] = self.options['helms']['current']


class StorageRowForm(forms.Form):
    # TODO: widgets
    attrs = {'class': 'form-control'}
    item_image = forms.URLField()
    item_name = forms.CharField()
    count = forms.IntegerField()
    count_to_move = forms.IntegerField(initial=None)

    def __init__(self, instance: StorageRow, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_image'] = instance.item.image
        self.fields['item_name'] = instance.item.name
        self.fields['count'] = instance.count
