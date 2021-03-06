# Generated by Django 2.1.5 on 2019-04-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_site', '0002_auto_20190116_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blurb', models.TextField(blank=True)),
                ('icon', models.CharField(choices=[('PAPER_AIRPLANE', 'Paper Airplane'), ('SQUARE_ROOT', 'Square Root')], max_length=50)),
                ('full_description', models.TextField()),
            ],
        ),
    ]
