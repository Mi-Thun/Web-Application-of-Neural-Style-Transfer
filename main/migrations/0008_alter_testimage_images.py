# Generated by Django 4.0.2 on 2022-04-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_testimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimage',
            name='images',
            field=models.ImageField(upload_to='test'),
        ),
    ]
