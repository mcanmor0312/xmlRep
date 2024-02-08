import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "archivos": {
      "type": "object",
      "properties": {
        "Alumno": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "NIF": {
                "type": "string",
                "minLength": 1
              },
              "Resultado": {
                "type": "string",
                "minLength": 1
              },
              "Observaciones": {
                "type": "string",
                "minLength": 1
              },
              "IP_MAC": {
                "type": "object",
                "properties": {
                  "IP": {
                    "type": "string",
                    "minLength": 1
                  },
                  "MAC": {
                    "type": "string",
                    "minLength": 1
                  }
                },
                "required": []
              }
            },
            "required": [
              "NIF",
              "Resultado",
              "Observaciones",
              "IP_MAC"
            ]
          }
        }
      },
      "required": [
        "Alumno"
      ]
    }
  },
  "required": [
    "archivos"
  ]
}

# Archivo JSON a validar
archivo_json ={
  "archivos": {
    "Alumno": [
      {
        "NIF": "123456789A",
        "Resultado": "6",
        "Observaciones": "Excelente desempeño en clase.",
        "IP_MAC": {
          "IP": "192.168.1.1"
        }
      },
      {
        "NIF": "987654321B",
        "Resultado": "6",
        "Observaciones": "Debe mejorar en la participación.",
        "IP_MAC": {
          "MAC": "00:1A:2B:3C:4D:5E"
        }
      },
      {
        "NIF": "111223344X",
        "Resultado": "6",
        "Observaciones": "Buen rendimiento académico.",
        "IP_MAC": {
          "IP": "192.168.1.2"
        }
      },
      {
        "NIF": "555666777Y",
        "Resultado": "6",
        "Observaciones": "Participación destacada en actividades extracurriculares.",
        "IP_MAC": {
          "MAC": "11:22:33:44:55:66"
        }
      },
      {
        "NIF": "999888777Z",
        "Resultado": "6",
        "Observaciones": "Atención necesaria en asignaturas específicas.",
        "IP_MAC": {
          "IP": "192.168.1.3"
        }
      },
      {
        "NIF": "333444555C",
        "Resultado": "6",
        "Observaciones": "Destaca en matemáticas y ciencias.",
        "IP_MAC": {
          "IP": "192.168.1.4"
        }
      },
      {
        "NIF": "666777888D",
        "Resultado": "6",
        "Observaciones": "Necesita mejorar la asistencia a clases.",
        "IP_MAC": {
          "MAC": "22:33:44:55:66:77"
        }
      },
      {
        "NIF": "444555666E",
        "Resultado": "6",
        "Observaciones": "Participa activamente en actividades deportivas.",
        "IP_MAC": {
          "IP": "192.168.1.5"
        }
      },
      {
        "NIF": "777888999F",
        "Resultado": "6",
        "Observaciones": "Interesado en la informática y la programación.",
        "IP_MAC": {
          "MAC": "33:44:55:66:77:88"
        }
      },
      {
        "NIF": "555444333G",
        "Resultado": "6",
        "Observaciones": "Necesita más atención en la resolución de problemas.",
        "IP_MAC": {
          "IP": "192.168.1.6"
        }
      },
      {
        "NIF": "888999000H",
        "Resultado": "6",
        "Observaciones": "Se destaca en las actividades artísticas.",
        "IP_MAC": {
          "MAC": "44:55:66:77:88:99"
        }
      }
    ]
  }
}
# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
