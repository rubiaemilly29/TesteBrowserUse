from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="acesse o link https://docs.google.com/document/d/1cRQZOB2Nzlf2js09CH3irm073HX1Rs6hMYGzJ-MWB3k/edit?usp=sharing , selecione a aba Arquivo, depois baixar, depois microsoft word",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())