# Generated by Django 3.1.7 on 2021-04-01 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0002_auto_20210401_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_artist',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_duration',
            field=models.DurationField(default=''),
        ),
    ]