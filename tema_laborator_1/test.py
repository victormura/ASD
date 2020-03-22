import random
import time
from datetime import timedelta

def test_1(sort_method):
	test_input = list(range(100))[::-1]
	sort_method(test_input)
	print('N = {}, Max = {}'.format(len(test_input), max(test_input)))
	return sort_method(test_input) == sorted(test_input)

def test_2(sort_method):
	test_input = list(range(100))
	print('N = {}, Max = {}'.format(len(test_input), max(test_input)))
	return sort_method(test_input) == sorted(test_input)

def test_3(sort_method):
	test_input = list(random.randrange(1, 1000001) for i in range(1, 1001))
	print('N = {}, Max = {}'.format(len(test_input), max(test_input)))

	return sort_method(test_input) == sorted(test_input)

def test_4(sort_method):
	test_input = list(random.randrange(1, 1000001) for i in range(1, 10001))
	print('N = {}, Max = {}'.format(len(test_input), max(test_input)))

	return sort_method(test_input) == sorted(test_input)

def test_5(sort_method):
	test_input = list()
	test_output = list()
	print('input_list = []')
	return sort_method(test_input) == test_output

def test_6(sort_method):
	print('input_list = None')
	test_input = None
	test_output = None

	return sort_method(test_input) == test_output

def test_7(sort_method):
	test_input = [5]
	print('N = {}, Max = {}'.format(len(test_input), max(test_input)))
	return sort_method(test_input) == test_input

def test_8(sort_method):
	test_input = [-7, 11, -23, 6]
	print('N = {}, Max = {}'.format(len(test_input), max(test_input)))
	return sort_method(test_input) == sorted(test_input)

def test_all(sort_methods):
	tests = [test_1, test_2, test_3, test_4, test_5, test_6, test_7, test_8]
	print('T = {}'.format(len(tests)))
	for index, test in enumerate(tests):
		print('\n-- Test {}'.format(index+1))
		for key, method in sort_methods.items():
			start_time = time.monotonic()
			test_status = 'Passed' if test(method) else 'Failure'
			end_time = time.monotonic()
			duration = timedelta(seconds=end_time - start_time)
			print("- {} - {}, {}".format(key,
				'{} seconds'.format(duration.seconds) if duration.seconds > 0 else '{} microseconds'.format(duration.microseconds), test_status))

