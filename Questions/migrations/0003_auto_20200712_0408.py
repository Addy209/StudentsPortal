# Generated by Django 3.0.4 on 2020-07-11 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0002_auto_20200712_0357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classinfo',
            name='classname',
        ),
        migrations.RemoveField(
            model_name='classinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='AllClasses',
        ),
        migrations.DeleteModel(
            name='ClassInfo',
        ),
    ]
