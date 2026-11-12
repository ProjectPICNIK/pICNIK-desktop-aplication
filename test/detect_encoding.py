from tkinter import filedialog, messagebox
import pandas as pd
import chardet
import doctest

class Aplication():
   

    def __init__(self):
        self.one_step_aux=[]

    def detect_encoding(self,file, num_bytes=10000):
            """
            >>> mi_app = Aplication()
            >>> mi_app.detect_encoding("examples/Paracetamol/PARACETAMOL_2.csv")
            ('UTF-16', 1.0)

            """
            with open(file, 'rb') as f:
                raw_data = f.read(num_bytes)
            result = chardet.detect(raw_data)
            return result['encoding'], result['confidence']



mi_app = Aplication()

# pasamos la ruta del archivo que queremos analizar entre los paréntesis
encoding, confidence = mi_app.detect_encoding("examples/Paracetamol/PARACETAMOL_2.csv")

print(f"Codificación: {encoding} con {confidence*100}% de confianza.")              
doctest.testmod()