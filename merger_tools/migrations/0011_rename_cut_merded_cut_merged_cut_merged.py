# Generated by Django 4.0.3 on 2022-12-16 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merger_tools', '0010_remove_cut_original_v_cut_original_cut_original'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cut_merged',
            old_name='cut_merded',
            new_name='cut_merged',
        ),
    ]
