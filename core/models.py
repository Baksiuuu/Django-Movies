from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

age_choices = (
    (7,7),
    (13,13),
    (16,16),
    (18,18)
)

class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(null = True, blank = True, choices=age_choices)

    def __str__(self):
        return f'{self.name} with age limit set on {self.age_limit}'

class Director(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Movie(models.Model):
    title = models.CharField(max_length = 120)
    rating = models.IntegerField(
        null=True, validators = [MaxValueValidator(10), MinValueValidator(1)]
    )

    released = models.DateField(null = True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null = True, on_delete = models.SET_NULL)
    director = models.ForeignKey(Director, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return f'{self.title} from {self.released}'
