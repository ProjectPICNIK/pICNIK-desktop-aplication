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
   

    #def conversion(self,one_step_aux):
    def method_menu(self,Beta,T0,isoTables):
                
            """
            >>> one_step_aux=['E_cnt_2.5.csv','E_cnt_5.csv','E_cnt_10.csv','E_cnt_15.csv','E_cnt_20.csv']
            >>> mi_app = Aplication()
            >>> xtr = pnk.DataExtraction()
            >>> Beta, T0, x, y = xtr.read_files(one_step_aux)
            Files to be used: 
            ['E_cnt_2.5.csv', 'E_cnt_5.csv', 'E_cnt_10.csv', 'E_cnt_15.csv', 'E_cnt_20.csv']
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
            >>> mi_app.method_menu(Beta,T0,isoTables)
            """
            
            try:
                ace = pnk.ActivationEnergy(Beta,T0,isoTables)              
                aVy = ace.aVy((5,380),var='time', p= 0.90)
                print(aVy)
            except Exception as e:
                    
                messagebox.showerror("Unexpected error", f"Details: {str(e)}")
    
doctest.testmod()