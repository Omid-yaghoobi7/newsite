# Generated by Django 4.2.11 on 2024-04-08 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approve',
            new_name='approved',
        ),
    ]
