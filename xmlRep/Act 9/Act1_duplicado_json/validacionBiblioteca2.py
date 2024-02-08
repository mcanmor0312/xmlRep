import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "ListaPeliculas": {
      "type": "object",
      "properties": {
        "Pelicula": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "Titulo": {
                "type": "string",
                "minLength": 1
              },
              "Director": {
                "type": "string",
                "minLength": 1
              },
              "AnioLanzamiento": {
                "type": "number",
                "minLength": 1
              },
              "Genero": {
                "type": "string",
                "minLength": 1
              }
            },
            "required": [
              "Titulo",
              "Director",
              "AnioLanzamiento",
              "Genero"
            ]
          }
        }
      },
      "required": [
        "Pelicula"
      ]
    }
  },
  "required": [
    "ListaPeliculas"
  ]
}
# Archivo JSON a validar
archivo_json = {
    "ListaPeliculas": {
      "Pelicula": [
        {
          "Titulo": "Sueño de Fuga",
          "Director": "Frank Darabont",
          "AnioLanzamiento": 1994,
          "Genero": "Drama"
        },
        {
          "Titulo": "El Padrino",
          "Director": "Francis Ford Coppola",
          "AnioLanzamiento": 1972,
          "Genero": "Crimen"
        },
        {
          "Titulo": "Tiempos Violentos",
          "Director": "Quentin Tarantino",
          "AnioLanzamiento": 1994,
          "Genero": "Crimen"
        },
        {
          "Titulo": "El Caballero de la Noche",
          "Director": "Christopher Nolan",
          "AnioLanzamiento": 2008,
          "Genero": "Acción"
        },
        {
          "Titulo": "Forrest Gump",
          "Director": "Robert Zemeckis",
          "AnioLanzamiento": 1994,
          "Genero": "Drama"
        },
        {
          "Titulo": "La Lista de Schindler",
          "Director": "Steven Spielberg",
          "AnioLanzamiento": 1993,
          "Genero": "Biografía"
        },
        {
          "Titulo": "Avatar",
          "Director": "James Cameron",
          "AnioLanzamiento": 2009,
          "Genero": "Acción"
        },
        {
          "Titulo": "Interstellar",
          "Director": "Christopher Nolan",
          "AnioLanzamiento": 2014,
          "Genero": "Ciencia Ficción"
        },
        {
          "Titulo": "La La Land",
          "Director": "Damien Chazelle",
          "AnioLanzamiento": 2016,
          "Genero": "Musical"
        },
        {
          "Titulo": "Matrix",
          "Director": "Lana Wachowski, Lilly Wachowski",
          "AnioLanzamiento": 1999,
          "Genero": "Ciencia Ficción"
        }
      ]
    }
  }

# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
