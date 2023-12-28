import json
import sys
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from field import field
from gen_random import gen_random

path = 'data_light.json'

with open(path, encoding='utf_8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return [i for i in Unique(field(arg, 'job-name'), ignore_case=True)]


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом python', arg))


@print_result
def f4(arg):
    zipped = list(zip(arg, gen_random(len(arg), 100000, 200000)))
    return [f'{i[0]}, зарплата {i[1]} руб' for i in zipped]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))