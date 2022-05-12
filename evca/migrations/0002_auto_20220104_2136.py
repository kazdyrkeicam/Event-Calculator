# Generated by Django 3.2.9 on 2022-01-04 20:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='debt',
        ),
        migrations.RemoveField(
            model_name='event',
            name='due',
        ),
        migrations.RemoveField(
            model_name='event',
            name='member',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 4, 20, 33, 58, 93586, tzinfo=utc), verbose_name='event date'),
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 1, 4, 20, 36, 22, 257214, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt', models.FloatField(default=0)),
                ('due', models.FloatField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evca.event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evca.member')),
            ],
        ),
    ]
