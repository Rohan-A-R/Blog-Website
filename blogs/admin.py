from django.contrib import admin
from . models import Category,Blog,About, Links,Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('title',)}
    list_display=('title','category','author','status','is_fetured')
    search_fields=('id','title','category__Category_name','status')
    list_editable=('is_fetured','status')
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self,request):
        count=About.objects.all().count()
        if count ==0:
            return True
        return False
admin.site.register(About,AboutAdmin)

admin.site.register(Links)
