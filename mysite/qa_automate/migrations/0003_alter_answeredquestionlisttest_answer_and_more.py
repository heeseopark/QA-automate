# Generated by Django 4.0.3 on 2023-04-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_automate', '0002_searchedquestionlisttest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeredquestionlisttest',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='faqandestimatedanswertest',
            name='answer',
            field=models.TextField(default=''),
        ),
    ]
