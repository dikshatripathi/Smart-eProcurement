from django.db import models
from .T_category import Category
from .T_Status import Status

# Create your models here.
class Tender(models.Model):
    Subject = models.CharField(max_length=200, default=0)
    Reference_Number = models.IntegerField(default=0)
    Identification_No = models.IntegerField(default=0)
    Budget = models.IntegerField(default=0)
    Time_Duration = models.IntegerField(default=0)
    EMD = models.IntegerField(default=0)
    Eligible_Class = models.CharField(max_length=200, default=0)

    @staticmethod
    def get_all_Tender():
        return Tender.objects.all()
