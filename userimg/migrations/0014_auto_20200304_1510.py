# Generated by Django 2.2.5 on 2020-03-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userimg', '0013_auto_20200304_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oid_qr',
            name='o_id',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
