# Generated by Django 3.2.10 on 2022-03-28 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_comment_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='avatar',
            new_name='avatarop',
        ),
    ]
