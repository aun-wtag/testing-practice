import asyncio


async def mock_generate_response(*args, **kwargs):
    mock_tokens = ["Hello", " ", "World", " ", "test", " ", "tokens"]
    for token in mock_tokens:
        await asyncio.sleep(0.01)  # Simulate delay
        yield token

async def main():
    response = []
    async for token in mock_generate_response():
        response.append(token)
    print("".join(response))

asyncio.run(main())