from importlib import reload
import multiprocessing
import subprocess


def import_test():
    try:
        import data.solution
    except:
        return

def test_function(function):
    try:
        import data.solution
        reload(data.solution)
        eval(f'data.solution.{function}')
    except:
        return

def start_test_function(function):
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

def test_import_programm():
    try:
        import data.solution
        reload(data.solution)
        eval(f'data.solution')
    except:
        return

def start_test_programm_import():
    process = multiprocessing.Process(target=test_import_programm)
    process.start()

    # Ждём 300 секунд (5 минут) 
    process.join(3)
    # Если процесс живой,то убиваем его
    if process.is_alive():
        process.terminate()
        raise TimeoutError()

def start_tests_function(function, output):
    import data.solution
    reload(data.solution)
    if output is None:
        assert eval(f'data.solution.{function}') is output
    else:
        assert eval(f'data.solution.{function}') == eval(output)


def start_test_programm(input_data, output):
    try:
        programm_output = subprocess.check_output(['./python_code.sh', input_data])
    except Exception as ex:
        raise Exception(f'Programm exit with non-zero status')
    programm_output = programm_output.decode()
    if output is None:
        assert eval(programm_output) is output
    else:
        assert eval(programm_output) == eval(output)


def main(contest):
    from contest.models import ContestTest
    tests = ContestTest.objects.filter(contest=contest)
    num_last_test = len(tests)
    if contest.type_programm == 'module':
        try:
            start_test_function(tests[0].input)
        except TimeoutError:
            return (f'Error! Timeout!', f'Test 0/{num_last_test}')
        except Exception as e:
            return (f'Error! Programm not worked!', f'Error: {e}')
        for num, test in enumerate(tests, 1):
            try:
                start_tests_function(test.input, test.answer)
            except AssertionError:
                return (f'Error! Incorrect answer!', f'Test {num}/{num_last_test}')
            except TimeoutError:
                return (f'Error! Timeout!', f'Test {num}/{num_last_test}')
            except Exception as e:
                return (f'Error! Programm not worked!', f'Test {num}/{num_last_test} Error: {e}') 
        return ('OK', 'OK')
    elif contest.type_programm == 'programm':
        try:
            start_test_programm_import()
        except TimeoutError:
            return (f'Error! Timeout!', f'Test 0/{num_last_test}')
        except Exception as e:
            return (f'Error! Programm not worked!', f'Error: {e}')
        for num, test in enumerate(tests, 1):
            try:
                start_test_programm(test.input, test.answer)
            except AssertionError:
                return (f'Error! Incorrect answer!', f'Test {num}/{num_last_test}')
            except TimeoutError:
                return (f'Error! Timeout!', f'Test {num}/{num_last_test}')
            except Exception as e:
                return (f'Error! Programm not worked!', f'Test {num}/{num_last_test} Error: {e}') 
        return ('OK', 'OK')