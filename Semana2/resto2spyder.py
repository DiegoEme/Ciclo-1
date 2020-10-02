


def prestamo(informacion: dict) -> dict:
    
    
    
    if(informacion["historia_credito"] == 1):
        if(informacion["ingreso_codeudor"] > 0 and informacion["ingreso_deudor"]/9 > informacion["cantidad_prestamo"]):
            respuesta = dict(id_prestamo=informacion["id_prestamo"], aprobado=True)
            return respuesta

        else:
            if(informacion["dependientes"] == "3+" and informacion["independiente"] == "Si"):
                if(informacion["ingreso_codeudor"]/12 > informacion["cantidad_prestamo"]):
                    respuesta =dict(id_prestamo=informacion["id_prestamo"], aprobado=True)
                    return respuesta
                else:
                    respuesta =  dict(id_prestamo=informacion["id_prestamo"], aprobado=False)
                    return respuesta
            else:
                if(informacion["cantidad_prestamo"] < 200):
                    respuesta =  dict(id_prestamo=informacion["id_prestamo"], aprobado=True)
                    return respuesta
                else:
                    respuesta =  dict(id_prestamo=informacion["id_prestamo"], aprobado=False)
                    return respuesta
    else:
        if(informacion["independiente"] == "Si"):
            if(not (informacion["casado"] == "Si") and (not(informacion["dependientes"] == 2) or not(informacion["dependientes"] == "3+"))):
                if(informacion["ingreso_deudor"]/10 > informacion["cantidad_prestamo"] or informacion["ingreso_codeudor"]/10 > informacion["cantidad_prestamo"]):
                    if(informacion["cantidad_prestamo"] < 180):
                        respuesta = dict(id_prestamo=informacion["id_prestamo"], aprobado=True)
                        return respuesta
                    else:
                        respuesta = dict(id_prestamo=informacion["id_prestamo"], aprobado=False)
                        return respuesta
                else:
                    respuesta = dict(id_prestamo=informacion["id_prestamo"], aprobado=False)
                    return respuesta
            else:
                respuesta =  dict(id_prestamo=informacion["id_prestamo"], aprobado=False)
                return respuesta
        else:
            if(not(informacion["tipo_propiedad"] == "Semiurbano" and informacion["dependientes"] < 2)):
                if(informacion["educacion"] == "Graduado"):
                    if(informacion["ingreso_deudor"]/11 > informacion["cantidad_prestamo"] and informacion["ingreso_codeudor"]/11 > informacion["cantidad_prestamo"]):
                        respuesta =  dict(id_prestamo=informacion["id_prestamo"], aprobado=True)
                        return respuesta
                    else:
                        respuesta =  dict(id_prestamo=informacion["id_prestamo"], aprobado=False)
                        return respuesta
                else:
                    respuesta =  dict(id_prestamo=informacion["id_prestamo"], aprobado=False)
                    return respuesta
            else:
                respuesta = dict(id_prestamo=informacion["id_prestamo"], aprobado=False)
                return respuesta

    return respuesta


        
print(prestamo({'id_prestamo': 'RETOS2_001', 'casado': 'No', 'dependientes': 0, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 4692, 'ingreso_codeudor': 120, 'cantidad_prestamo': 106, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_002', 'casado': 'Si', 'dependientes': '3+', 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 692, 'ingreso_codeudor': 150, 'cantidad_prestamo': 106, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Urbano'}))
print(prestamo({'id_prestamo': 'RETOS2_003', 'casado': 'Si', 'dependientes': '3+', 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 691, 'ingreso_codeudor': 1500, 'cantidad_prestamo': 106, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_004', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 0, 'cantidad_prestamo': 286, 'plazo_prestamo': 90, 'historia_credito': 1, 'tipo_propiedad': 'Urbano'}))
print(prestamo({'id_prestamo': 'RETOS2_005', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 0, 'cantidad_prestamo': 170, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_006', 'casado': 'No', 'dependientes': 2, 'educacion': 'No Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 1000, 'cantidad_prestamo': 86, 'plazo_prestamo': 460, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))
print(prestamo({'id_prestamo': 'RETOS2_007', 'casado': 'No', 'dependientes': 2, 'educacion': 'No Graduado', 'independiente': 'Si', 'ingreso_deudor': 11500, 'ingreso_codeudor': 1000, 'cantidad_prestamo': 256, 'plazo_prestamo': 460, 'historia_credito': 0, 'tipo_propiedad': 'Semiurbano'}))
print(prestamo({'id_prestamo': 'RETOS2_008', 'casado': 'No', 'dependientes': '3+', 'educacion': 'No Graduado', 'independiente': 'Si', 'ingreso_deudor': 100, 'ingreso_codeudor': 0, 'cantidad_prestamo': 1086, 'plazo_prestamo': 160, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))
print(prestamo({'id_prestamo': 'RETOS2_009', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si', 'ingreso_deudor': 11, 'ingreso_codeudor': 564, 'cantidad_prestamo': 100, 'plazo_prestamo': 189, 'historia_credito': 0, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_010', 'casado': 'No', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 11, 'ingreso_codeudor': 564, 'cantidad_prestamo': 100, 'plazo_prestamo': 189, 'historia_credito': 0, 'tipo_propiedad': 'Semiurbano'}))
print(prestamo({'id_prestamo': 'RETOS2_011', 'casado': 'No', 'dependientes': 1, 'educacion': 'No Graduado', 'independiente': 'No', 'ingreso_deudor': 11, 'ingreso_codeudor': 564, 'cantidad_prestamo': 100, 'plazo_prestamo': 189, 'historia_credito': 0, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_012', 'casado': 'No', 'dependientes': 0, 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 1111, 'ingreso_codeudor': 1111, 'cantidad_prestamo': 90, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Rural'}))
print(prestamo({'id_prestamo': 'RETOS2_013', 'casado': 'No', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 11, 'ingreso_codeudor': 564, 'cantidad_prestamo': 100, 'plazo_prestamo': 189, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))










