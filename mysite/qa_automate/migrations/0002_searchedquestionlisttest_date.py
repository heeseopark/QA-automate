# Generated by Django 4.0.3 on 2023-04-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_automate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchedquestionlisttest',
            name='date',
            field=models.DateField(default='2023-03-01'),
            preserve_default=False,
        ),
    ]
