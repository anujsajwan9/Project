# Generated by Django 3.2.6 on 2021-09-08 07:20

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Glance_Skills_App', '0007_auto_20210903_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
        migrations.AddField(
            model_name='project',
            name='likes',
            field=models.ManyToManyField(related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='created_date',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 9, 8, 7, 20, 48, 327755, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='created_by',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 9, 8, 7, 20, 48, 329756, tzinfo=utc)),
        ),
    ]
