# Generated by Django 4.2.3 on 2023-10-02 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_alter_contesttest_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontestanswer',
            name='time',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Время отправки'),
        ),
        migrations.AlterField(
            model_name='contesttest',
            name='answer_type',
            field=models.TextField(choices=[('str', 'Str'), ('int', 'Int'), ('list', 'List'), ('dict', 'Dict'), ('bool', 'Bool'), ('none', 'None')], verbose_name='Тип ответа'),
        ),
        migrations.AlterField(
            model_name='contesttest',
            name='input',
            field=models.TextField(blank=True, verbose_name='Ввод (список через запятую, ; - несколько значений)'),
        ),
    ]