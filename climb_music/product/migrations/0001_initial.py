# Generated by Django 2.2.12 on 2020-07-08 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sing', models.CharField(max_length=50, verbose_name='歌名')),
                ('singer', models.CharField(max_length=50, verbose_name='歌手')),
                ('issued_date', models.DateTimeField(verbose_name='发行日期')),
            ],
        ),
    ]
