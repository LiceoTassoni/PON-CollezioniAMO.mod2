# vim:fileencoding=utf-8

import math

import pandas as pd
import json

from .util import *

transfer_columns = [
    'ID', 'Armadio (indicare la lettera presente a fianco della serratura)',
    "Ripiano (dal basso all'alto)",
    'Numero di inventario Provincia? (se presente)',
    'Ditta costruttrice? (se rintracciabile)',
    'Cartellino? (riportare il testo se presente)',
    'Nome assegnato (eventualmente provvisorio)',
    'Ambito fisico',
    'Stato di conservazione',
    'Nota sullo stato di conservazione (osservazioni, interventi suggeriti,...)',
    'Materiali (se riconoscibili)',
    'Breve descrizione del funzionamento (se  conosciuta)',
    'Risorse (testi, siti web) utilizzate',
    "Giudizio complessivo sul livello di interesse dell'oggetto ai fini espositivi"
]

def read_exel_db():
    """Reads excel database"""

    exceldb = pd.read_excel(opj(static_path(), "collezioniamo_excel.xlsx"))
    ### insert sorting here


    exceldb_list = []
    for k in range(len(exceldb)):
        dict_list = [("ID", int(exceldb["ID"][k]))]
        for col_name in transfer_columns[1:]:
            try:
                if math.isnan(exceldb[col_name][k]):
                    dict_list.append((col_name, None))
                else:
                    dict_list.append((col_name, exceldb[col_name][k]))
            except TypeError:
                dict_list.append((col_name, exceldb[col_name][k]))
        exceldb_list.append(dict(dict_list))
    #[dict([("ID", int(exceldb["ID"][k]))]+[
    #    (col_name, exceldb[col_name][k]) for col_name in transfer_columns[1:]]
    #) for k in range(len(exceldb))]

    return exceldb_list

def exceldb_gen():
    """Excel database generator"""
    exceldb = read_exel_db()
    for i in exceldb:
        yield i
