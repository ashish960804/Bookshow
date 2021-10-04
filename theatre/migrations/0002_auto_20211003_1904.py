# Generated by Django 3.2.7 on 2021-10-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='totaldays',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='show',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='screen',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='show',
            name='time',
            field=models.TimeField(choices=[('09:30:00', '09:30:00'), ('12:00:00', '12:00:00'), ('15:30:00', '15:30:00'), ('18:00:00', '18:00:00'), ('21:30:00', '21:30:00')]),
        ),
    ]
