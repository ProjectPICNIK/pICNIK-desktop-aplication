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
            >>> one_step_aux=['examples/Paracetamol/PARACETAMOL_2.csv', 'examples/Paracetamol/PARACETAMOL_5.csv', 'examples/Paracetamol/PARACETAMOL_10.csv', 'examples/Paracetamol/PARACETAMOL_15.csv', 'examples/Paracetamol/PARACETAMOL_20.csv']
            >>> mi_app = Aplication()
            >>> xtr = pnk.DataExtraction()
            >>> B, T0, x, y = xtr.read_files(one_step_aux, encoding='UTF-16')
            Files to be used: 
            ['examples/Paracetamol/PARACETAMOL_2.csv', 'examples/Paracetamol/PARACETAMOL_5.csv', 'examples/Paracetamol/PARACETAMOL_10.csv', 'examples/Paracetamol/PARACETAMOL_15.csv', 'examples/Paracetamol/PARACETAMOL_20.csv']
            <BLANKLINE>
            Reading files and creating DataFrames...
            <BLANKLINE>
            The computed heating rates are:
            <BLANKLINE>
            <BLANKLINE>
             1.987 +/- 0.002 K/min
            <BLANKLINE>
            <BLANKLINE>
             4.985 +/- 0.002 K/min
            <BLANKLINE>
            <BLANKLINE>
             9.979 +/- 0.004 K/min
            <BLANKLINE>
            <BLANKLINE>
            14.974 +/- 0.006 K/min
            <BLANKLINE>
            <BLANKLINE>
            19.972 +/- 0.009 K/min
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