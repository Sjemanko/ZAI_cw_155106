from django.contrib import admin

# Register your models here.
from django.contrib import admin
from filmy.models import Film


class FilmAdmin(admin.ModelAdmin):
    pass


admin.site.register(Film, FilmAdmin)
