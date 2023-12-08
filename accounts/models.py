from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.common import slugify

class User(AbstractUser):
    full_name = models.CharField('full_name',max_length=300, null=True)
    email = models.CharField('email',max_length=300, null=True)
    number = models.IntegerField(null=True, blank=True, default=0)
    password = models.CharField('password',max_length=300, null=True)
    is_store = models.BooleanField(default=True)
    description = models.CharField('description',max_length=300, null=True)
    adress = models.CharField('adress',max_length=300, null=True)
    map_link = models.CharField('map_link',max_length=300, null=True)
    image = models.ImageField('Image',upload_to='banners/', null=True, blank=True)
    makes = models.CharField('makes',max_length=300, null=True)
    

    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.username)}'
        super(User, self).save(*args, **kwargs)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User' 
        verbose_name_plural = 'Users'



class Request(models.Model):
    model = models.CharField('model',max_length=300, null=True)
    user  = models.CharField('user',max_length=300, null=True)
    year  = models.IntegerField(null=True, blank=True, default=0)
    body_type = models.CharField('body_type',max_length=300, null=True)
    color = models.CharField('color',max_length=300, null=True)
    transmission = models.CharField('transmission',max_length=300, null=True)
    engine = models.CharField('engine',max_length=300, null=True)
    country = models.CharField('country',max_length=300, null=True)
    
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Request' 
        verbose_name_plural = 'Requests'


class Offer(models.Model):

    
    color = models.CharField('color',max_length=300, null=True)
    price = models.DecimalField('Price',max_digits=6, decimal_places=2)
    condition = models.CharField('condition',max_length=300, null=True)

    
    makes = models.CharField('makes',max_length=300, null=True)
    

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'
# Create your models here.
