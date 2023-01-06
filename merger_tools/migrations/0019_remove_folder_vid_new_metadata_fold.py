# Generated by Django 4.0.3 on 2023-01-04 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0018_folder_vid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='vid',
        ),
        migrations.AddField(
            model_name='new_metadata',
            name='fold',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='merger_tools.folder'),
        ),
    ]