from django.db import models

# Create your models here.
class Status(models.Model):
    Status = models.CharField(max_length=200)

    def __str__(self):
        return self.Status
