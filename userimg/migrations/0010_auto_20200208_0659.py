# Generated by Django 2.2.5 on 2020-02-08 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userimg', '0009_auto_20200207_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_img',
            name='c_img',
            field=models.ImageField(blank=True, null=True, upload_to='user_pics'),
        ),
    ]
