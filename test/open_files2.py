from tkinter import filedialog, messagebox
import pandas as pd
import chardet
import doctest

class Aplication():
   

    def __init__(self):
        self.one_step_aux=[]
        self.files=[]

    def open_files(self,files2): 
            """
            >>> files2=("examples/Decano/DEC_1.5.csv","examples/Decano/DEC_1.csv","examples/Decano/DEC_2.3.csv","examples/Decano/DEC_3.5.csv","examples/Decano/DEC_5.csv")                     
            >>> mi_app = Aplication()
            >>> mi_app.open_files(files2)
            ('examples/Decano/DEC_1.5.csv', 'examples/Decano/DEC_1.csv', 'examples/Decano/DEC_2.3.csv', 'examples/Decano/DEC_3.5.csv', 'examples/Decano/DEC_5.csv')
            """
                
            self.one_step_aux.clear()
            
            try:
                #files = filedialog.askopenfilenames(
                #    filetypes=[("valid files", "*.csv *.txt")]
                #)
                files=files2
                # files validation
                if len(files) > 1:
                    self.one_step_aux.clear()
                    self.one_step_aux.extend(files)
                    
                    # save number files
                    self.numero_de_archivos = len(files)    
                else:
                    messagebox.showinfo(
                        title="Two or more files, please",
                        message="Two or more files, please"
                    )
                    self.one_step_aux.clear()
                    return # detiene la función aquí si no hay archivos válidos
               
                # validación del número de columnas solo corre si hay mas de un archivo
                estado = 0
                for file in self.one_step_aux:
                    try:
            
                        #codificacion, confianza = self.detect_encoding(file)
                        codificacion="UTF-16" 
                          
                        # 3. read colums for detect encoding
                        df = pd.read_csv(file, nrows=0, skipinitialspace=True, encoding=codificacion, sep=r'[\t,;]+', engine='python')
                        columnas = df.shape[1]
                            
                        if columnas != 3:
                            estado = 1
                            break 
                        #print(f"{columnas}---{estado}")    
                    except Exception as e:
                        print(f"Error al verificar columnas en {file}: {e}")
                        estado = 1
                        break
            
                if estado == 0: 
                    #self.view_graphs()
                    print(files)
                else:
                    messagebox.showerror(
                        title="Error file",
                        message="Number of columns incorrect or unreadable file. Please check your file."
                    )
                    
            except Exception as e:
                pass
                #messagebox.showerror("error", f"error open files: {e}")
                    

doctest.testmod()