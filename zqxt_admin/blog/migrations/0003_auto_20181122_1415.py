# Generated by Django 2.1.3 on 2018-11-22 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='belong_to_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='blog.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=256, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=128, unique=True),
        ),
    ]
