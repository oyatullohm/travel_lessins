# Generated by Django 4.0.5 on 2022-07-06 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cantact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'yangilik', 'verbose_name_plural': 'yangiliklar'},
        ),
    ]
