# Generated by Django 2.2.4 on 2019-10-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blend',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blend',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
