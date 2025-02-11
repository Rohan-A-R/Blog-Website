from django.contrib import admin
from . models import Category,Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('title',)}
    list_display=('title','category','author','status','is_fetured')
    search_fields=('id','title','category__Category_name','status')
    list_editable=('is_fetured','status')
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
