from django.db import models
from users.models import User
from django.utils import timezone


class Contest(models.Model):
    TYPES = (
        ('module', 'Функция'),
        ('programm', 'Программа'),
    )
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    input_data = models.TextField('Входные данные (описание)', null=True, serialize=True)
    output_data = models.TextField('Результат (описание)', null=True, serialize=True)
    for_everyone = models.BooleanField('Публичный ли контест:', default=True)
    special_for_users = models.ManyToManyField(User, verbose_name='Если приватный, то для кого:', related_name='contest', blank=True)
    timeout = models.IntegerField('Ограничение по времени в сек.', default=3)
    type_programm = models.CharField('Тип программы', choices=TYPES, default='module', max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

class UserContestAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers', verbose_name='Пользователь')
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, verbose_name='Задание')
    code = models.TextField('Код')
    short_status = models.CharField('Статус', default='OK', max_length=50)
    big_status = models.TextField('Развёрнутый статус', default='OK')
    time = models.DateTimeField(
        'Время отправки',
        default=timezone.now,
        db_index=True
    )

    def __str__(self) -> str:
        return f'{self.user.username}_{self.contest.name}_{self.id}'
    
    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователя'


class ContestTest(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, verbose_name='Задание', related_name='tests')
    input = models.TextField('Ввод (если это функция, то с названием)', blank=True, null=True, serialize=True)
    answer = models.TextField('Ответ', blank=True, null=True, serialize=True)

    def __str__(self) -> str:
        return f'{self.contest.name}_test_{self.id}'

    class Meta:
        verbose_name = 'Тест для задания'
        verbose_name_plural = 'Тесты для задания'


class ContestGroup(models.Model):
    name = models.CharField('Название', max_length=100)
    contests = models.ManyToManyField(Contest, verbose_name='Задания', blank=True)
    text_to_users = models.TextField('Напутственное слово:', default='Не переживай! Удачи)')
    special_for_users = models.ManyToManyField(User, verbose_name='Для кого:', related_name='can_view_group', blank=True)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Группа заданий'
        verbose_name_plural = 'Группы заданий'