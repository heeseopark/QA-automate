# Generated by Django 4.0.3 on 2023-02-21 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.PositiveIntegerField(default=1)),
                ('question_number', models.PositiveIntegerField(default=1)),
                ('count', models.PositiveIntegerField(default=1)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SibalSooSangDate',
            fields=[
                ('datecheck_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='qa_automate.datecheck')),
            ],
            bases=('qa_automate.datecheck',),
        ),
        migrations.CreateModel(
            name='SibalSooSangQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='qa_automate.question')),
            ],
            bases=('qa_automate.question',),
        ),
    ]
