# Generated by Django 4.2 on 2023-05-22 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_prseason_table_prseasonresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prseason',
            name='hm',
        ),
        migrations.RemoveField(
            model_name='prseason',
            name='ranks',
        ),
    ]