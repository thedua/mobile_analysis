# Generated by Django 2.1.5 on 2019-04-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_mobile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='company',
            field=models.CharField(choices=[('Xiaomi', 'Xiaomi'), ('Samsumg', 'Samsumg'), ('Asus', 'Asus'), ('Honor', 'Honor'), ('Moto', 'Moto'), ('Nokia', 'Nokia'), ('Realme', 'Realme'), ('Oneplus', 'Oneplus'), ('LG', 'LG'), ('Oppo', 'Oppo'), ('Huawei', 'Huawei')], default=None, max_length=30),
        ),
    ]
