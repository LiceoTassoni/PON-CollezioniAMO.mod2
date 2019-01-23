# vim:fileencoding=utf-8


import pandas as pd

from .util import *

def read_exel_db():
    """Reads excel database"""

    f = open(opj(json_path(), "collezioniamo_excel.xslx"))
    exceldb = json.load(f)
    f.close()

    return exceldb
