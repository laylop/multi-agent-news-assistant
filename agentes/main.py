from agentes.agente_rastreo import AgenteRastreo
from agentes.agente_pnl import AgentePNL
from agentes.agente_personalizacion import AgentePersonalizacion
from agentes.agente_interaccion import AgenteInteraccion
from interfaz.app import app


def main():
    fuentes = [
        {"nombre": "El País", "url": "https://elpais.com/", "selector": "article.c_b"},
        {"nombre": "BBC News", "url": "https://www.bbc.com/news",
            "selector": "article.gs-c-promo"}
    ]

    # Inicializar agentes
    agente_rastreo = AgenteRastreo(fuentes)
    agente_pnl = AgentePNL()
    agente_personalizacion = AgentePersonalizacion()
    agente_interaccion = AgenteInteraccion()

    # Realizar el rastreo y procesamiento
    agente_rastreo.rastrear()
    noticias = agente_pnl.procesar_noticia(noticias)

    # Ejecutar el servidor Flask
    app.run(debug=True)


if __name__ == "__main__":
    main()
