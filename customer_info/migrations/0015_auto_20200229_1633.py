# Generated by Django 2.2.5 on 2020-02-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0014_auto_20200229_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquery_order',
            name='a_Description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inquery_order',
            name='a_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inquery_order',
            name='c_Description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inquery_order',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]
