# Generated by Django 4.0.3 on 2023-01-05 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0019_remove_folder_vid_new_metadata_fold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zip_file',
            name='file',
            field=models.FileField(null=True, upload_to='zip'),
        ),
    ]