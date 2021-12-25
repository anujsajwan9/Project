# Generated by Django 3.2.6 on 2021-09-03 10:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Glance_Skills_App', '0005_auto_20210902_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcategory',
            name='created_date',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 9, 3, 10, 44, 0, 406006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='images/project_images/'),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='created_by',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 9, 3, 10, 44, 0, 406006, tzinfo=utc)),
        ),
    ]