# Generated by Django 4.2.5 on 2023-09-20 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('subforum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.subforum')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('subforum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.company_subforum')),
            ],
        ),
    ]
