# Generated by Django 4.0.3 on 2022-12-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0007_cut_original'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cut_Merged',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cut_merded', models.FileField(null=True, upload_to='cut_merged')),
            ],
        ),
        migrations.RemoveField(
            model_name='cut_original',
            name='cut_merded',
        ),
        migrations.AddField(
            model_name='cut_original',
            name='cut_original',
            field=models.FileField(null=True, upload_to='cut_original'),
        ),
    ]
