from collections import deque
import asyncio

def some_gen(n):
    while n > -5:
        print('SG', n)
        yield n
        yield 1
        n -= 1
    yield 2
    return True


def countdown_task(n):
    print('C1:', n)
    yield from some_gen(n)
    return True
    print('C2:', n)
    yield from some_gen(n)
    n -= 1


for i in countdown_task(5):
    print('Loop i:', i)

# A list of tasks to run
tasks = deque([countdown_task(5),
               countdown_task(7),
               countdown_task(9)])


def scheduler(tasks):
    while tasks:
        task = tasks.popleft()
        try:
            next(task)
            tasks.append(task)
        except StopIteration:
            pass


scheduler(tasks)
