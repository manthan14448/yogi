# Generated by Django 2.2.5 on 2020-03-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0018_auto_20200301_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquery_order',
            name='i_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
