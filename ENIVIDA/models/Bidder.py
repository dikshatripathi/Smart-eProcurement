from django.db import models

# Create your models here.
class User(models.Model):

    Name = models.CharField(max_length=200,default=0)
    Email = models.EmailField(max_length=200, default=0)

    Bidder_Mobile = models.CharField(max_length=500,default=0)
    Password = models.CharField(max_length=500,default=0)
    Company_Name = models.CharField(max_length=500,default=0)
    Registration_Number = models.CharField(max_length=500,default=0)
    Registered_Address = models.CharField(max_length=1000,default=0)
    Partners_or_Directors = models.CharField(max_length=500,default=0)
    City = models.CharField(max_length=500,default=0)
    State = models.CharField(max_length=500,default=0)
    Postal_Code = models.IntegerField(default=000)
    PAN_TAN_Number = models.CharField(max_length=500,default=0)
    Estd_Year = models.IntegerField(default=2022)
    Nature_of_Business = models.CharField(max_length=500,default=0)
    Legel_Status = models.CharField(max_length=500,default=0)

    @staticmethod
    def get_user_by_email(Email):
        try:
            return User.objects.get(Email = Email)
        except:
            return False

    @staticmethod
    def isExists(Email):
        if User.objects.filter(Email = Email):
            return True
        else:
            return False
