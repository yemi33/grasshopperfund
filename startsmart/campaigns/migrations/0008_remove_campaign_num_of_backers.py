# Generated by Django 3.1.2 on 2020-10-18 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0007_remove_campaign_current_money'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='num_of_backers',
        ),
    ]