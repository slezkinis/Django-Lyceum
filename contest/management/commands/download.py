from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import os
import datetime
import json

from contest.models import *

class Command(BaseCommand):
    help = 'Скачать информацию'

    def add_arguments(self, parser):
        parser.add_argument(
            "--contest",
            help="По определённому контесту",
            type=int
        )
        parser.add_argument(
            "--path",
            help="Путь до папки",
            default='test/'
        )
    
    def handle(self, *args, **options):
        path = options['path']
        all_contests = Contest.objects.all()
        all_users = User.objects.all()
        for contest in all_contests:
            try:
                os.mkdir(path + (contest.name).replace(' ', '_'))
            except FileNotFoundError:
                print(f'[!] Error! Не найдена папка {path}')
                return
            except FileExistsError:
                print(f"[!] Warning! Папка {path + (contest.name).replace(' ', '_')} уже существует")
            for user in all_users:
                try:
                    os.mkdir(f"{path + (contest.name).replace(' ', '_')}/{user.username}")
                except FileExistsError:
                    print(f"[!] Warning! Папка {path + (contest.name).replace(' ', '_')}/{user.username} уже существует")
                all_contest_answers = user.answers
                for contest_answer in all_contest_answers.all():
                    about_contest_answer = {
                        'code': contest_answer.code,
                        'short_status': contest_answer.short_status,
                        'big_status': contest_answer.big_status,
                        'send_at': contest_answer.time.strftime('%Y-%m-%d %H:%M')
                    }
                    with open(f"{path + (contest.name).replace(' ', '_')}/{user.username}/{contest.name}_{contest_answer.short_status}_{contest_answer.id}.json", 'w') as file:
                        json.dump(about_contest_answer, file, indent=2)
                    # except FileExistsError:
                    #     print(f"[!] Warning! Файл {path + (contest.name).replace(' ', '_')}/{user.username}/{contest.name}_{contest_answer.short_status}_{contest_answer.id}.json уже существует")
                    #     os.remove(f"{path + (contest.name).replace(' ', '_')}/{user.username}/{contest.name}_{contest_answer.short_status}_{contest_answer.id}.json")
                    #     with open(f"{path + (contest.name).replace(' ', '_')}/{user.username}/{contest.name}_{contest_answer.short_status}_{contest_answer.id}.json", 'w') as file:
                    #         json.dump(about_contest_answer, file, indent=2)


