# Generated by Django 4.2 on 2023-05-22 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_tournamentresults_options_set_player1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='region_code',
        ),
    ]