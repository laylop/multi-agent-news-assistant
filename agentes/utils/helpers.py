import sqlite3


def guardar_noticias(noticias):
    conn = sqlite3.connect('base_datos/noticias.db')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO noticias (titulo, enlace, resumen, fuente) VALUES (?, ?, ?, ?)",
                       [(noticia["titulo"], noticia["enlace"], noticia["resumen"], noticia["fuente"]) for noticia in noticias])
    conn.commit()
    conn.close()


def obtener_noticias():
    conn = sqlite3.connect('base_datos/noticias.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM noticias")
    noticias = cursor.fetchall()
    conn.close()
    return noticias
