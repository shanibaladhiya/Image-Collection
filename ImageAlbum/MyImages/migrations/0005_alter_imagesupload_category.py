# Generated by Django 3.2.3 on 2021-07-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyImages', '0004_alter_imagesupload_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesupload',
            name='category',
            field=models.CharField(blank=True, choices=[('Nature', 'Nature'), ('Food', 'Food')], default='Nature', max_length=50),
        ),
    ]
