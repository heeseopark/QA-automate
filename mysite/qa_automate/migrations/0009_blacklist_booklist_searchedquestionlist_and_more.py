# Generated by Django 4.0.3 on 2023-04-07 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa_automate', '0008_extractedquestionlisttest_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('student', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('lecture', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(default='주교재', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SearchedQuestionList',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('page', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('theme', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa_automate.booklist')),
            ],
        ),
        migrations.CreateModel(
            name='FaqAndEstimatedAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('theme', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=1)),
                ('keyword1', models.CharField(max_length=20, null=True)),
                ('keyword2', models.CharField(max_length=20, null=True)),
                ('keyword3', models.CharField(max_length=20, null=True)),
                ('answer', models.TextField(default='')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa_automate.booklist')),
            ],
        ),
        migrations.CreateModel(
            name='ExtractedQuestionList',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('student', models.CharField(max_length=50)),
                ('page', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('theme', models.IntegerField(default=0)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('done', models.BooleanField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa_automate.booklist')),
            ],
        ),
        migrations.CreateModel(
            name='DateCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa_automate.booklist')),
            ],
        ),
        migrations.CreateModel(
            name='AnsweredQuestionList',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('student', models.CharField(max_length=50)),
                ('page', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('theme', models.IntegerField(default=0)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa_automate.booklist')),
            ],
        ),
    ]
