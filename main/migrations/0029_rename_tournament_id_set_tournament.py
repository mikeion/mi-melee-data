# Generated by Django 4.2 on 2023-05-22 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_rename_tour_set_tournament_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='set',
            old_name='tournament_id',
            new_name='tournament',
        ),
    ]