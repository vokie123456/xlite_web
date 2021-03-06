# Generated by Django 2.0.3 on 2018-03-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('body', models.TextField(verbose_name='正文')),
                ('cover', models.CharField(blank=True, max_length=300, verbose_name='封面')),
                ('created_time', models.DateTimeField(verbose_name='时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
