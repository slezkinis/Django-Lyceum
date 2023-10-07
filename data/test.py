from importlib import reload
import multiprocessing


def import_test():
    import data.solution

def test_function(function, params, output):
    import data.solution
    reload(data.solution)
    # print(eval(f'data.solution.{str(function)[:len(function) - 1]}'))
    try:
        eval(f'data.solution.{str(function) + str(params)}')
    except AssertionError:
        raise AssertionError

def test_time_function(function, params):
    import data.solution
    eval(f'data.solution.{str(function) + str(params)}')

def start_test(function, params, output):
    process = multiprocessing.Process(target=import_test)
    process.start()

    # Ждём 300 секунд (5 минут) 
    process.join(3)

    # Если процесс живой,то убиваем его
    if process.is_alive():
        print('KILL')
        process.terminate()
        raise TimeoutError
    process2 = multiprocessing.Process(target=test_function, args=(function, params, output, ))
    process2.start()
    # Ждём 300 секунд (5 минут) 
    process2.join(2)

    # Если процесс живой,то убиваем его
    if process2.is_alive():
        process2.terminate()
        raise TimeoutError    
    import data.solution
    reload(data.solution)
    # # print(eval(f'data.solution.{str(function)[:len(function) - 1]}'))
    assert eval(f'data.solution.{str(function) + str(params)}') == eval(output)
    # # print(1)


def main(contest):
    from contest.models import ContestTest
    tests = ContestTest.objects.filter(contest=contest)
    num_last_test = len(tests)
    for num, test in enumerate(tests, 1):
        fun, params = test.input.split('(', 2)[0], f'({test.input.split("(", 2)[1]}'
        try:
            start_test(fun, params, test.answer)
        except AssertionError:
            return (f'Error! Incorrect answer!', f'Test {num}/{num_last_test}')
        except TimeoutError:
            return (f'Error! Timeout!', f'Test {num}/{num_last_test}')
        except Exception as e:
            return (f'Error! Programm not worked!', f'Test {num}/{num_last_test} Error: {e}') 
    return ('OK', 'OK')