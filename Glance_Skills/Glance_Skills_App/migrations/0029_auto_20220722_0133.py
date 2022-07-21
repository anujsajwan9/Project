# Generated by Django 3.2.6 on 2022-07-21 20:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Glance_Skills_App', '0028_auto_20220722_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_commentsreply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='Glance_Skills_App.projects_comment'),
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='created_date',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 7, 21, 20, 3, 15, 895775, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='created_by',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 7, 21, 20, 3, 15, 897768, tzinfo=utc), auto_now_add=True),
        ),
    ]
