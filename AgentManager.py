from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()

class AgentManager:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o")

    def get_agent(self, task):
        return Agent(task=task, llm=self.llm)

    async def test(self, task):
        agent = self.get_agent(task)
        result = await agent.run()
        return result
