# Generated by Django 5.1.7 on 2025-06-18 00:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armoury', '0002_alter_product_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='describtion',
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 18, 0, 26, 44, 134215, tzinfo=datetime.timezone.utc), verbose_name='creation_date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='desc',
            field=models.TextField(default='trying to go home', verbose_name='describtion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 18, 0, 27, 34, 527789, tzinfo=datetime.timezone.utc), verbose_name='creation_date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(default='trying to go home', verbose_name='describtion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='armoury.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
