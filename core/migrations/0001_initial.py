# Generated by Django 3.2.5 on 2021-08-25 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('number', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=500)),
                ('entity', models.CharField(default='', max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('id', models.IntegerField(default=1)),
                ('content', models.TextField()),
                ('main_title', models.CharField(default='', max_length=500)),
                ('sub_title', models.CharField(default='', max_length=500)),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='UrlData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=500)),
                ('entity', models.CharField(default='', max_length=50)),
                ('title', models.CharField(max_length=500)),
                ('id', models.IntegerField(default=1)),
                ('content', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.chapter')),
            ],
            options={
                'ordering': ('number',),
            },
        ),
    ]
