import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "ModuloProfesional": {
      "type": "object",
      "properties": {
        "Nombre": {
          "type": "string",
          "minLength": 1
        },
        "Asignaturas": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "Nombre": {
                "type": "string",
                "minLength": 1
              },
              "Contenidos": {
                "type": "object",
                "properties": {
                  "UD": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "Tipo": {
                          "type": "string",
                          "minLength": 1
                        },
                        "Descripcion": {
                          "type": "string",
                          "minLength": 1
                        }
                      },
                      "required": [
                        "Tipo",
                        "Descripcion"
                      ]
                    }
                  }
                },
                "required": [
                  "UD"
                ]
              }
            },
            "required": [
              "Nombre",
              "Contenidos"
            ]
          }
        }
      },
      "required": [
        "Nombre",
        "Asignaturas"
      ]
    }
  },
  "required": [
    "ModuloProfesional"
  ]
}

# Archivo JSON a validar
archivo_json ={
    "ModuloProfesional": {
      "Nombre": "Primer año de DAM",
      "Asignaturas": [
        {
          "Nombre": "Base de datos",
          "Contenidos": {
            "UD": [
              {
                "Tipo": "Enseñanza breve e introduccion",
                "Descripcion": "Descripción de la primera UD"
              },
              {
                "Tipo": "Enseñanza de esquemas en base de datos",
                "Descripcion": "Descripción de la segunda UD"
              },
              {
                "Tipo": "Enseñanza de esque mas mas avanzados en base de datos",
                "Descripcion": "Descripción de la tercera UD"
              },
              {
                "Tipo": "introduccion en sql",
                "Descripcion": "Descripción de la cuarta UD"
              }
            ]
          }
        },
        {
          "Nombre": "Programación",
          "Contenidos": {
            "UD": [
              {
                "Tipo": "Introducción a la programación",
                "Descripcion": "Descripción de la primera UD"
              },
              {
                "Tipo": "Estructuras de control y bucles",
                "Descripcion": "Descripción de la segunda UD"
              },
              {
                "Tipo": "Funciones y procedimientos",
                "Descripcion": "Descripción de la tercera UD"
              },
              {
                "Tipo": "Programación orientada a objetos",
                "Descripcion": "Descripción de la cuarta UD"
              }
            ]
          }
        },
        {
          "Nombre": "Lenguajes de Marcas",
          "Contenidos": {
            "UD": [
              {
                "Tipo": "Introducción a HTML",
                "Descripcion": "Descripción de la primera UD"
              },
              {
                "Tipo": "Creación de páginas web con HTML",
                "Descripcion": "Descripción de la segunda UD"
              },
              {
                "Tipo": "Introducción a CSS",
                "Descripcion": "Descripción de la tercera UD"
              },
              {
                "Tipo": "Estilización de páginas web con CSS",
                "Descripcion": "Descripción de la cuarta UD"
              }
            ]
          }
        },
        {
          "Nombre": "Entorno de Desarrollo",
          "Contenidos": {
            "UD": [
              {
                "Tipo": "Introducción a los entornos de desarrollo",
                "Descripcion": "Descripción de la primera UD"
              },
              {
                "Tipo": "Configuración de entornos de desarrollo",
                "Descripcion": "Descripción de la segunda UD"
              },
              {
                "Tipo": "Depuración en entornos de desarrollo",
                "Descripcion": "Descripción de la tercera UD"
              },
              {
                "Tipo": "Control de versiones en entornos de desarrollo",
                "Descripcion": "Descripción de la cuarta UD"
              }
            ]
          }
        },
        {
          "Nombre": "Sistemas Informáticos",
          "Contenidos": {
            "UD": [
              {
                "Tipo": "Introducción a los sistemas operativos",
                "Descripcion": "Descripción de la primera UD"
              },
              {
                "Tipo": "Administración de sistemas informáticos",
                "Descripcion": "Descripción de la segunda UD"
              },
              {
                "Tipo": "Redes de computadoras",
                "Descripcion": "Descripción de la tercera UD"
              },
              {
                "Tipo": "Seguridad informática",
                "Descripcion": "Descripción de la cuarta UD"
              }
            ]
          }
        },
        {
          "Nombre": "Formación y Orientación Laboral",
          "Contenidos": {
            "UD": [
              {
                "Tipo": "Introducción a la formación profesional",
                "Descripcion": "Descripción de la primera UD"
              },
              {
                "Tipo": "Metodologías de aprendizaje",
                "Descripcion": "Descripción de la segunda UD"
              },
              {
                "Tipo": "Orientación laboral",
                "Descripcion": "Descripción de la tercera UD"
              },
              {
                "Tipo": "Búsqueda de empleo",
                "Descripcion": "Descripción de la cuarta UD"
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
