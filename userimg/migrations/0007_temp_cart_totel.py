# Generated by Django 2.2.5 on 2020-02-07 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userimg', '0006_auto_20200207_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_cart',
            name='Totel',
            field=models.FloatField(blank=True, null=True),
        ),
    ]