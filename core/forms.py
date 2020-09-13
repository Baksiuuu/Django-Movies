import re
from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from core.models import Genre, Director, Country, Movie


def capitalized_validator(value: str):
    if value[0].islower():
        raise ValidationError('Value must be capitalized')


class PastMonthField(forms.DateField):
    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    title = forms.CharField(validators=[capitalized_validator])
    rating = forms.IntegerField(min_value=1, max_value=10)
    released = PastMonthField()

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        cleaned = '. '.join(sentence.capitalize() for sentence in sentences)
        return cleaned

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'Comedy' and result['rating'] >= 5:
            raise ValidationError('The best comedy is worth a 4.')
        return result