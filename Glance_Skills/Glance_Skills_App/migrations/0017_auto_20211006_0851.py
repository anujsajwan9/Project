# Generated by Django 3.2.6 on 2021-10-06 03:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Glance_Skills_App', '0016_auto_20211006_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcategory',
            name='created_date',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 10, 6, 3, 21, 48, 632445, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='created_by',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 10, 6, 3, 21, 48, 634446, tzinfo=utc), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Glance_Skills_App.project'),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='updated_by',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
