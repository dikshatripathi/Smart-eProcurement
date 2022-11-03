from django.contrib import admin
from .models.tender import Tender
from .models.T_category import Category
from .models.T_Status import Status
from .models.Press_Release import Press
from .models.Bidder import User
from .models.filetender import etender
from .models.administration import administrater

class AdminTender(admin.ModelAdmin):
    list_display = ['Subject','Reference_Number']

class AdminCategory(admin.ModelAdmin):
    list_display = ['Category_Name']

class AdminStatus(admin.ModelAdmin):
    list_display = ['Status']

class AdminPress(admin.ModelAdmin):
    list_display = ['Press_Release']

class AdminUser(admin.ModelAdmin):
    list_display = ['Name']

class AdminTenderfilled(admin.ModelAdmin):
    list_display = ['Biddername']

class Adminadministrater(admin.ModelAdmin):
    list_display = ['AName', 'AEmail', 'AMobile']

# Register your models here.
admin.site.register(Tender , AdminTender)
admin.site.register(Category, AdminCategory)
admin.site.register(Status, AdminStatus)
admin.site.register(Press, AdminPress)
admin.site.register(User, AdminUser)
admin.site.register(etender, AdminTenderfilled)
admin.site.register(administrater, Adminadministrater)

