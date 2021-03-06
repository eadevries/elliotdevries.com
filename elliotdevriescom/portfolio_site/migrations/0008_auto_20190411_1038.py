# Generated by Django 2.1.5 on 2019-04-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_site', '0007_project_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='external_link_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
