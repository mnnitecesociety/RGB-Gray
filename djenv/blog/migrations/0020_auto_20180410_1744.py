# Generated by Django 2.0.3 on 2018-04-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20180409_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='topbanner',
            field=models.FileField(blank=True, default='documents/03.jpg', null=True, upload_to='get_topbanner_filename'),
        ),
    ]
