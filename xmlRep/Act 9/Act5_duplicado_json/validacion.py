import json
from jsonschema import validate

# Definir el esquema
schema ={
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "entrevista": {
      "type": "object",
      "properties": {
        "candidato": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "nombre": {
                "type": "string",
                "minLength": 1
              },
              "puesto": {
                "type": "string",
                "minLength": 1
              },
              "resultado": {
                "type": "object",
                "properties": {
                  "Apto": {
                    "type": "string",
                    "minLength": 1
                  },
                  "NoApto": {
                    "type": "string",
                    "minLength": 1
                  }
                },
                "required": []
              },
              "observaciones": {
                "type": "string",
              
              },
              "contacto": {
                "type": "object",
                "properties": {
                  "telefono": {
                    "type": "string"
                  },
                  "correo": {
                    "type": "string"
                  }
                },
                "required": [
                  "telefono",
                  "correo"
                ]
              }
            },
            "required": [
              "nombre",
              "puesto",
              "resultado",
              "observaciones",
              "contacto"
            ]
          }
        }
      },
      "required": [
        "candidato"
      ]
    }
  },
  "required": [
    "entrevista"
  ]
}

# Archivo JSON a validar
archivo_json ={
    "entrevista": {
      "candidato": [
        {
          "nombre": "Juan Perez",
          "puesto": "Desarrollador de Software",
          "resultado": {
            "Apto": ""
          },
          "observaciones": "Excelente experiencia en desarrollo web.",
          "contacto": {
            "telefono": "555-1234",
            "correo": "juan@example.com"
          }
        },
        {
          "nombre": "Maria Rodriguez",
          "puesto": "Analista de Datos",
          "resultado": {
            "NoApto": ""
          },
          "observaciones": "Necesita mejorar habilidades en análisis estadístico.",
          "contacto": {
            "telefono": "555-5678",
            "correo": "maria@example.com"
          }
        },
        {
          "nombre": "Carlos Gomez",
          "puesto": "Ingeniero de Sistemas",
          "resultado": {
            "Apto": ""
          },
          "observaciones": "Experiencia en administración de redes.",
          "contacto": {
            "telefono": "555-8765",
            "correo": "carlos@example.com"
          }
        },
        {
          "nombre": "Ana Martinez",
          "puesto": "Diseñadora Gráfica",
          "resultado": {
            "Apto": ""
          },
          "observaciones": "Destreza en herramientas de diseño.",
          "contacto": {
            "telefono": "555-4321",
            "correo": "ana@example.com"
          }
        },
        {
          "nombre": "Luis Hernandez",
          "puesto": "Consultor Financiero",
          "resultado": {
            "Apto": ""
          },
          "observaciones": "Conocimiento profundo en finanzas corporativas.",
          "contacto": {
            "telefono": "555-9999",
            "correo": "luis@example.com"
          }
        },
        {
          "nombre": "Sofia Ramirez",
          "puesto": "Analista de Marketing",
          "resultado": {
            "NoApto": ""
          },
          "observaciones": "Necesita mejorar habilidades en análisis de mercado.",
          "contacto": {
            "telefono": "555-6789",
            "correo": "sofia@example.com"
          }
        }
      ]
    }
  }
# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
