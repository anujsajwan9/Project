# Generated by Django 3.2.6 on 2021-10-06 03:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Glance_Skills_App', '0017_auto_20211006_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcategory',
            name='created_date',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 10, 6, 3, 24, 23, 196283, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='created_by',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 10, 6, 3, 24, 23, 196283, tzinfo=utc), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='projects_comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]