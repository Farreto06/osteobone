import os
from openpyxl import load_workbook

class Excel:
    def __init__(self, ruta_excel, nombre_hoja = "Hoja1"):
        self.ruta_excel = ruta_excel
        self.nombre_hoja = nombre_hoja
        self.wb = load_workbook(ruta_excel)

        # Verificar si la hoja existe
        if nombre_hoja not in self.wb.sheetnames:
            print(f"Error: La hoja '{nombre_hoja}' no existe.")
            return

    def modificar_celda(self, celda, nuevo_valor):
        try:
            hoja = self.wb[self.nombre_hoja]
            hoja[celda] = nuevo_valor
            self.wb.save(self.ruta_excel)
        except Exception as e:
            print(f"Ocurrió un error al modificar la celda: {e}")


arch = Excel("Plantilla Retenciones osteobone.xlsx", "Hoja1")

arch.modificar_celda("K21", "125693")

#inputs
date = "02/07/2026"

# process varibles
scuensial_number = ""
split_date = date.split("/")
day = split_date[0]
month = split_date[1]
year = split_date[2]
numeroComprobante = f'N. DE COMPROBANTE {year}{month}000001__'

print("Ejecición finalizada.")