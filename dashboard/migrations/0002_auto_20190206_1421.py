# Generated by Django 2.1.5 on 2019-02-06 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datafile', models.FileField(upload_to='Others/')),
            ],
        ),
        migrations.RenameField(
            model_name='mobile',
            old_name='mobile',
            new_name='name',
        ),
        migrations.AddField(
            model_name='mobiledata',
            name='mobile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Mobile'),
        ),
    ]
