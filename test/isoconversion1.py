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
            >>> mi_app.ver_TempAdvIsoDF(one_step_aux,xtr)
            Creating Isoconversion DataFrames...
            Done
                      beta = 1.99 K/min  beta = 4.99 K/min  beta = 9.98 K/min  beta = 14.97 K/min  beta = 19.97 K/min
            0.002034           370.4750           376.7924           383.5566            375.7367            364.2142
            0.007034           397.9457           404.3177           413.3335            413.7057            419.2067
            0.012034           409.1716           415.1358           426.2000            429.9030            436.8788
            0.017034           413.7425           421.6344           433.0789            437.5273            442.9510
            0.022034           418.0522           425.3914           437.9619            442.8522            447.7177
            ...                     ...                ...                ...                 ...                 ...
            0.977034           546.0564           574.2008           575.9345            571.5515            623.7551
            0.982034           563.0231           591.9676           589.6036            579.6511            636.5502
            0.987034           588.5798           616.3721           612.9083            592.3100            649.0504
            0.992034           644.6658           641.6951           645.4324            615.3129            663.6677
            0.997034           666.2319           666.8888           671.6360            658.8527            675.9335
            <BLANKLINE>
            [200 rows x 5 columns]
            """
            try:
                isoTables = xtr.Isoconversion(d_a=0.005)
                print(isoTables[0])                
           
            except Exception as e:
                    
                messagebox.showerror("Unexpected error", f"Details: {str(e)}")
    
doctest.testmod()