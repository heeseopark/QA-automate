# Generated by Django 4.0.3 on 2023-04-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_automate', '0004_extractedquestionlisttest_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeredquestionlisttest',
            name='question',
            field=models.TextField(default='questiontext'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extractedquestionlisttest',
            name='question',
            field=models.TextField(default='questiontext'),
            preserve_default=False,
        ),
    ]
