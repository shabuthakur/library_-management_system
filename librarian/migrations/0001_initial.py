# Generated by Django 4.1.1 on 2022-09-16 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('book_status', models.CharField(choices=[('BORROWED', 'BORROWED'), ('AVAILABLE', 'AVAILABLE')], max_length=80)),
            ],
        ),
    ]
