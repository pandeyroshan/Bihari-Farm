# Generated by Django 2.2.7 on 2019-12-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsite', '0009_remove_couponcode_validity'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponcode',
            name='discount',
            field=models.IntegerField(default=12, verbose_name='Discount'),
            preserve_default=False,
        ),
    ]
