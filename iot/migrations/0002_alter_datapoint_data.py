# Generated by Django 5.0.6 on 2024-05-20 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='data',
            field=models.TextField(),
        ),
    ]