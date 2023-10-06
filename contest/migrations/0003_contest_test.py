# Generated by Django 4.2.3 on 2023-09-30 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_usercontestanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(blank=True, max_length=10000, verbose_name='Ввод (список через запятую)')),
                ('input_type', models.CharField(choices=[('str', 'Str'), ('int', 'Int'), ('list', 'List'), ('dict', 'Dict'), ('bool', 'Bool'), ('none', 'None')], max_length=10000, verbose_name='Тип ввода')),
                ('answer', models.CharField(blank=True, max_length=100, verbose_name='Ответ')),
                ('answer_type', models.CharField(choices=[('str', 'Str'), ('int', 'Int'), ('list', 'List'), ('dict', 'Dict'), ('bool', 'Bool'), ('none', 'None')], max_length=10000, verbose_name='Тип ответа')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='contest.contest', verbose_name='Задание')),
            ],
        ),
    ]