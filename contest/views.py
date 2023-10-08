from django.shortcuts import render, redirect
from .models import Contest, UserContestAnswer, ContestTest
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django import forms
import os
from django.views.decorators.csrf import csrf_exempt

import datetime


class Contest_Check(forms.Form):
    code = forms.CharField(required=True,
                            widget=forms.Textarea)


# @csrf_exempt
def show_test(request, task_id):
    answer = ('', '')
    contest = get_object_or_404(Contest, id=task_id)
    if request.method == 'POST':
        form = Contest_Check(request.POST)
        if form.is_valid():
            # Form fields passed validation
            code = form.cleaned_data['code'].replace('input()', '')
            with open('data/solution.py', 'w') as file:
                file.write(code)
            import data.test        
            answer = data.test.main(contest)
            UserContestAnswer.objects.create(
                user=request.user,
                contest=contest,
                code=code,
                short_status=answer[0],
                big_status=answer[1],
                time=datetime.datetime.now()
            )
            os.remove('data/solution.py')
    form = Contest_Check()
    answers = []
    first_test = ContestTest.objects.filter(contest=contest).first()
    enter_data = first_test.input
    result_data = first_test.answer
    if request.user.is_authenticated:
        user_answers = UserContestAnswer.objects.filter(user=request.user, contest=contest)
        answers = []
        for contest_answer in user_answers[::-1]:
            answers.append({'id': contest_answer.id, 'time': contest_answer.time.strftime('%Y-%m-%d %H:%M'), 'status': contest_answer.short_status, 'code_link': f'/answer/{contest_answer.id}'})
    return render(request, 'contest.html', context={
        'id': task_id,
        'name': contest.name,
        'description': contest.description,
        'type_input_data': contest.input_data,
        'type_output_data': contest.output_data,
        'example_input_data' : enter_data,
        'example_output_data': result_data,
        'form': form,
        'answer': answer[0],
        'user_answers': answers
    })


# @csrf_exempt
def get_answer_status(request, answer_id):
    answer = get_object_or_404(UserContestAnswer, id=answer_id)
    if answer.user != request.user:
        return redirect('home')
    return render(request, 'answer.html', context={'code': answer.code, 'short_status': answer.short_status, 'large_status': answer.big_status})


# @csrf_exempt
def main(request):
    if not request.user.is_authenticated:
        about_contest = Contest.objects.filter(for_everyone=True)
    else:
        about_contest = Contest.objects.filter(Q(for_everyone=True) | Q(special_for_users=request.user))
    contests = []
    for contest in about_contest:
        contests.append({
            'title': contest.name,
            'link': f'task/{contest.id}'
        })
    return render(request, 'all_contests.html', context={'contests': contests})