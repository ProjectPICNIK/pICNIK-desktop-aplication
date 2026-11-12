from tkinter import messagebox
import picnik as pnk
import os
import pandas as pd
import re
import doctest


#the six initial main figures are draw


class Aplication():
   

    def __init__(self):
        self.one_step=[]

    # The usual DataExtraction commands
   

    def conversion(self,one_step_aux,xtr):
            """
            >>> one_step_aux=['examples/Decano/DEC_1.csv', 'examples/Decano/DEC_1.5.csv', 'examples/Decano/DEC_2.3.csv', 'examples/Decano/DEC_3.5.csv', 'examples/Decano/DEC_5.csv']
            >>> mi_app = Aplication()
            >>> xtr = pnk.DataExtraction()
            >>> B, T0, x, y = xtr.read_files(one_step_aux, encoding='utf16')
            Files to be used: 
            ['examples/Decano/DEC_1.csv', 'examples/Decano/DEC_1.5.csv', 'examples/Decano/DEC_2.3.csv', 'examples/Decano/DEC_3.5.csv', 'examples/Decano/DEC_5.csv']
            <BLANKLINE>
            Reading files and creating DataFrames...
            <BLANKLINE>
            The computed heating rates are:
            <BLANKLINE>
            <BLANKLINE>
             0.997 +/- 0.001 K/min
            <BLANKLINE>
            <BLANKLINE>
             1.516 +/- 0.002 K/min
            <BLANKLINE>
            <BLANKLINE>
             2.321 +/- 0.004 K/min
            <BLANKLINE>
            <BLANKLINE>
             3.538 +/- 0.006 K/min
            <BLANKLINE>
            <BLANKLINE>
             5.060 +/- 0.008 K/min
            <BLANKLINE>
            >>> xtr.Conversion([333,333,333,333,333],[777,777,777,777,777])
            Computing conversion values...
            Done
            <Figure size 1200x900 with 1 Axes>
            >>> isoTables  = xtr.Isoconversion(d_a = 0.005)
            Creating Isoconversion DataFrames...
            Done
            >>> mi_app.conversion(one_step_aux,xtr)
            Computing conversion values...
            Done
            """
           

            


            try:   
                fig=xtr.Conversion([333,333,333,333,333],[777,777,777,777,777])
                conversion_aux=1
                #self.draw_fig()

            except Exception as e:
                
                messagebox.showerror("Unexpected error", f"Details: {str(e)}")

doctest.testmod()