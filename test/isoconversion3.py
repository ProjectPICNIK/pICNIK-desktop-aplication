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
            >>> mi_app.ver_TempAdvIsoDF(one_step_aux,xtr)
            Creating Isoconversion DataFrames...
            Done
                      beta = 2.50 K/min  beta = 5.00 K/min  beta = 10.00 K/min  beta = 15.00 K/min  beta = 20.00 K/min
            0.002027           445.0437           459.3545            474.5730            483.8592            490.4537
            0.007027           471.4102           487.4201            504.4989            514.9477            522.3798
            0.012027           483.7911           500.6284            518.6167            529.6355            537.4788
            0.017027           492.1588           509.5662            528.1825            539.5954            547.7229
            0.022027           498.5530           516.4020            535.5053            547.2240            555.5722
            ...                     ...                ...                 ...                 ...                 ...
            0.977027           666.7993           698.1326            732.2462            751.9288            762.4467
            0.982027           669.5062           701.0869            735.4591            754.9639            764.8105
            0.987027           672.8830           704.7739            739.4604            758.6117            767.4665
            0.992027           677.5283           709.8487            744.9433            763.2830            770.5230
            0.997027           685.7883           718.8803            754.5450            770.0782            774.1662
            <BLANKLINE>
            [200 rows x 5 columns]
            """
            try:
                isoTables = xtr.Isoconversion(d_a=0.005)
                print(isoTables[0])                
           
            except Exception as e:
                    
                messagebox.showerror("Unexpected error", f"Details: {str(e)}")
    
doctest.testmod()