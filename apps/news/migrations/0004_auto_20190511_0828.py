# Generated by Django 2.0.5 on 2019-05-11 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190508_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField()),
                ('image_url', models.URLField()),
                ('link_to', models.URLField()),
                ('pub_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-priority'],
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pub_time']},
        ),
    ]