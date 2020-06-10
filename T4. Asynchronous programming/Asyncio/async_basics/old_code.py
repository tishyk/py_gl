import time
import requests

page = 'https://www.leroymerlin.ua/'


def old_style_function1(*args):
    start = time.time()
    while (time.time() - start) < 5:
        # Some blocking old function
        pass
    print('Old function call done in %1.1f seconds with args: %s' % (time.time() - start, args))
    return True

def old_style_function2(page, symbols_count):
    start = time.time()
    respond = requests.get(page)
    if respond.ok:
        print(respond.content[:symbols_count])
    print('Old function call done in %1.1f seconds' % (time.time() - start))
    return respond.ok


if __name__ == "__main__":
    start = time.time()
    old_style_function1(page)
    old_style_function2(page)
    print('Summary: Old code execution done in %1.1f seconds' % (time.time() - start))
