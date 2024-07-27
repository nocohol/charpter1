'''import asyncio'''
import asyncio

# test
async def fetch_data(id, sleep_time):
    '''
    simulate fetching data in a consuming time
    Args:
    id - task id
    sleep_time - sleep time
    '''
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    '''
    create tasks for running corountine concurretly
    '''
    task1 = asyncio.create_task(fetch_data(1, 1))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 2))
    result1 = await task1
    result2 = await task2
    result3 = await task3
    print(result1, result2, result3)
    
    # Return a future aggregating results from the given coroutines/futures
    result4 = await asyncio.gather(fetch_data(1, 1), fetch_data(2, 3), fetch_data(3, 2))
    print(result4)
asyncio.run(main())
