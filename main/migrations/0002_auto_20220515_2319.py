# Generated by Django 3.2.9 on 2022-05-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='20-08-20'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.CharField(default='20-08-20', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='verification_ans',
            field=models.TextField(default='resr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='verification_question',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
