# Generated by Django 4.1.3 on 2022-11-28 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appuser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='username',
        ),
        migrations.AddField(
            model_name='appuser',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='last_logged_in_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]