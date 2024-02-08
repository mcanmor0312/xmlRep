import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
      "reporteVentas": {
        "type": "object",
        "properties": {
          "informeRegion": {
            "type": "array",
            "items": [
              {
                "type": "object",
                "properties": {
                  "explicacion": {
                    "type": "string"
                  },
                  "area": {
                    "type": "object",
                    "properties": {
                      "norte": {
                        "type": "object",
                        "properties": {
                          "periodos": {
                            "type": "object",
                            "properties": {
                              "periodo1": {
                                "type": "string"
                              },
                              "periodo2": {
                                "type": "string"
                              },
                              "periodo3": {
                                "type": "string"
                              },
                              "periodo4": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "periodo1",
                              "periodo2",
                              "periodo3",
                              "periodo4"
                            ]
                          }
                        },
                        "required": [
                          "periodos"
                        ]
                      },
                      "centro": {
                        "type": "object",
                        "properties": {
                          "periodos": {
                            "type": "object",
                            "properties": {
                              "periodo1": {
                                "type": "string"
                              },
                              "periodo2": {
                                "type": "string"
                              },
                              "periodo3": {
                                "type": "string"
                              },
                              "periodo4": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "periodo1",
                              "periodo2",
                              "periodo3",
                              "periodo4"
                            ]
                          }
                        },
                        "required": [
                          "periodos"
                        ]
                      },
                      "sur": {
                        "type": "object",
                        "properties": {
                          "periodos": {
                            "type": "object",
                            "properties": {
                              "periodo1": {
                                "type": "string"
                              },
                              "periodo2": {
                                "type": "string"
                              },
                              "periodo3": {
                                "type": "string"
                              },
                              "periodo4": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "periodo1",
                              "periodo2",
                              "periodo3",
                              "periodo4"
                            ]
                          }
                        },
                        "required": [
                          "periodos"
                        ]
                      }
                    },
                    "required": [
                      "norte",
                      "centro",
                      "sur"
                    ]
                  }
                },
                "required": [
                  "explicacion",
                  "area"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "explicacion": {
                    "type": "string"
                  },
                  "area": {
                    "type": "object",
                    "properties": {
                      "norte": {
                        "type": "object",
                        "properties": {
                          "periodos": {
                            "type": "object",
                            "properties": {
                              "periodo1": {
                                "type": "string"
                              },
                              "periodo2": {
                                "type": "string"
                              },
                              "periodo3": {
                                "type": "string"
                              },
                              "periodo4": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "periodo1",
                              "periodo2",
                              "periodo3",
                              "periodo4"
                            ]
                          }
                        },
                        "required": [
                          "periodos"
                        ]
                      },
                      "centro": {
                        "type": "object",
                        "properties": {
                          "periodos": {
                            "type": "object",
                            "properties": {
                              "periodo1": {
                                "type": "string"
                              },
                              "periodo2": {
                                "type": "string"
                              },
                              "periodo3": {
                                "type": "string"
                              },
                              "periodo4": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "periodo1",
                              "periodo2",
                              "periodo3",
                              "periodo4"
                            ]
                          }
                        },
                        "required": [
                          "periodos"
                        ]
                      },
                      "sur": {
                        "type": "object",
                        "properties": {
                          "periodos": {
                            "type": "object",
                            "properties": {
                              "periodo1": {
                                "type": "string"
                              },
                              "periodo2": {
                                "type": "string"
                              },
                              "periodo3": {
                                "type": "string"
                              },
                              "periodo4": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "periodo1",
                              "periodo2",
                              "periodo3",
                              "periodo4"
                            ]
                          }
                        },
                        "required": [
                          "periodos"
                        ]
                      }
                    },
                    "required": [
                      "norte",
                      "centro",
                      "sur"
                    ]
                  }
                },
                "required": [
                  "explicacion",
                  "area"
                ]
              }
            ]
          }
        },
        "required": [
          "informeRegion"
        ]
      }
    },
    "required": [
      "reporteVentas"
    ]
  }
# Archivo JSON a validar
archivo_json ={
    "reporteVentas": {
       "informeRegion": [
         {
           "explicacion": "Este informe presenta las ventas de libros durante el primer trimestre del año 2023.",
           "area": {
             "norte": {
               "periodos": {
                 "periodo1": "500",
                 "periodo2": "600",
                 "periodo3": "700",
                 "periodo4": "800"
               }
             },
             "centro": {
               "periodos": {
                 "periodo1": "900",
                 "periodo2": "1000",
                 "periodo3": "1100",
                 "periodo4": "1200"
               }
             },
             "sur": {
               "periodos": {
                 "periodo1": "1300",
                 "periodo2": "1400",
                 "periodo3": "1500",
                 "periodo4": "1600"
               }
             }
           }
         },
         {
           "explicacion": "Este informe presenta las ventas de libros durante el segundo trimestre del año 2023.",
           "area": {
             "norte": {
               "periodos": {
                 "periodo1": "1700",
                 "periodo2": "1800",
                 "periodo3": "1900",
                 "periodo4": "2000"
               }
             },
             "centro": {
               "periodos": {
                 "periodo1": "2100",
                 "periodo2": "2200",
                 "periodo3": "2300",
                 "periodo4": "2400"
               }
             },
             "sur": {
               "periodos": {
                 "periodo1": "2500",
                 "periodo2": "2600",
                 "periodo3": "2700",
                 "periodo4": "2800"
               }
             }
           }
         }
       ]
    }
   }
# No necesitas cargar el archivo JSON con json.loads() porque ya tienes el diccionario

# Validar contra el esquema
validate(instance=archivo_json, schema=schema)

# El resto del comentario sobre cómo funciona la validación también está bien
