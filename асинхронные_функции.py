import time
import asyncio


def power(n):
    return n ** 2


def mult(n):
    return n * 5

async def f1(n):
    print(power(n))
    await asyncio.sleep(3)
    print('f1 completed')


async def f2(n):
    print(mult(n))
    await asyncio.sleep(2)
    print('f2 completed')


async def main():
    # task1 = asyncio.create_task(f1(5))
    # task2 = asyncio.create_task((f2(100)))
    # await task1
    # await task2

    await asyncio.gather(f1(7), f2(200))

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    stop = time.perf_counter()
    print(f'Duration: {stop - start:.2f}')

# def f1(n):
#     print(power(n))
#     time.sleep(3)
#     print('f1 completed')
#
#
# def f2(n):
#     print(mult(n))
#     time.sleep(3)
#     print('f2 completed')
#
#
# def main():
#     f1(5)
#     f2(100)
#
#
# if __name__ == '__main__':
#     start = time.perf_counter()
#     main()
#     stop = time.perf_counter()
#     print(f'Duration: {stop - start:.2f}')