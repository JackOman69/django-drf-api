# Generated by Django 4.1.4 on 2022-12-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnesskit_task', '0005_alter_user_image_url_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_url',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]