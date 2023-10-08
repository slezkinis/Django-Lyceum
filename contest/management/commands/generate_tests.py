from django.core.management.base import BaseCommand
import os
import datetime
import random
import json
from test_code import *

from contest.models import *

class Command(BaseCommand):
    help = 'Сгенерировать тесты для контеста (файл с кодом должен лежать в корне проекта и называться main.py)'

    def add_arguments(self, parser):
        parser.add_argument("contest_id", type=int, help='ID контеста')
        parser.add_argument("function_name", type=str, help='Название функции')
        parser.add_argument(
            "--number_of_tests",
            help="Количество создаваемых тестов",
            type=int,
            default=17
        )
        parser.add_argument(
            "--remove_old_tests",
            help="Удалить старые тесты",
            type=bool,
            default=False
        )
    
    def handle(self, *args, **options):
        try:
            contest = Contest.objects.get(id=options['contest_id'])
        except Contest.DoesNotExist:
            print(f"[!] Error! Контест с ID {options['contest_id']} не найден")
            return
        if options['remove_old_tests']:
            for i in ContestTest.objects.filter(contest=contest):
                i.delete()
            print(f'[!] Info! Все тесты для контеста {contest.name} удалены!')
        func = eval(options["function_name"])
        count_args = func.__code__.co_argcount
        # print(count_args)
        # print(contest)
        for _ in range(options['number_of_tests']):
            while True:
                arguments = []
                for i in range(count_args):
                    arguments.append(random.uniform(-1000000, 1000000))
                    # print(arguments)
                # output = eval(f'{options["function_name"]}({", ".join([str(x) for x in arguments])})')
                try:
                    output = eval(f'{options["function_name"]}({", ".join([str(x) for x in arguments])})')
                except:
                    continue
                ContestTest.objects.create(
                    contest=contest,
                    input=f'{options["function_name"]}({", ".join([str(x) for x in arguments])})',
                    answer=output
                )
                break
            # print(f'[!] Info! Тест создан!')
        print(f'[!] Info! Создано {options["number_of_tests"]} тестов')
                

