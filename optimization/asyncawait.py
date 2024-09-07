import asyncio

async def say_hello():
    print("Hello, world!")
    await asyncio.sleep(2)
    print("Goodbye, world!")


if __name__ == "__main__":
    asyncio.run(say_hello())