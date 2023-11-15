from django.contrib import admin
from mysite.models import Post,Product #匯入資料
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date')#管理時可看到
    

admin.site.register(Post,PostAdmin) #註冊
admin.site.register(Product)

