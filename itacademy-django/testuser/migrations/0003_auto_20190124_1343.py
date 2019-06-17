# Generated by Django 2.1.5 on 2019-01-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('testuser', '0002_auto_20190122_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='testuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user/avatar'),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='День варенья'),
        ),
    ]