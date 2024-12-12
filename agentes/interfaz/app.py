from flask import Flask, render_template
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate
from chainlit import Chainlit
import os
from utils.helpers import obtener_noticias

# Configura la API Key de OpenAI
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# Inicializa el modelo de lenguaje y la cadena de conversación
llm = ChatOpenAI(temperature=0.7)
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    prompt=PromptTemplate(
        input_variables=["history", "input"],
        template="""Eres un asistente de noticias de IA. Aquí tienes el historial de la conversación:
        {history}
        Humano: {input}
        Asistente:"""
    )
)


@Chainlit.on_chat_start
async def start():
    await Chainlit.send_message("Hola! Soy tu asistente de noticias. ¿En qué puedo ayudarte?")


@Chainlit.on_message
async def main(message: str):
    response = await Chainlit.run(conversation.run(message))

    if "mostrar noticias" in message.lower():
        noticias = obtener_noticias()
        noticias_formateadas = ""
        for noticia in noticias:
            noticias_formateadas += f"**{noticia[1]}** ({noticia[4]})\n{noticia[2]}\n\n"
        await Chainlit.send_message(noticias_formateadas)
    else:
        await Chainlit.send_message(response)
