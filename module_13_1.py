import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(6 - power) # 6 условное число на 1 секунду больше максимальной силы участников
        print(f'Силач {name} поднял {i+1} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Алексей", 3))
    task2 = asyncio.create_task(start_strongman("Пётр", 4))
    task3 = asyncio.create_task(start_strongman("Александр", 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
