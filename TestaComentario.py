from AgentManager import AgentManager
import asyncio
import sys

class TestaComentario:
    def __init__(self):
        self.agent_manager = AgentManager()

    async def testaSeEPossivelAdicionarERemoverComentario(self):
        task = """Acesse o link https://docs.google.com/document/d/1orGRdLg3CJbsgP9CN71b-5kNIi1TB2QcRepmJxKiTIg/edit?usp=sharing
        Verifique se é possível adicionar um comentário no documento
        Adicione um comentário aleatorio no documento
        Verifique se o comentário foi adicionado com sucesso
        Verifique se é possível remover o comentário
        remova o comentário do documento acessando os tres pontinhos e clicando em "excluir"
        confirme clicando em "excluir"
        Verifique se o comentário foi removido com sucesso
        """
        result =  await self.agent_manager.test(task)
        print(result)


    async def main(self):
        await self.testaSeEPossivelAdicionarERemoverComentario()

            

if __name__ == "__main__":
    instancia = TestaComentario()
    asyncio.run(instancia.main())

