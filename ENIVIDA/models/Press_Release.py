from django.db import models

# Create your models here.
class Press(models.Model):
    Press_Release = models.CharField(max_length=200)

    @staticmethod
    def get_all_Press():
        return Press.objects.all()

    def __str__(self):
        return self.Press_Release

