# Generated by Django 4.0.3 on 2022-04-07 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('can_add_new_project', 'can add new project')]},
        ),
    ]
