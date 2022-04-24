# Generated by Django 3.2.9 on 2021-11-15 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0005_auto_20211115_1251'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(editable=False, max_length=222)),
                ('first_name', models.CharField(max_length=222)),
                ('last_name', models.CharField(max_length=222)),
                ('phone', models.CharField(max_length=222)),
                ('address', models.CharField(max_length=222)),
                ('city', models.CharField(max_length=222)),
                ('country', models.CharField(max_length=222)),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'Yangi'), ('Accepted', 'Qabul qilingan'), ('OnShipping', 'Yetkazib berishga'), ('Completed', 'Tugallangan'), ('Cancelled', 'Bekor qilingan')], default='New', max_length=15)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('amount', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'Yangi'), ('Accepted', 'Qabul qilingan'), ('Cancelled', 'Bekor qilingan')], max_length=222)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderbook.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
