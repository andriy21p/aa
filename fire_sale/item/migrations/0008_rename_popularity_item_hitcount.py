# Generated by Django 4.0.4 on 2022-05-04 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_rename_hitcount_item_popularity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='popularity',
            new_name='hitcount',
        ),
    ]
