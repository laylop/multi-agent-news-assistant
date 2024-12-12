import requests
from bs4 import BeautifulSoup
from utils.helpers import guardar_noticias

class AgenteRastreo:
    def __init__(self, fuentes):
        self.fuentes = fuentes

    def rastrear(self):
        for fuente in self.fuentes:
            try:
                response = requests.get(fuente["url"])
                response.raise_for_status()
                soup = BeautifulSoup(response.content, "html.parser")
                noticias = self.extraer_noticias(soup, fuente["selector"])
                guardar_noticias(noticias)
            except requests.exceptions.RequestException as e:
                print(f"Error al rastrear {fuente['url']}: {e}")

    def extraer_noticias(self, soup, selector):
        noticias = []
        articulos = soup.select(selector)
        for articulo in articulos:
            titulo = articulo.select_one("h2 a").text.strip()
            enlace = articulo.select_one("h2 a")["href"]
            resumen = articulo.select_one("p").text.strip()
            noticias.append({"titulo": titulo, "enlace": enlace, "resumen": resumen, "fuente": fuente["nombre"]})
        return noticias
