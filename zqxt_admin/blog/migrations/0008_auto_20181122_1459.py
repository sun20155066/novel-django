# Generated by Django 2.1.3 on 2018-11-22 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181122_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='belong_to_user',
            new_name='user_id',
        ),
    ]