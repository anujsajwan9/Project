# Generated by Django 3.2.6 on 2022-04-10 07:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Glance_Skills_App', '0019_auto_20211006_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcategory',
            name='created_date',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 4, 10, 7, 29, 47, 625704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='created_by',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 4, 10, 7, 29, 47, 625704, tzinfo=utc), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Glance_Skills_App.project'),
        ),
    ]