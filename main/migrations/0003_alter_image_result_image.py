# Generated by Django 4.0.2 on 2022-04-15 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_image_result_image_alter_image_source_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='result_image',
            field=models.ImageField(blank=True, null=True, upload_to='files/result'),
        ),
    ]