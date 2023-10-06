from django.db import models
from users.models import User
from django.utils import timezone


class Contest(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')

    def __str__(self) -> str:
        return self.name


class UserContestAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
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
    input = models.TextField('Ввод', blank=True)
    answer = models.CharField('Ответ', max_length=100, blank=True)

    def __str__(self) -> str:
        return f'{self.contest.name}_test_{self.id}'