# Generated by Django 4.1.4 on 2022-12-10 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=128)),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=128)),
                ('name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=12)),
                ('image_url', models.URLField(default='', max_length=128)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_list', to='fitnesskit_task.sources')),
            ],
        ),
    ]
