# Generated by Django 4.2.3 on 2023-10-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0014_remove_contest_entered_data_contest_input_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='input_data',
            field=models.TextField(null=True, verbose_name='Входные данные (описание)'),
        ),
        migrations.AlterField(
            model_name='contesttest',
            name='answer',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='contesttest',
            name='input',
            field=models.TextField(blank=True, null=True, verbose_name='Ввод'),
        ),
    ]