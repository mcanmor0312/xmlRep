import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "biblioteca": {
      "type": "object",
      "properties": {
        "libro": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "titulo": {},
              "autor": {
                "type": "string",
                "minLength": 1
              },
              "publicacion": {
                "type": "number",
                "minLength": 1
              },
              "genero": {
                "type": "string",
                "minLength": 1
              }
            },
            "required": [
              "titulo",
              "autor",
              "publicacion",
              "genero"
            ]
          }
        }
      },
      "required": [
        "libro"
      ]
    }
  },
  "required": [
    "biblioteca"
  ]
}

# Archivo JSON a validar
archivo_json = {
    "biblioteca": {
      "libro": [
        {
          "titulo": "El Señor de los Anillos",
          "autor": "J.R.R. Tolkien",
          "publicacion": 1954,
          "genero": "Fantasía"
        },
        {
          "titulo": "Cien años de soledad",
          "autor": "Gabriel García Márquez",
          "publicacion": 1967,
          "genero": "Realismo mágico"
        },
        {
          "titulo": 1984,
          "autor": "George Orwell",
          "publicacion": 1949,
          "genero": "Ficción distópica"
        },
        {
          "titulo": "Orgullo y prejuicio",
          "autor": "Jane Austen",
          "publicacion": 1813,
          "genero": "Clásico romántico"
        },
        {
          "titulo": "Harry Potter y la piedra filosofal",
          "autor": "J.K. Rowling",
          "publicacion": 1997,
          "genero": "Fantasía"
        },
        {
          "titulo": "Crónica de una muerte anunciada",
          "autor": "Gabriel García Márquez",
          "publicacion": 1981,
          "genero": "Realismo mágico"
        },
        {
          "titulo": "Fahrenheit 451",
          "autor": "Ray Bradbury",
          "publicacion": 1953,
          "genero": "Ficción distópica"
        },
        {
          "titulo": "Don Quijote de la Mancha",
          "autor": "Miguel de Cervantes",
          "publicacion": 1605,
          "genero": "Clásico"
        },
        {
          "titulo": "Juego de tronos",
          "autor": "George R.R. Martin",
          "publicacion": 1996,
          "genero": "Fantasía épica"
        },
        {
          "titulo": "Los pilares de la Tierra",
          "autor": "Ken Follett",
          "publicacion": 1989,
          "genero": "Novela histórica"
        }
      ]
    }
  }

# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
