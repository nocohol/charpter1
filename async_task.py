import asyncio
# define a coroutine for simulating a time-consuming task


async def fetch_data(delay):
    print('Fetching data ...')
    await asyncio.sleep(delay)
    print('data fetched')
    return {"data": "Some Data"}

#define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    print("do something before fetch_data completes")
    # await the fetch_data coroutine, pausing execution of main util fetch_data completes
    result = await task
    print(f"Received data: {result}")
    print("End of main coroutine")
    
    task2 = fetch_data(2)
    result2 = await task2
    
    task3 = fetch_data(2)
    result3 = await task3
    
    print(result2)
    print(result3)

# run the main coroutine
asyncio.run(main())
