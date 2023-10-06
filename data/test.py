from contest.models import ContestTest
from importlib import reload
try:
    import data.solution
except:
    _ = ''


def test_function(function, params, output):
    reload(data.solution)
    assert eval(f'data.solution.{str(function) + str(params)}') == eval(output)


def main(contest):
    tests = ContestTest.objects.filter(contest=contest)
    num_last_test = len(tests)
    for num, test in enumerate(tests, 1):
        fun, params = test.input.split('(', 2)[0], f'({test.input.split("(", 2)[1]}'
        try:
            test_function(fun, params, test.answer)
        except AssertionError:
            return (f'Error! Incorrect answer!', f'Test {num}/{num_last_test}')
        except Exception as e:
            return (f'Error! Programm not worked!', f'Test {num}/{num_last_test} Error: {e}') 
    return ('OK', 'OK')