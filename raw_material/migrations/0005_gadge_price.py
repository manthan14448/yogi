# Generated by Django 2.2.5 on 2020-01-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_material', '0004_auto_20200121_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='gadge',
            name='price',
            field=models.IntegerField(default=50, max_length=10),
            preserve_default=False,
        ),
    ]