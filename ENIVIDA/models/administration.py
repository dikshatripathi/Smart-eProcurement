from django.db import models

class administrater(models.Model):

    AName = models.CharField(max_length=200,default=0)
    AUID = models.EmailField(max_length=200, default=0)
    AEmail = models.CharField(max_length=500,default=0)
    APassword = models.CharField(max_length=500,default=0)
    AMobile= models.IntegerField(default = 0)

    @staticmethod
    def get_user_by_email(AEmail):
        try:
            return User.objects.get(AEmail=AEmail)
        except:
            return False

    @staticmethod
    def isExists(AEmail):
        if administrater.objects.filter(AEmail=AEmail):
            return True
        else:
            return False