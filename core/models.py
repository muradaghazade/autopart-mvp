from django.db import models
from accounts.models import User
# from accounts.models import User , Request, Offer

class Make(models.Model):
    title = models.CharField('title',max_length=300, null=True)
    logo = models.ImageField('Image',upload_to='banners/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True )

    class Meta:
        verbose_name = 'Make' 

    def __str__(self):
        return f"{self.title}" 


class Model(models.Model):
    
    title = models.CharField('title',max_length=300, null=True)

    # make integer *> Make.id
    
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True )

    class Meta:
        verbose_name = 'Model' 

    def __str__(self):
        return f"{self.title}"

class Part(models.Model):
    title = models.CharField('title',max_length=300, null=True)
    category = models.IntegerField(null=True, blank=True, default=0)
    request = models.IntegerField(null=True, blank=True, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True )


    class Meta:
        verbose_name = 'Part' 

    def __str__(self):
        return f"{self.category}"


class Category(models.Model):
    title = models.CharField('title',max_length=300, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True )

    class Meta:
        verbose_name = 'Category' 

    def __str__(self):
        return f"{self.category}"


# account = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='posts', null=True, blank=True)
# Create your models here.

 
