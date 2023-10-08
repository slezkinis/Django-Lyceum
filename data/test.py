from importlib import reload
import multiprocessing


def import_test():
    try:
        import data.solution
    except:
        return

def test_function(function):
    try:
        import data.solution
        reload(data.solution)
        # print(eval(f'data.solution.{str(function)[:len(function) - 1]}'))
        eval(f'data.solution.{function}')
    except:
        return


def start_test(function, output):
    process = multiprocessing.Process(target=import_test)
    process.start()

    # Ждём 300 секунд (5 минут) 
    process.join(3)
    # Если процесс живой,то убиваем его
    if process.is_alive():
        process.terminate()
        raise TimeoutError
    process2 = multiprocessing.Process(target=test_function, args=(function, ))
    process2.start()
    # Ждём 300 секунд (5 минут) 
    process2.join(3)

    # Если процесс живой,то убиваем его
    if process2.is_alive():
        process2.terminate()
        raise TimeoutError   
    import data.solution
    reload(data.solution)
    # # print(eval(f'data.solution.{str(function)[:len(function) - 1]}'))
    if output is None:
        assert eval(f'data.solution.{function}') is output
    else:
        assert eval(f'data.solution.{function}') == eval(output)
    # # print(1)


def main(contest):
    from contest.models import ContestTest
    tests = ContestTest.objects.filter(contest=contest)
    num_last_test = len(tests)
    for num, test in enumerate(tests, 1):
        try:
            start_test(test.input, test.answer)
        except AssertionError:
            return (f'Error! Incorrect answer!', f'Test {num}/{num_last_test}')
        except TimeoutError:
            return (f'Error! Timeout!', f'Test {num}/{num_last_test}')
        except Exception as e:
            return (f'Error! Programm not worked!', f'Test {num}/{num_last_test} Error: {e}') 
    return ('OK', 'OK')