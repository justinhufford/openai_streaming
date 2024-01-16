import os
import asyncio
from openai import AsyncOpenAI


client = AsyncOpenAI(
)

# Read the script's own source code
with open(__file__, 'r') as file:
    code = file.read()


async def main():
    stream = await client.chat.completions.create(
    #          Model:                  Input Cost:          Output Cost:      
    #          gpt-4-1106-preview      $0.010 / 1K tokens	$0.030 / 1K tokens
    #          gpt-3.5-turbo-1106      $0.001 / 1K tokens	$0.002 / 1K tokens
        model="gpt-3.5-turbo-1106",
        messages=[ {"role": "system", "content": "You are a programmer writing a helpful guide for implementing the text streaming feature of OpenAI's python API library. Please use the following code as an example of this functionality. This code assumes the user has their OpenAI API key stored as an enviroment variable. Code: ```python" + code + "``` Please write a helpful guide to text streaming. The user cannot see the code. Provide code snippets and various examples. Write as if you're writing a blog post or online guide. Please begin:"}],
        stream=True,
    )

    async for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        for char in content:
            print(char, end="", flush=True)
            await asyncio.sleep(0.000000001)  # Adjust delay to simulate typing speed
    input()

asyncio.run(main())

