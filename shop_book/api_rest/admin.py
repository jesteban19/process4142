from django.contrib import admin
from api_rest.models import Book,Author
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	pass

@admin.register(Author)
class Authordmin(admin.ModelAdmin):
	pass
