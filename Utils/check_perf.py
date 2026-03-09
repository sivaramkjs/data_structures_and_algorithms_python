from time import perf_counter


def check_performance(func, *inputs):
    start = perf_counter()
    val = func(*inputs)
    end = perf_counter()
    print(f'Took {end - start:.4f} seconds')
