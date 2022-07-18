# Generated by Django 3.2.6 on 2022-07-18 12:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Glance_Skills_App', '0022_auto_20220718_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='image',
            field=models.ImageField(default='defaultuser.jpeg', null=True, upload_to='images/user_images/'),
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='created_date',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 7, 18, 12, 30, 39, 928945, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='created_by',
            field=models.DateTimeField(auto_created=datetime.datetime(2022, 7, 18, 12, 30, 39, 930468, tzinfo=utc), auto_now_add=True),
        ),
    ]
