# Generated by Django 4.1.6 on 2023-02-20 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_restaurnat_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurnat',
            name='Address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='restaurnat',
            name='Name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
