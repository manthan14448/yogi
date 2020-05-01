# Generated by Django 2.2.5 on 2020-03-04 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0027_auto_20200303_1253'),
        ('userimg', '0011_temp_cart_p_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_img',
            name='img_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer_info.customer_detail'),
        ),
        migrations.CreateModel(
            name='oid_qr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr', models.ImageField(upload_to='qrcode')),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_info.order_detail')),
            ],
        ),
    ]