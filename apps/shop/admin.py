from django.contrib import admin

from .models import Profile, Product,Category, Product, ProductSpecifications, ProductImage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user'
    )
    list_display_links = (
        'user',
        'id'
    )
    list_filter = (
        'user',
        'id'
    )
    search_fields = (
        'user',
        'id'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
class ProductSpecificationsInline(admin.TabularInline):
    model = ProductSpecifications
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'brand', 'model', 'quantity')
    list_filter = ('category', 'brand', 'model')
    search_fields = ('name', 'brand', 'model')
    inlines = [ProductSpecificationsInline, ProductImageInline]

    #def image_show(self, obj):
    #    if obj.image:
    #        return mark_safe("<img src='{}' width='60' />".format((obj.image.url)))
    #    return 'None'
    #image_show.__name__ = "Картинка"






@admin.register(ProductSpecifications)
class ProductSpecificationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'product')
    list_filter = ('product',)
    search_fields = ('name', 'value')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product')
    list_filter = ('product',)
