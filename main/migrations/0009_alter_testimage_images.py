# Generated by Django 4.0.2 on 2022-04-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_testimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimage',
            name='images',
            field=models.ImageField(upload_to='orpage/test'),
        ),
    ]
