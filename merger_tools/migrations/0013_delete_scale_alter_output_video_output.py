# Generated by Django 4.0.3 on 2022-12-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0012_output_video'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Scale',
        ),
        migrations.AlterField(
            model_name='output_video',
            name='output',
            field=models.FileField(null=True, upload_to='output_video'),
        ),
    ]
