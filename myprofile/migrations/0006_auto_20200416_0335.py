# Generated by Django 2.2 on 2020-04-16 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0005_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default=''),
        ),
    ]