from django.contrib import admin
from greeting.models import MyDb


class MyDbAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_display_links = ('email',)
    search_fields = ('email',)


admin.site.register(MyDb, MyDbAdmin)
