# Generated by Django 2.2.5 on 2020-04-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0035_auto_20200413_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquery_order',
            name='a_status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
