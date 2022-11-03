from django.db import models

class etender(models.Model):

    Biddername = models.CharField(max_length=200,default = 0)
    Bid_ID = models.CharField(max_length=200,default = 0)
    Bid_Type = models.CharField(max_length=200,default = 0)
    Bid_Category = models.CharField(max_length=200,default = 0)
    Total_Projects_Worked = models.IntegerField(default=0)
    Total_Success_Projects = models.IntegerField(default=0)
    Org_size = models.IntegerField(default=0)
    Org_est = models.IntegerField(default=0)
    Value_of_Last_Project = models.IntegerField(default=0)

    Proposed_Cost_of_Project = models.IntegerField(default=0)

