from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import model_utils

AGE_CATEGORIES = model_utils.Choices(
    (0, 'kids', 'kids'),
    (1, 'teens', 'teens'),
    (2, 'adults', 'adults'),
)


class Genre(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True
    )
    age_category = models.IntegerField(
        null=True,
        blank=True,
        choices=AGE_CATEGORIES
    )

    def __str__(self):
        return f'{self.name} ({self.get_age_category_display()})'


class Director(models.Model):
    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Country(models.Model):
    country = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        unique = True
    )

    class Meta:
        ordering = ['country',]

    def __str__(self):
        return f'{self.country}'


class Movie(models.Model):
    title = models.CharField(max_length=120)
    rating = models.IntegerField(
        null=True,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    released = models.DateField(null=True)
    description = models.TextField(
        null=True,
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL
    )
    director = models.ForeignKey(
        Director,
        null=True,
        on_delete=models.SET_NULL
    )
    countries = models.ManyToManyField(
        Country,
        related_name='Movies'
    )

    class Meta:
        unique_together = ('title', 'director', 'released')
        ordering = ['title']

    def __str__(self):
        return f'{self.title} from {self.released}'
