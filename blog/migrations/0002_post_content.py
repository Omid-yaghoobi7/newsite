# Generated by Django 4.2.11 on 2024-03-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(),
            preserve_default=False,
        ),
    ]