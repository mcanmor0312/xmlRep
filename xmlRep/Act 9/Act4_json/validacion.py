import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "clientes_v1": {
      "type": "object",
      "properties": {
        "sede": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "dir1": {
                "type": "string",
                "minLength": 1
              },
              "dir2": {
                "type": "string",
                "minLength": 1
              },
              "empleado": {
                "type": "string",
                "minLength": 1
              },
              "fecha": {
                "type": "string",
                "minLength": 1
              },
              "cliente1": {
                "type": "object",
                "properties": {
                  "cod": {
                    "type": "string",
                    "minLength": 1
                  },
                  "descripcion": {
                    "type": "string",
                    "minLength": 1
                  },
                  "numero": {
                    "type": "number",
                    "minLength": 1
                  },
                  "coste": {
                    "type": "number",
                    "minLength": 1
                  },
                  "resumen": {
                    "type": "string",
                    "minLength": 1
                  },
                  "plazo": {
                    "type": "string",
                    "minLength": 1
                  }
                },
                "required": [
                  "cod",
                  "descripcion",
                  "numero",
                  "coste",
                  "resumen",
                  "plazo"
                ]
              },
              "cliente2": {
                "type": "object",
                "properties": {
                  "cod": {
                    "type": "string",
                    "minLength": 1
                  },
                  "descripcion": {
                    "type": "string",
                    "minLength": 1
                  },
                  "numero": {
                    "type": "number",
                    "minLength": 1
                  },
                  "coste": {
                    "type": "number",
                    "minLength": 1
                  },
                  "resumen": {
                    "type": "string",
                    "minLength": 1
                  },
                  "plazo": {
                    "type": "string",
                    "minLength": 1
                  }
                },
                "required": [
                  "cod",
                  "descripcion",
                  "numero",
                  "coste",
                  "resumen",
                  "plazo"
                ]
              }
            },
            "required": [
              "dir1",
              "dir2",
              "empleado",
              "fecha",
              "cliente1"
            ]
          }
        }
      },
      "required": [
        "sede"
      ]
    }
  },
  "required": [
    "clientes_v1"
  ]
}

# Archivo JSON a validar
archivo_json ={
    "clientes_v1": {
      "sede": [
        {
          "dir1": "Dirección Principal 123",
          "dir2": "Zona Central",
          "empleado": "Juan Pérez",
          "fecha": "2024-01-22",
          "cliente1": {
            "cod": "COD-001",
            "descripcion": "Producto A",
            "numero": 1,
            "coste": 120.5,
            "resumen": "Compra de producto A",
            "plazo": "30 días"
          }
        },
        {
          "dir1": "Avenida Comercial 789",
          "dir2": "Zona Este",
          "empleado": "Maria Rodriguez",
          "fecha": "2024-01-23",
          "cliente1": {
            "cod": "COD-002",
            "descripcion": "Producto B",
            "numero": 2,
            "coste": 85.2,
            "resumen": "Compra de producto B",
            "plazo": "45 días"
          },
          "cliente2": {
            "cod": "COD-003",
            "descripcion": "Servicio de Consultoría",
            "numero": 3,
            "coste": 500,
            "resumen": "Contrato de consultoría técnica",
            "plazo": "60 días"
          }
        },
        {
          "dir1": "Calle Innovación 555",
          "dir2": "Zona Oeste",
          "empleado": "Carlos Gómez",
          "fecha": "2024-01-24",
          "cliente1": {
            "cod": "COD-004",
            "descripcion": "Producto C",
            "numero": 4,
            "coste": 150.75,
            "resumen": "Compra de producto C",
            "plazo": "30 días"
          },
          "cliente2": {
            "cod": "COD-005",
            "descripcion": "Servicio de Mantenimiento",
            "numero": 5,
            "coste": 300,
            "resumen": "Mantenimiento preventivo",
            "plazo": "90 días"
          }
        },
        {
          "dir1": "Av. Tecnológica 789",
          "dir2": "Zona Industrial",
          "empleado": "Laura Martínez",
          "fecha": "2024-01-25",
          "cliente1": {
            "cod": "COD-006",
            "descripcion": "Producto D",
            "numero": 6,
            "coste": 200,
            "resumen": "Compra de producto D",
            "plazo": "60 días"
          }
        },
        {
          "dir1": "Plaza Comercial 123",
          "dir2": "Zona Residencial",
          "empleado": "Ricardo García",
          "fecha": "2024-01-26",
          "cliente1": {
            "cod": "COD-007",
            "descripcion": "Producto E",
            "numero": 7,
            "coste": 75.5,
            "resumen": "Compra de producto E",
            "plazo": "30 días"
          },
          "cliente2": {
            "cod": "COD-008",
            "descripcion": "Servicio de Reparación",
            "numero": 8,
            "coste": 150,
            "resumen": "Reparación de equipos",
            "plazo": "45 días"
          }
        },
        {
          "dir1": "Calzada del Sol 456",
          "dir2": "Zona Comercial",
          "empleado": "Marta Sánchez",
          "fecha": "2024-01-27",
          "cliente1": {
            "cod": "COD-009",
            "descripcion": "Producto F",
            "numero": 9,
            "coste": 180,
            "resumen": "Compra de producto F",
            "plazo": "30 días"
          }
        },
        {
          "dir1": "Paseo de la Montaña 789",
          "dir2": "Zona Turística",
          "empleado": "Roberto López",
          "fecha": "2024-01-28",
          "cliente1": {
            "cod": "COD-010",
            "descripcion": "Producto G",
            "numero": 10,
            "coste": 250,
            "resumen": "Compra de producto G",
            "plazo": "60 días"
          },
          "cliente2": {
            "cod": "COD-011",
            "descripcion": "Servicio de Eventos",
            "numero": 11,
            "coste": 800,
            "resumen": "Organización de eventos corporativos",
            "plazo": "90 días"
          }
        },
        {
          "dir1": "Ruta del Sol 123",
          "dir2": "Zona Costera",
          "empleado": "Isabel Martínez",
          "fecha": "2024-01-29",
          "cliente1": {
            "cod": "COD-012",
            "descripcion": "Producto H",
            "numero": 12,
            "coste": 120,
            "resumen": "Compra de producto H",
            "plazo": "30 días"
          }
        }
      ]
    }
  }
# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
