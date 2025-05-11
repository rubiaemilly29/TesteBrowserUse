from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import asyncio

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

async def main():
    task = """Acesse o link https://docs.google.com/document/d/1cRQZOB2Nzlf2js09CH3irm073HX1Rs6hMYGzJ-MWB3k/edit?usp=sharing
    Verifique se é possível adicionar um comentário no documento
    Adicione o comentário 'Teste' no documento
    Verifique se o comentário foi adicionado com sucesso
    """
    
    
    agent = Agent(task=task, llm=llm)
    result = await agent.run()


"""     print(f"Resultado: {result}")
 """
asyncio.run(main())
