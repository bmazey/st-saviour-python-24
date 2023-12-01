import time
from structures.lists import every_other
from demo.fibonacci_recursive import fibonacci_recursive
from demo.fibonacci_dynamic import fibonacci_dynamic

if __name__ == '__main__':
    tic = time.perf_counter()
    result = fibonacci_recursive(30)
    toc = time.perf_counter()
    print('recursive result: ' + str(result))
    print(f'time: {toc - tic:0.4f} seconds')

    tic = time.perf_counter()
    result = fibonacci_dynamic(30)
    toc = time.perf_counter()
    print('dynamic result: ' + str(result))
    print(f'time: {toc - tic: 0.4f} seconds')

