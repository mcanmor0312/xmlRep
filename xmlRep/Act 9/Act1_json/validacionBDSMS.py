import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "BDSMS": {
      "type": "object",
      "properties": {
        "sms": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "telefono": {
                "type": "number",
                "minLength": 1
              },
              "fecha": {
                "type": "string",
                "minLength": 1
              },
              "hora": {
                "type": "string",
                "minLength": 1
              },
              "mensaje": {
                "type": "string",
                "minLength": 1
              }
            },
            "required": [
              "telefono",
              "fecha",
              "hora",
              "mensaje"
            ]
          }
        }
      },
      "required": [
        "sms"
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
      "sms": [
        {
          "telefono": 1234567890,
          "fecha": "2024-01-11",
          "hora": "09:00 AM",
          "mensaje": "Hello, how are you?"
        },
        {
          "telefono": 9876543210,
          "fecha": "2024-01-11",
          "hora": "10:30 AM",
          "mensaje": "Meeting at 11 AM."
        },
        {
          "telefono": 5551234567,
          "fecha": "2024-01-11",
          "hora": "01:45 PM",
          "mensaje": "Don't forget to buy groceries!"
        },
        {
          "telefono": 7778889999,
          "fecha": "2024-01-11",
          "hora": "03:15 PM",
          "mensaje": "Call me back when you can."
        },
        {
          "telefono": 1112233445,
          "fecha": "2024-01-11",
          "hora": "05:00 PM",
          "mensaje": "Happy birthday!"
        },
        {
          "telefono": 9990001111,
          "fecha": "2024-01-11",
          "hora": "07:30 PM",
          "mensaje": "What's for dinner?"
        },
        {
          "telefono": 4445556666,
          "fecha": "2024-01-11",
          "hora": "09:45 PM",
          "mensaje": "Movie night tonight!"
        },
        {
          "telefono": 8887776666,
          "fecha": "2024-01-11",
          "hora": "11:00 PM",
          "mensaje": "Can't wait to see you!"
        },
        {
          "telefono": 2223334444,
          "fecha": "2024-01-11",
          "hora": "02:00 AM",
          "mensaje": "Good night!"
        },
        {
          "telefono": 6667778888,
          "fecha": "2024-01-11",
          "hora": "04:30 AM",
          "mensaje": "Need your help tomorrow."
        }
      ]
    }
  }

# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
