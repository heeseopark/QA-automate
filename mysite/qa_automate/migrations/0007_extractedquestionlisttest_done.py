# Generated by Django 4.0.3 on 2023-04-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_automate', '0006_remove_extractedquestionlisttest_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='extractedquestionlisttest',
            name='done',
            field=models.BooleanField(default='False'),
            preserve_default=False,
        ),
    ]
