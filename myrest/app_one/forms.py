from django import forms

from .models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs = {'class': 'form-control'}

        self.fields['title'].widget.attrs['class'] += ' redcolor'

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title == title.capitalize():
            raise forms.ValidationError('Must be start with upper case')
        return title

