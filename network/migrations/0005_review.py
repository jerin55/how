# Generated by Django 4.1.5 on 2023-03-03 03:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_user_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewz', models.CharField(blank=True, max_length=255, null=True)),
                ('mail', models.EmailField(blank=True, max_length=255, null=True)),
                ('rating', models.IntegerField(blank=True, max_length=255, null=True)),
                ('review_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewposst', to='network.post')),
                ('reviewer', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]