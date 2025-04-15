from django.contrib import admin
from .models import Book
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
  list_filter = ('title', 'author', 'publication_year')
  search_fields = ('title', 'author')

class CustomUserAdmin(admin.ModelAdmin):
  list_filter = ('email', 'password', 'date_of_birth', 'profile_photo')
  search_fields = ('email', 'date_of_birth')

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)