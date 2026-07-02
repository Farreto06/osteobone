import shelve

def obtener_siguiente_codigo(archivo_db="datebase"):
    # Abrimos el archivo de shelve
    with shelve.open(archivo_db) as db:
        
        # Si es la primera vez que se ejecuta, el contador no existirá.
        # Lo inicializamos en 148 (el equivalente numérico de '00000148')
        if "contador_id" not in db:
            db["contador_id"] = 148
            
        # Leemos el ID actual guardado permanentemente
        id_actual = db["contador_id"]
        
        # Lo transformamos a un formato de texto de 8 dígitos con ceros a la izquierda
        # El formato ':08d' significa: entero (d) con un ancho de 8 caracteres, rellenado con ceros (0)
        id_formateado = f"{id_actual:08d}"
        
        # Incrementamos el valor numérico para la siguiente llamada y lo guardamos
        db["contador_id"] = id_actual + 1
        
        # Retornamos el código listo con sus 8 dígitos
        return id_formateado
