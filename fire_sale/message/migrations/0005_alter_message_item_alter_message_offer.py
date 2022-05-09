# Generated by Django 4.0.4 on 2022-05-09 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0018_alter_item_has_accepted_offer'),
        ('message', '0004_message_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.item'),
        ),
        migrations.AlterField(
            model_name='message',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.offer'),
        ),
    ]
