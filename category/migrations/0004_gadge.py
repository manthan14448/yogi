# Generated by Django 2.2.5 on 2020-01-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20200112_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='gadge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gadge', models.TextField(max_length=3)),
            ],
        ),
    ]