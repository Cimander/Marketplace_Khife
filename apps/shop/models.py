from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from django_filters.rest_framework import DjangoFilterBackend
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user_default.jpeg', upload_to='profile_images')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    slug = models.SlugField(
        _('Slug'),
        max_length=100,
        unique=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    description = models.TextField(
        _('Description'),
    )
    price = models.PositiveIntegerField(
        _('Price'),
        default=0,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('Category'),
    )
    brand = models.CharField(
        _('Brand'),
        max_length=255,
    )
    model = models.CharField(
        _('Model'),
        max_length=255,
    )
    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=0,
    )
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'pk': self.pk})



class ProductSpecifications(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='specifications',
        verbose_name=_('Product'),
    )
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    value = models.CharField(
        _('Value'),
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product specification')
        verbose_name_plural = _('Product specifications')




class ProductImage(models.Model):
    image = models.ImageField(
        _('Image'),
        upload_to='products/',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Product'),
    )


