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
    def ver_TempAdvIsoDF(self,one_step_aux,xtr):
                
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
            >>> mi_app.ver_TempAdvIsoDF(one_step_aux,xtr)
            Creating Isoconversion DataFrames...
            Done
                      beta = 1.00 K/min  beta = 1.52 K/min  beta = 2.32 K/min  beta = 3.54 K/min  beta = 5.06 K/min
            0.002117           333.0402           333.0258           333.0610           333.1253           333.1526
            0.007117           333.0315           333.0769           333.1936           333.3476           333.4496
            0.012117           333.0536           333.1450           333.2956           333.5759           333.7474
            0.017117           333.0678           333.1996           333.3958           333.7989           334.0345
            0.022117           333.0871           333.2500           333.5220           334.0184           334.3227
            ...                     ...                ...                ...                ...                ...
            0.977117           336.7541           342.0985           349.9181           359.4899           364.2228
            0.982117           338.9712           342.1812           350.0330           359.6088           364.3604
            0.987117           358.2767           342.2869           350.1420           359.7461           364.5133
            0.992117           404.6883           343.8612           350.2714           359.9046           364.7116
            0.997117           465.6947           393.6009           351.3926           360.3743           370.8200
            <BLANKLINE>
            [200 rows x 5 columns]
            """
            try:
                isoTables = xtr.Isoconversion(d_a=0.005)
                print(isoTables[0])                
           
            except Exception as e:
                    
                messagebox.showerror("Unexpected error", f"Details: {str(e)}")
    
doctest.testmod()