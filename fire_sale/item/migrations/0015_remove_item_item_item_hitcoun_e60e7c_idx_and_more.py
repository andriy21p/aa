# Generated by Django 4.0.4 on 2022-05-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0014_item_item_item_show_in_33e0f4_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='item',
            name='item_item_hitcoun_e60e7c_idx',
        ),
        migrations.RemoveIndex(
            model_name='item',
            name='item_item_show_in_33e0f4_idx',
        ),
        migrations.AddIndex(
            model_name='item',
            index=models.Index(fields=['show_in_catalog', '-hitcount', 'name'], name='item_main_view_index'),
        ),
    ]
