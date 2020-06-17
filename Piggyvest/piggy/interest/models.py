from django.db import models


class Info(models.Model):
    principle = models.FloatField(max_length=2)
    addition = models.FloatField(max_length=2)
    rate = models.FloatField(max_length=2)
    time = models.FloatField(max_length=2)

    def __str__(self):
        return self.principle
