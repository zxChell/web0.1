from django.db import models

# Create your models here.


class Tovar(models.Model):
    title = models.CharField(max_length=25)
    sell = models.IntegerField()

    def __str__(self):
        return self.title


