# Generated by Django 4.2 on 2023-05-22 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_rename_tour_id_tournament_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournamentresults',
            old_name='tour',
            new_name='tournament_id',
        ),
        migrations.AlterUniqueTogether(
            name='tournamentresults',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='tournamentresults',
            name='player_id',
            field=models.ForeignKey(db_column='player_id', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main.player'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='tournamentresults',
            unique_together={('tournament_id', 'player_id')},
        ),
        migrations.RemoveField(
            model_name='tournamentresults',
            name='playerid',
        ),
    ]
