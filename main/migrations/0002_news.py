# Generated by Django 4.0.5 on 2022-07-06 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='image')),
                ('text', models.TextField(blank=True)),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
