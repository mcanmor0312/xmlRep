import json
from jsonschema import validate

# Definir el esquema
schema ={
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "reporteVentas": {
      "type": "object",
      "properties": {
        "informeRegion": {
          "type": "array",
          "items": {
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
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
                          },
                          "periodo2": {
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
                          },
                          "periodo3": {
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
                          },
                          "periodo4": {
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
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
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
                          },
                          "periodo2": {
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
                          },
                          "periodo3": {
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
                          },
                          "periodo4": {
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
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
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
                          },
                          "periodo2": {
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
                          },
                          "periodo3": {
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
                          },
                          "periodo4": {
                            "type": "object",
                            "properties": {
                              "entradasVendidas": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "entradasVendidas"
                            ]
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
          "explicacion": "Informe de ventas por región",
          "area": {
            "norte": {
              "periodos": {
                "periodo1": {
                  "entradasVendidas": 150
                },
                "periodo2": {
                  "entradasVendidas": 110
                },
                "periodo3": {
                  "entradasVendidas": 130
                },
                "periodo4": {
                  "entradasVendidas": 90
                }
              }
            },
            "centro": {
              "periodos": {
                "periodo1": {
                  "entradasVendidas": 100
                },
                "periodo2": {
                  "entradasVendidas": 120
                },
                "periodo3": {
                  "entradasVendidas": 80
                },
                "periodo4": {
                  "entradasVendidas": 110
                }
              }
            },
            "sur": {
              "periodos": {
                "periodo1": {
                  "entradasVendidas": 90
                },
                "periodo2": {
                  "entradasVendidas": 140
                },
                "periodo3": {
                  "entradasVendidas": 100
                },
                "periodo4": {
                  "entradasVendidas": 120
                }
              }
            }
          }
        },
        {
          "explicacion": "Informe de ventas por región",
          "area": {
            "norte": {
              "periodos": {
                "periodo1": {
                  "entradasVendidas": 100
                },
                "periodo2": {
                  "entradasVendidas": 120
                },
                "periodo3": {
                  "entradasVendidas": 90
                },
                "periodo4": {
                  "entradasVendidas": 110
                }
              }
            },
            "centro": {
              "periodos": {
                "periodo1": {
                  "entradasVendidas": 80
                },
                "periodo2": {
                  "entradasVendidas": 130
                },
                "periodo3": {
                  "entradasVendidas": 95
                },
                "periodo4": {
                  "entradasVendidas": 105
                }
              }
            },
            "sur": {
              "periodos": {
                "periodo1": {
                  "entradasVendidas": 110
                },
                "periodo2": {
                  "entradasVendidas": 115
                },
                "periodo3": {
                  "entradasVendidas": 100
                },
                "periodo4": {
                  "entradasVendidas": 120
                }
              }
            }
          }
        },
        {
          "explicacion": "Informe de ventas por región",
          "area": {
            "norte": {
              "periodos": {
                "periodo1": {
                  "entradasVendidas": 150
                },
                "periodo2": {
                  "entradasVendidas": 110
                },
                "periodo3": {
                  "entradasVendidas": 130
                },
                "periodo4": {
                  "entradasVendidas": 90
                }
              }
            },
            "centro": {
              "periodos": {
                "periodo1": {
                  "entradasVendidas": 100
                },
                "periodo2": {
                  "entradasVendidas": 120
                },
                "periodo3": {
                  "entradasVendidas": 80
                },
                "periodo4": {
                  "entradasVendidas": 110
                }
              }
            },
            "sur": {
              "periodos": {
                "periodo1": {
                  "entradasVendidas": 90
                },
                "periodo2": {
                  "entradasVendidas": 140
                },
                "periodo3": {
                  "entradasVendidas": 100
                },
                "periodo4": {
                  "entradasVendidas": 120
                }
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
