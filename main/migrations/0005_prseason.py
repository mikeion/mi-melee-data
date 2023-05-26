# Generated by Django 4.2 on 2023-05-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_set_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='PRSeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('ranks', models.JSONField(default=list)),
                ('hm', models.JSONField(default=list)),
            ],
            options={
                'db_table': 'pr_seasons',
            },
        ),
    ]
