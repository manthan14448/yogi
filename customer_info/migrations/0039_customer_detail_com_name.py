# Generated by Django 2.2.5 on 2020-04-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0038_auto_20200426_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_detail',
            name='com_name',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='comapany name'),
        ),
    ]
