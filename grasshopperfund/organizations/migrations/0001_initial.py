# Generated by Django 3.1.2 on 2020-12-01 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, default='campaign_default_pic.png', upload_to='organization_pics')),
                ('created', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
