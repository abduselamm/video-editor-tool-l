# Generated by Django 4.0.3 on 2022-12-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0011_rename_cut_merded_cut_merged_cut_merged'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output', models.FileField(null=True, upload_to='output')),
            ],
        ),
    ]
