from tkinter import messagebox
import picnik as pnk
import os
import pandas as pd
import re
import doctest
from rxn_models import rxn_models 

#the six initial main figures are draw


class Aplication():
   

    def __init__(self):
        self.one_step=[]

    # The usual DataExtraction commands
   

    def conversion(self,one_step_aux,xtr):
            """
            >>> one_step_aux=['examples/Constant_E/E_cnt_2.5.csv', 'examples/Constant_E/E_cnt_5.csv', 'examples/Constant_E/E_cnt_10.csv', 'examples/Constant_E/E_cnt_15.csv', 'examples/Constant_E/E_cnt_20.csv']
            >>> mi_app = Aplication()
            >>> xtr = pnk.DataExtraction()
            >>> B, T0, x, y = xtr.read_files(one_step_aux)
            Files to be used: 
            ['examples/Constant_E/E_cnt_2.5.csv', 'examples/Constant_E/E_cnt_5.csv', 'examples/Constant_E/E_cnt_10.csv', 'examples/Constant_E/E_cnt_15.csv', 'examples/Constant_E/E_cnt_20.csv']
            <BLANKLINE>
            Reading files and creating DataFrames...
            <BLANKLINE>
            The computed heating rates are:
            <BLANKLINE>
            <BLANKLINE>
             2.500 +/- 0.000 K/min
            <BLANKLINE>
            <BLANKLINE>
             5.000 +/- 0.000 K/min
            <BLANKLINE>
            <BLANKLINE>
            10.000 +/- 0.000 K/min
            <BLANKLINE>
            <BLANKLINE>
            15.000 +/- 0.000 K/min
            <BLANKLINE>
            <BLANKLINE>
            20.000 +/- 0.000 K/min
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
               
            except Exception as e:
                
                messagebox.showerror("Unexpected error", f"Details: {str(e)}")

doctest.testmod()