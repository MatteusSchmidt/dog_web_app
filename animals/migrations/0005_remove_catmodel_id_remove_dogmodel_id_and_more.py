# Generated by Django 4.2.7 on 2023-12-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_alter_catmodel_left_alter_catmodel_stars_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catmodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='dogmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='catmodel',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dogmodel',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
