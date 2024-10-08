# Generated by Django 5.0.7 on 2024-08-04 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='libraries',
        ),
        migrations.RemoveField(
            model_name='book',
            name='page_count',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publishing_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='library',
            name='site',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='address',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='city',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='country',
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ForeignKey(default=2000, on_delete=django.db.models.deletion.CASCADE, to='library.library'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='year_published',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=2000, on_delete=django.db.models.deletion.CASCADE, to='library.author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=2000, on_delete=django.db.models.deletion.CASCADE, to='library.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.publisher'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='library',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='library',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='library',
            name='country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
