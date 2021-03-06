# Generated by Django 2.2.7 on 2019-12-02 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsite', '0002_couponcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='blogs')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Blogs',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='NewsLetters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Newsletters',
                'verbose_name_plural': 'NewsLetters',
            },
        ),
    ]
