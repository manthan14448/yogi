# Generated by Django 2.2.5 on 2020-02-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0011_auto_20200214_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_detail',
            name='p_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
