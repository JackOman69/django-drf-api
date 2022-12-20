# Generated by Django 4.1.4 on 2022-12-11 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnesskit_task', '0004_alter_user_image_url_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_url',
            field=models.URLField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]