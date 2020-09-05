from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length = 120)
    rating = models.IntegerField(
        null=True, validators = [MaxValueValidator(10), MinValueValidator(1)]
    )

    relased = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} from {self.relased}'
