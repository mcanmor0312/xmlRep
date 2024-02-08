import json
from jsonschema import validate

# Definir el esquema
schema ={
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "Puerto": {
      "type": "object",
      "properties": {
        "Barco": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "Codigo": {
                "type": "number",
                "minLength": 1
              },
              "Marca": {
                "type": "string",
                "minLength": 1
              },
              "Modelo": {},
              "Matricula": {
                "type": "string",
                "minLength": 1
              },
              "Potencia": {
                "type": "number",
                "minLength": 1
              },
              "CapacidadPasajeros": {
                "type": "number",
                "minLength": 1
              },
              "NumeroCabinas": {
                "type": "number",
                "minLength": 1
              }
            },
            "required": [
              "Codigo",
              "Marca",
              "Modelo",
              "Matricula",
              "Potencia",
              "CapacidadPasajeros",
              "NumeroCabinas"
            ]
          }
        }
      },
      "required": [
        "Barco"
      ]
    }
  },
  "required": [
    "Puerto"
  ]
}

# Archivo JSON a validar
archivo_json 
{
    "Puerto": {
      "Barco": [
        {
          "Codigo": 1,
          "Marca": "Yamaha",
          "Modelo": "Speedboat",
          "Matricula": "ABC123",
          "Potencia": 200,
          "CapacidadPasajeros": 6,
          "NumeroCabinas": 0
        },
        {
          "Codigo": 2,
          "Marca": "Sea Ray",
          "Modelo": "Express Cruiser",
          "Matricula": "DEF456",
          "Potencia": 350,
          "CapacidadPasajeros": 8,
          "NumeroCabinas": 2
        },
        {
          "Codigo": 3,
          "Marca": "Beneteau",
          "Modelo": "Oceanis",
          "Matricula": "GHI789",
          "Potencia": 150,
          "CapacidadPasajeros": 10,
          "NumeroCabinas": 3
        },
        {
          "Codigo": 4,
          "Marca": "Bayliner",
          "Modelo": "Bowrider",
          "Matricula": "JKL012",
          "Potencia": 180,
          "CapacidadPasajeros": 5,
          "NumeroCabinas": 0
        },
        {
          "Codigo": 5,
          "Marca": "Jeanneau",
          "Modelo": "Sun Odyssey",
          "Matricula": "MNO345",
          "Potencia": 130,
          "CapacidadPasajeros": 12,
          "NumeroCabinas": 4
        },
        {
          "Codigo": 6,
          "Marca": "Hanse",
          "Modelo": 415,
          "Matricula": "PQR678",
          "Potencia": 250,
          "CapacidadPasajeros": 8,
          "NumeroCabinas": 2
        },
        {
          "Codigo": 7,
          "Marca": "Fountain",
          "Modelo": "Lightning",
          "Matricula": "STU901",
          "Potencia": 450,
          "CapacidadPasajeros": 4,
          "NumeroCabinas": 1
        },
        {
          "Codigo": 8,
          "Marca": "Catalina",
          "Modelo": 375,
          "Matricula": "VWX234",
          "Potencia": 180,
          "CapacidadPasajeros": 6,
          "NumeroCabinas": 2
        },
        {
          "Codigo": 8,
          "Marca": "Catalina",
          "Modelo": 375,
          "Matricula": "VWX234",
          "Potencia": 180,
          "CapacidadPasajeros": 6,
          "NumeroCabinas": 2
        },
        {
          "Codigo": 9,
          "Marca": "Yandel",
          "Modelo": 378,
          "Matricula": "WUE647",
          "Potencia": 500,
          "CapacidadPasajeros": 200,
          "NumeroCabinas": 6
        },
        {
          "Codigo": 10,
          "Marca": "Durant",
          "Modelo": 543,
          "Matricula": "HGK332",
          "Potencia": 600,
          "CapacidadPasajeros": 400,
          "NumeroCabinas": 10
        }
      ]
    }
  }

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.