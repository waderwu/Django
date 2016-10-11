from django.contrib import admin
from login.models import User

# Register your models here.


class USerAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(User,USerAdmin)