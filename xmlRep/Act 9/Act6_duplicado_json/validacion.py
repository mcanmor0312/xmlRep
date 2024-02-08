import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "Departamento": {
      "type": "object",
      "properties": {
        "Nombre": {
          "type": "string"
        },
        "Carreras": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "Nombre": {
                "type": "string"
              },
              "Asignaturas": {}
            },
            "required": [
              "Nombre",
              "Asignaturas"
            ]
          }
        }
      },
      "required": [
        "Nombre",
        "Carreras"
      ]
    }
  },
  "required": [
    "Departamento"
  ]
}
# Archivo JSON a validar
archivo_json ={
    "Departamento": {
      "Nombre": "Departamento de Medicina",
      "Carreras": [
        {
          "Nombre": "Medicina General",
          "Asignaturas": [
            {
              "Nombre": "Anatomía",
              "UnidadesDidacticas": [
                {
                  "Tipo": "Teórico",
                  "Descripcion": "Estudio de la estructura del cuerpo humano."
                },
                {
                  "Tipo": "Práctico",
                  "Descripcion": "Prácticas de disección y observación."
                }
              ]
            },
            {
              "Nombre": "Patología",
              "UnidadesDidacticas": [
                {
                  "Tipo": "Teórico",
                  "Descripcion": "Estudio de enfermedades y trastornos."
                },
                {
                  "Tipo": "Práctico",
                  "Descripcion": "Observación clínica de pacientes."
                }
              ]
            }
          ]
        },
        {
          "Nombre": "Oftalmología",
          "Asignaturas": {
            "Nombre": "Anatomía ocular",
            "UnidadesDidacticas": [
              {
                "Tipo": "Teórico",
                "Descripcion": "Estudio de la estructura del ojo humano."
              },
              {
                "Tipo": "Práctico",
                "Descripcion": "Prácticas de cirugía ocular."
              }
            ]
          }
        }
    ]
    }
  }
# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
