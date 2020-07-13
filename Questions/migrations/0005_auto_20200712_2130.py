# Generated by Django 3.0.4 on 2020-07-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0004_allclasses_classinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='questionandanswers',
            name='question',
        ),
    ]
