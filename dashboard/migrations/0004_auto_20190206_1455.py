# Generated by Django 2.1.5 on 2019-02-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20190206_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
