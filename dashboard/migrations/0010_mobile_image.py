# Generated by Django 2.1.5 on 2019-03-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_mobilereviews_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='image',
            field=models.ImageField(null=True, upload_to='mobiles/'),
        ),
    ]
