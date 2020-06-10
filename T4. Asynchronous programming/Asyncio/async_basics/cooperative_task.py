import time
import asyncio

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


async def generator3():
    print("Lets do some stuff while coroutines are blocked, {}".format(tic()))
    await asyncio.sleep(1)
    print("Done!")


io_loop = asyncio.get_event_loop()

tasks = [io_loop.create_task(generator1()),
         io_loop.create_task(generator2()),
         io_loop.create_task(generator3())]

io_loop.run_until_complete(asyncio.wait(tasks))
io_loop.close()

print(time.perf_counter())
