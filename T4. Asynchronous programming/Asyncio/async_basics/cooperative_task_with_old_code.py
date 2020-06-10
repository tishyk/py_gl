import time
import asyncio

from old_code import old_style_function1, old_style_function2, page
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(40)  # For old style code

time.perf_counter()
start = time.time()


def tic():
    return 'at %1.1f seconds' % (time.time() - start)


async def generator1():
    # Busy waits for a second, but we don't want to stick around...
    print('generator1 started: {}'.format(tic()))
    await asyncio.sleep(2)
    print('generator1 ended work: {}'.format(tic()))


async def generator2():
    # Busy waits for a second, but we don't want to stick around...
    print('generator2 started: {}'.format(tic()))
    await asyncio.sleep(2)
    print('generator2 Ended work: {}'.format(tic()))


async def generator_with_old_function():
    print("Lets do some old stuff without blocking other coroutines")
    respond_ok = await io_loop.run_in_executor(pool, old_style_function2, page, 50)
    return respond_ok


io_loop = asyncio.get_event_loop()
# Use in generators for not blocking calls
# from_func_return = yield from io_loop.run_in_executor(pool, old_style_function, function_args)

tasks = [io_loop.create_task(generator1()),
         io_loop.create_task(generator2()),
         io_loop.create_task(generator_with_old_function())]

io_loop.run_until_complete(asyncio.wait(tasks))
io_loop.close()

print(time.perf_counter())
