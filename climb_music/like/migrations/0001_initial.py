# Generated by Django 2.2.12 on 2020-07-06 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sing', models.CharField(max_length=128, verbose_name='歌名')),
                ('singer', models.CharField(max_length=50, verbose_name='歌手')),
                ('status', models.IntegerField(default='已收藏', verbose_name='收藏')),
                ('user_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
            ],
            options={
                'db_table': 'user_likes',
            },
        ),
    ]