# Generated by Django 3.2.12 on 2022-12-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0014_zip_file_delete_cut_merged_delete_cut_original'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='metadata')),
            ],
        ),
    ]
