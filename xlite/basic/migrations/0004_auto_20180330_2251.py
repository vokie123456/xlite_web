# Generated by Django 2.0.3 on 2018-03-30 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20180330_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]