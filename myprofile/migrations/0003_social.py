# Generated by Django 2.2 on 2020-04-15 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_auto_20200415_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('url', models.URLField()),
            ],
        ),
    ]
