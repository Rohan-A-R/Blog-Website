from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    Category_name=models.CharField(max_length=50,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)


    class Meta:
        verbose_name_plural='categories'

    def __str__(self):
        return self.Category_name
STATUS_CHOICES=(
    ("Draft","Draft"),
    ("Published","Published")
)
    

class Blog(models.Model):
   title=models.CharField(max_length=100)
   slug=models.SlugField(max_length=150,unique=True,blank=True)
   category= models.ForeignKey(Category,on_delete=models.CASCADE)
   author=models.ForeignKey(User,on_delete=models.CASCADE)
   featured_image=models.ImageField(upload_to='uploads/%Y/%m/%d')
   short_description=models.TextField(max_length=500)
   blog_body=models.TextField(max_length=2000)
   status=models.CharField(max_length=20, choices=STATUS_CHOICES,default="Draft")
   is_fetured=models.BooleanField(default=False)
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now=True)

   def  __str__(self):
       return self.title
   

class About(models.Model):
    about_heading=models.CharField(max_length=25)
    about_description=models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='About'

    def __str__(self):
        return self.about_heading
    

class Links(models.Model):
    platform=models.CharField(max_length=25)
    link=models.URLField(max_length=100,default="https://example.com")
    def __str__(self):
        return self.platform
    
    class Meta:
        verbose_name_plural='link'

