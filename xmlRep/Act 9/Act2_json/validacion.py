import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "Concesionario": {
      "type": "object",
      "properties": {
        "Coche": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "Codigo": {
                "type": "number"
              },
              "Marca": {
                "type": "string"
              },
              "Modelo": {
                "type": "string"
              },
              "Matricula": {
                "type": "string"
              },
              "Potencia": {
                "type": "number"
              },
              "Plazas": {
                "type": "number"
              },
              "Puertas": {
                "type": "number"
              }
            },
            "required": [
              "Codigo",
              "Marca",
              "Modelo",
              "Matricula",
              "Potencia",
              "Plazas",
              "Puertas"
            ]
          }
        }
      },
      "required": [
        "Coche"
      ]
    }
  },
  "required": [
    "Concesionario"
  ]
}

# Archivo JSON a validar
archivo_json = {
    "Concesionario": {
      "Coche": [
        {
          "Codigo": 1,
          "Marca": "Ford",
          "Modelo": "Focus",
          "Matricula": "ABC123",
          "Potencia": 120,
          "Plazas": 5,
          "Puertas": 4
        },
        {
          "Codigo": 2,
          "Marca": "Toyota",
          "Modelo": "Corolla",
          "Matricula": "DEF456",
          "Potencia": 110,
          "Plazas": 5,
          "Puertas": 4
        },
        {
          "Codigo": 3,
          "Marca": "Honda",
          "Modelo": "Civic",
          "Matricula": "GHI789",
          "Potencia": 130,
          "Plazas": 5,
          "Puertas": 4
        },
        {
          "Codigo": 4,
          "Marca": "Chevrolet",
          "Modelo": "Malibu",
          "Matricula": "JKL012",
          "Potencia": 140,
          "Plazas": 5,
          "Puertas": 4
        },
        {
          "Codigo": 5,
          "Marca": "Volkswagen",
          "Modelo": "Passat",
          "Matricula": "MNO345",
          "Potencia": 125,
          "Plazas": 5,
          "Puertas": 4
        },
        {
          "Codigo": 6,
          "Marca": "BMW",
          "Modelo": "320i",
          "Matricula": "PQR678",
          "Potencia": 180,
          "Plazas": 5,
          "Puertas": 4
        },
        {
          "Codigo": 7,
          "Marca": "Mercedes-Benz",
          "Modelo": "C-Class",
          "Matricula": "STU901",
          "Potencia": 160,
          "Plazas": 5,
          "Puertas": 4
        },
        {
          "Codigo": 8,
          "Marca": "Audi",
          "Modelo": "A4",
          "Matricula": "VWX234",
          "Potencia": 150,
          "Plazas": 5,
          "Puertas": 4
        },
        {
          "Codigo": 9,
          "Marca": "BMV",
          "Modelo": "Serie1",
          "Matricula": "MKB356",
          "Potencia": 350,
          "Plazas": 5,
          "Puertas": 4
        },
        {
          "Codigo": 10,
          "Marca": "Opel",
          "Modelo": "Coursa",
          "Matricula": "JUL234",
          "Potencia": 200,
          "Plazas": 5,
          "Puertas": 4
        }
      ]
    }
  }
# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
