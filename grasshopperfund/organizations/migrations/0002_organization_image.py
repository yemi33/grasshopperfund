# Generated by Django 3.1.2 on 2020-11-06 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='image',
            field=models.ImageField(blank=True, default='campaign_default_pic.png', upload_to='organization_pics'),
        ),
    ]