from tkinter import messagebox
import picnik as pnk
import os
import pandas as pd
import re
import doctest


#the six initial main figures are draw


class Aplication():
   

    def __init__(self):
        self.one_step_aux=[]
        self.one_step=[]


    def view_graphs(self,one_step_aux2):
            """

            >>> one_step_aux2=['gDEC_1.5.csv', 'DEC_1.csv', 'DEC_2.3.csv', 'DEC_3.5.csv', 'DEC_5.csv']
            >>> mi_app = Aplication()
            >>> mi_app.view_graphs(one_step_aux2)
            Files to be used: 
            ['DEC_1.csv', 'gDEC_1.5.csv', 'DEC_2.3.csv', 'DEC_3.5.csv', 'DEC_5.csv']
            <BLANKLINE>
            Reading files and creating DataFrames...
            <BLANKLINE>

            """
            #self.configure_tem()
            try:
                self.one_step_aux=one_step_aux2
                # verification of selected files
                if not hasattr(self, 'one_step_aux') or not self.one_step_aux:
                    messagebox.showwarning("Warning", "No files selected to process.")
                    return

                # --- detección de encodings ---
                codificaciones = []
                for file in self.one_step_aux:
                    encoding='UTF-16'
                    if encoding:
                        codificaciones.append(encoding)
                    else:
                        messagebox.showerror("Error", f"The encoding could not be detected: {file}")
                        return
            
                encoding_set = set(codificaciones)
                if len(encoding_set) == 1:
                    self.encoding_final = encoding_set.pop()
                else:
                    messagebox.showerror(
                        "Encoding incompatibility",
                        "The files have different encodings:\n" + 
                        "\n".join(f"{f} => {e}" for f, e in zip(self.one_step_aux, codificaciones))
                    )
                    return 

                # data extraction and figure generation
                self.xtr = pnk.DataExtraction()
                
                # Function that isolates the file name to avoid including periods in the extension or paths
                
                def extraer_numero_de_ruta(ruta_completa):
                    
                    # extract only the final name
                    nombre_archivo = os.path.basename(ruta_completa)
                    
                    # remove the extension
                    nombre_sin_extension, _ = os.path.splitext(nombre_archivo)
                    
                    # extract only digits and periods from the clean name
                    solo_numeros = "".join(re.findall(r'[0-9.]', nombre_sin_extension))
                    try:
                        return float(solo_numeros)
                    except ValueError:
                        return float('inf') # Manda al final si algo sale mal

                #ordering
                self.one_step = sorted(self.one_step_aux, key=extraer_numero_de_ruta)

                self.fig, self.Beta, self.T0, self.DFlis = self.xtr.read_files(self.one_step, encoding=self.encoding_final)
                
                #review each DataFrame in the list
                array_DFlis = []
                limite_archivos = min(len(self.DFlis), 5)
                
                for i in range(limite_archivos):
                    try:
                        # Extract the maximum from column 4, safely converting to numeric
                        
                        valores_numericos = pd.to_numeric(self.DFlis[i].iloc[:, 4], errors='coerce')
                        max_valor = valores_numericos.max()
                        min_valor = valores_numericos.min()
                        if pd.notna(max_valor):
                            array_DFlis.append(int(max_valor))
                        if pd.notna(min_valor):
                            array_DFlis.append(int(min_valor))
                            
                            
                    except Exception:
                        pass
                
                if array_DFlis:
                    self.number_max = max(array_DFlis)
                    self.number_min = min(array_DFlis)
                    
                else:
                    self.number_max = 0
                    self.number_min = 0
                
                
                #self.draw_fig()

            except Exception as e:
                # unespected error
                pass
                #messagebox.showerror("error", f" Non-numeric data was detected, please check your files,  {str(e)}")

doctest.testmod()