# Generated by Django 2.2.5 on 2020-04-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0033_delivery_d_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='d_status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
