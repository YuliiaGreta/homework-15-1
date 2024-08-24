# Generated by Django 5.0.7 on 2024-08-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_publisher_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='location',
        ),
        migrations.AddField(
            model_name='library',
            name='address',
            field=models.CharField(default='Unknown Address', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='library',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
