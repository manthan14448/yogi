# Generated by Django 2.2.5 on 2020-02-07 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userimg', '0005_temp_cart_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_cart',
            name='qty',
            field=models.TextField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='temp_cart',
            name='p_id',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]
