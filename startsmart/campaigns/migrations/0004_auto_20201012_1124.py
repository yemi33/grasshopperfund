# Generated by Django 3.1.2 on 2020-10-12 18:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaigns', '0003_auto_20201012_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='user',
            new_name='creator',
        ),
        migrations.AlterUniqueTogether(
            name='campaign',
            unique_together={('creator', 'title')},
        ),
    ]
