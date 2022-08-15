# Generated by Django 3.2.6 on 2022-08-13 08:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Glance_Skills_App', '0030_auto_20220813_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcategory',
            name='created_date',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 8, 13, 8, 0, 21, 360330, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='created_by',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 8, 13, 8, 0, 21, 365244, tzinfo=utc), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Glance_Skills_App.project'),
        ),
    ]
