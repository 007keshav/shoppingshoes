# Generated by Django 3.2.9 on 2021-11-20 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='user',
        ),
        migrations.DeleteModel(
            name='cart',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='OrderPlaced',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
