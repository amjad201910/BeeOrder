# Generated by Django 4.1.6 on 2023-02-20 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import restaurant.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurnat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to=restaurant.models.upload_path)),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=42)),
                ('Restaurnat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurnat')),
            ],
        ),
    ]
