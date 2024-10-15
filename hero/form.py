from django import forms


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
