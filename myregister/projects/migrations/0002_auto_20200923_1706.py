# Generated by Django 3.1.1 on 2020-09-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='flag',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='course',
            name='quota',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='term',
            field=models.IntegerField(),
        ),
    ]