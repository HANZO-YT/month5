from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField()
    duration = models.IntegerField()
    is_hit = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
