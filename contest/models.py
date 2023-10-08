from django.db import models
from users.models import User
from django.utils import timezone


class Contest(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    input_data = models.TextField('Входные данные (описание)', null=True)
    output_data = models.TextField('Результат (описание)', null=True)
    for_everyone = models.BooleanField('Публичный ли контест:', default=True)
    special_for_users = models.ManyToManyField(User, verbose_name='Если приватный, то для кого:', related_name='contest', blank=True)

    def __str__(self) -> str:
        return self.name


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


class ContestTest(models.Model):
    TYPES = (
        ('str', 'Str'),
        ('int', 'Int'),
        ('list', 'List'),
        ('dict', 'Dict'),
        ('bool', 'Bool'),
        ('none', 'None')
    )
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, verbose_name='Задание', related_name='tests')
    input = models.TextField('Ввод', blank=True, null=True)
    answer = models.TextField('Ответ', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.contest.name}_test_{self.id}'