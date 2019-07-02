from django.contrib import admin
from .models import *

# Register your models here.

admin.site.ste_header = '发现生活后台管理'
admin.site.site_title = '发现生活'
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Orders)
admin.site.register(Prodouct)
admin.site.register(Shop)
admin.site.register(SubCategory)
admin.site.register(Ticket)
admin.site.register(User)
