from transformers import pipeline
from nltk.sentiment import SentimentIntensityAnalyzer

class AgentePNL:
    def __init__(self):
        self.resumen_pipeline = pipeline("summarization")
        self.analyzer = SentimentIntensityAnalyzer()

    def procesar_noticia(self, noticia):
        resumen = self.resumir(noticia["texto"])
        sentimiento = self.analizar_sentimiento(noticia["texto"])
        return {**noticia, "resumen": resumen, "sentimiento": sentimiento}

    def resumir(self, texto):
        resumen = self.resumen_pipeline(texto, max_length=100, min_length=30, do_sample=False)
        return resumen[0]["summary_text"]

    def analizar_sentimiento(self, texto):
        scores = self.analyzer.polarity_scores(texto)
        if scores["compound"] > 0.05:
            return "positivo"
        elif scores["compound"] < -0.05:
            return "negativo"
        else:
            return "neutral"
