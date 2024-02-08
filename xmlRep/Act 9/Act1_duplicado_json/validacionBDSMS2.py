import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "BDSMS": {
      "type": "object",
      "properties": {
        "contacto": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "nombre": {
                "type": "string"
              },
              "telefono": {
                "type": "number"
              },
              "fechaNacimiento": {
                "type": "string"
              },
              "email": {
                "type": "string"
              }
            },
            "required": [
              "nombre",
              "telefono",
              "fechaNacimiento",
              "email"
            ]
          }
        }
      },
      "required": [
        "contacto"
      ]
    }
  },
  "required": [
    "BDSMS"
  ]
}

# Archivo JSON a validar
archivo_json = {
    "BDSMS": {
      "contacto": [
        {
          "nombre": "John Doe",
          "telefono": 1234567890,
          "fechaNacimiento": "1980-05-15",
          "email": "john.doe@example.com"
        },
        {
          "nombre": "Jane Smith",
          "telefono": 9876543210,
          "fechaNacimiento": "1992-08-20",
          "email": "jane.smith@example.com"
        },
        {
          "nombre": "David Johnson",
          "telefono": 5551234567,
          "fechaNacimiento": "1975-12-10",
          "email": "david.johnson@example.com"
        },
        {
          "nombre": "Mary Williams",
          "telefono": 9998887777,
          "fechaNacimiento": "1988-03-25",
          "email": "mary.williams@example.com"
        },
        {
          "nombre": "Robert Brown",
          "telefono": 4445556666,
          "fechaNacimiento": "1995-11-05",
          "email": "robert.brown@example.com"
        },
        {
          "nombre": "Alice Johnson",
          "telefono": 7778889999,
          "fechaNacimiento": "1982-09-15",
          "email": "alice.johnson@example.com"
        },
        {
          "nombre": "Michael Davis",
          "telefono": 6669991111,
          "fechaNacimiento": "1978-07-08",
          "email": "michael.davis@example.com"
        },
        {
          "nombre": "Linda Miller",
          "telefono": 3332221111,
          "fechaNacimiento": "1990-04-12",
          "email": "linda.miller@example.com"
        },
        {
          "nombre": "William Taylor",
          "telefono": 1112223333,
          "fechaNacimiento": "1987-01-30",
          "email": "william.taylor@example.com"
        },
        {
          "nombre": "Susan White",
          "telefono": 8887776666,
          "fechaNacimiento": "1984-06-18",
          "email": "susan.white@example.com"
        }
      ]
    }
  }
# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
