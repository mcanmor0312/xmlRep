import json
from jsonschema import validate

# Definir el esquema
schema ={
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "nba_players": {
      "type": "object",
      "properties": {
        "jugador": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "nombre": {
                "type": "string"
              },
              "equipo": {
                "type": "string"
              },
              "posicion": {
                "type": "string"
              },
              "altura": {
                "type": "string"
              },
              "peso": {
                "type": "string"
              },
              "universidad": {
                "type": "string"
              },
              "año_draft": {
                "type": "number"
              },
              "eleccion_draft": {
                "type": "string"
              },
              "equipo_draft": {
                "type": "string"
              }
            },
            "required": [
              "nombre",
              "equipo",
              "posicion",
              "altura",
              "peso",
              "universidad",
              "año_draft",
              "eleccion_draft",
              "equipo_draft"
            ]
          }
        }
      },
      "required": [
        "jugador"
      ]
    }
  },
  "required": [
    "nba_players"
  ]
}

# Archivo JSON a validar
archivo_json ={
    "nba_players": {
      "jugador": [
        {
          "nombre": "LeBron James",
          "equipo": "Los Angeles Lakers",
          "posicion": "Delantero",
          "altura": "6'9\"",
          "peso": "250 lbs",
          "universidad": "St. Vincent-St. Mary HS",
          "año_draft": 2003,
          "eleccion_draft": "1º en general",
          "equipo_draft": "Cleveland Cavaliers"
        },
        {
          "nombre": "Stephen Curry",
          "equipo": "Golden State Warriors",
          "posicion": "Base",
          "altura": "6'3\"",
          "peso": "185 lbs",
          "universidad": "Davidson",
          "año_draft": 2009,
          "eleccion_draft": "7º en general",
          "equipo_draft": "Golden State Warriors"
        },
        {
          "nombre": "Stephen Curry",
          "equipo": "Golden State Warriors",
          "posicion": "Base",
          "altura": "6'3\"",
          "peso": "185 lbs",
          "universidad": "Davidson",
          "año_draft": 2009,
          "eleccion_draft": "7º en general",
          "equipo_draft": "Golden State Warriors"
        },
        {
          "nombre": "Kawhi Leonard",
          "equipo": "Los Angeles Clippers",
          "posicion": "Delantero",
          "altura": "6'7\"",
          "peso": "225 lbs",
          "universidad": "San Diego State",
          "año_draft": 2011,
          "eleccion_draft": "15º en general",
          "equipo_draft": "Indiana Pacers"
        },
        {
          "nombre": "Giannis Antetokounmpo",
          "equipo": "Milwaukee Bucks",
          "posicion": "Delantero",
          "altura": "6'11\"",
          "peso": "242 lbs",
          "universidad": "filathlitikos",
          "año_draft": 2013,
          "eleccion_draft": "15º en general",
          "equipo_draft": "Milwaukee Bucks"
        },
        {
          "nombre": "Luka Dončić",
          "equipo": "Dallas Mavericks",
          "posicion": "Base-Delantero",
          "altura": "6'7\"",
          "peso": "230 lbs",
          "universidad": "Real Madrid",
          "año_draft": 2018,
          "eleccion_draft": "3º en general",
          "equipo_draft": "Atlanta Hawks (canjeado a Dallas Mavericks)"
        },
        {
          "nombre": "Anthony Davis",
          "equipo": "Los Angeles Lakers",
          "posicion": "Delantero-Pívot",
          "altura": "6'10\"",
          "peso": "253 lbs",
          "universidad": "Kentucky",
          "año_draft": 2012,
          "eleccion_draft": "1º en general",
          "equipo_draft": "New Orleans Hornets"
        },
        {
          "nombre": "Kevin Durant",
          "equipo": "Brooklyn Nets",
          "posicion": "Delantero",
          "altura": "6'10\"",
          "peso": "240 lbs",
          "universidad": "Texas",
          "año_draft": 2007,
          "eleccion_draft": "2º en general",
          "equipo_draft": "Seattle SuperSonics"
        },
        {
          "nombre": "James Harden",
          "equipo": "Brooklyn Nets",
          "posicion": "Escolta",
          "altura": "6'5\"",
          "peso": "220 lbs",
          "universidad": "Arizona State",
          "año_draft": 2009,
          "eleccion_draft": "3º en general",
          "equipo_draft": "Oklahoma City Thunder"
        },
        {
          "nombre": "Damian Lillard",
          "equipo": "Portland Trail Blazers",
          "posicion": "Base",
          "altura": "6'2\"",
          "peso": "195 lbs",
          "universidad": "Weber State",
          "año_draft": 2012,
          "eleccion_draft": "6º en general",
          "equipo_draft": "Portland Trail Blazers"
        },
        {
          "nombre": "Joel Embiid",
          "equipo": "Philadelphia 76ers",
          "posicion": "Pívot",
          "altura": "7'0\"",
          "peso": "280 lbs",
          "universidad": "Kansas",
          "año_draft": 2014,
          "eleccion_draft": "3º en general",
          "equipo_draft": "Philadelphia 76ers"
        }
      ]
    }
  }
# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
