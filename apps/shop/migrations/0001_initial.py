# Generated by Django 4.2.7 on 2024-01-02 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Price')),
                ('brand', models.CharField(max_length=255, verbose_name='Brand')),
                ('model', models.CharField(max_length=255, verbose_name='Model')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='user_default.jpeg', upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='shop.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product specification',
                'verbose_name_plural': 'Product specifications',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product', verbose_name='Product')),
            ],
        ),
    ]
