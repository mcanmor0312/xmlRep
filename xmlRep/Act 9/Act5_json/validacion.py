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
                "type": "string"
              },
              "Resultado": {
                "type": "string"
              },
              "Observaciones": {
                "type": "string"
              },
              "IP_MAC": {
                "type": "object",
                "properties": {
                  "IP": {
                    "type": "string"
                  },
                  "MAC": {
                    "type": "string"
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
        "Resultado": "",
        "Observaciones": "Excelente desempeño en clase.",
        "IP_MAC": {
          "IP": "192.168.1.1"
        }
      },
      {
        "NIF": "987654321B",
        "Resultado": "",
        "Observaciones": "Debe mejorar en la participación.",
        "IP_MAC": {
          "MAC": "00:1A:2B:3C:4D:5E"
        }
      },
      {
        "NIF": "111223344X",
        "Resultado": "",
        "Observaciones": "Buen rendimiento académico.",
        "IP_MAC": {
          "IP": "192.168.1.2"
        }
      },
      {
        "NIF": "555666777Y",
        "Resultado": "",
        "Observaciones": "Participación destacada en actividades extracurriculares.",
        "IP_MAC": {
          "MAC": "11:22:33:44:55:66"
        }
      },
      {
        "NIF": "999888777Z",
        "Resultado": "",
        "Observaciones": "Atención necesaria en asignaturas específicas.",
        "IP_MAC": {
          "IP": "192.168.1.3"
        }
      },
      {
        "NIF": "333444555C",
        "Resultado": "",
        "Observaciones": "Destaca en matemáticas y ciencias.",
        "IP_MAC": {
          "IP": "192.168.1.4"
        }
      },
      {
        "NIF": "666777888D",
        "Resultado": "",
        "Observaciones": "Necesita mejorar la asistencia a clases.",
        "IP_MAC": {
          "MAC": "22:33:44:55:66:77"
        }
      },
      {
        "NIF": "444555666E",
        "Resultado": "",
        "Observaciones": "Participa activamente en actividades deportivas.",
        "IP_MAC": {
          "IP": "192.168.1.5"
        }
      },
      {
        "NIF": "777888999F",
        "Resultado": "",
        "Observaciones": "Interesado en la informática y la programación.",
        "IP_MAC": {
          "MAC": "33:44:55:66:77:88"
        }
      },
      {
        "NIF": "555444333G",
        "Resultado": "",
        "Observaciones": "Necesita más atención en la resolución de problemas.",
        "IP_MAC": {
          "IP": "192.168.1.6"
        }
      },
      {
        "NIF": "888999000H",
        "Resultado": "",
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
