# Generated by Django 3.1.6 on 2021-03-06 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emsapp', '0009_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='emsapp.department'),
            preserve_default=False,
        ),
    ]
