# Generated by Django 4.0.3 on 2023-01-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0017_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='vid',
            field=models.FileField(null=True, upload_to='newVideo'),
        ),
    ]
