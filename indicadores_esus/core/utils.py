import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from pyexcel_xlsx import get_data


def set_date_to_int(date):
    year = str(date.year)
    month = str(date.month).zfill(2)
    day = str(date.day).zfill(2)
    return int(f"{year}{month}{day}")


def set_int_to_date(intdate):
    strdate = str(intdate)
    year = int(strdate[:4])
    month = int(strdate[4:6])
    day = int(strdate[6:])
    return datetime.date(year, month, day)


def paginate(queryset, page_size, page):
    paginator = Paginator(queryset, per_page=page_size)
    page_obj = paginator.get_page(page)
    return page_obj


class Quadrimester:
    def __init__(self, quad, year):
        try:
            year = int(year)
            quad = int(quad)
        except ValueError:
            "Insira um valor válido para quadrimestre e ano"
        if not isinstance(quad, int) or quad not in [1, 2, 3]:
            raise ValidationError("Insira um quadrimestre de 1 a 3")
        if not isinstance(year, int):
            raise ValidationError("Insira um ano válido")
        self.quad = quad
        self.year = year
        self.evaluation_start = self.get_evaluation_start()
        self.evaluation_end = self.get_evaluation_end()
        self.extraction_start = self.get_extraction_start()
        self.extraction_end = self.evaluation_end
        self.dt_max_dum = self.get_max_dum()
        self.title = f"{quad} de {year}"
        self.abbrev = f"Q{quad}/{year}"

    def get_evaluation_start(self):
        month = 1
        if self.quad == 2:
            month = 5
        elif self.quad == 3:
            month = 9
        return datetime.date(self.year, month, 1)

    def get_evaluation_end(self):
        month = 1
        day = 31
        if self.quad == 1:
            month = 4
            day = 30
        elif self.quad == 2:
            month = 8
        elif self.quad == 3:
            month = 12
        return datetime.date(self.year, month, day)

    def get_extraction_start(self):
        return self.evaluation_start - relativedelta(months=9)

    def get_max_dum(self):
        return self.extraction_end - relativedelta(days=294)


def which_quadrimester(start_date, end_date=None):
    if start_date.month in range(1, 5):
        quad = 1
    elif start_date.month in range(5, 9):
        quad = 2
    elif start_date.month in range(9, 13):
        quad = 3
    else:
        quad = 3

    quad_object = Quadrimester(quad, start_date.year)
    return quad_object


def get_columns_index(raw_header):
    header = []
    for col in raw_header:
        col = col.upper()
        header.append(col)

    contract_col = ""
    qtd_inicial_col = ""

    if "CONTRATO / AS / OC" in header:
        contract_col = header.index("CONTRATO / AS / OC")
    elif "CONTRATO / AS" in header:
        contract_col = header.index("CONTRATO / AS")

    if "QTD INICIAL" in header:
        qtd_inicial_col = header.index("QTD INICIAL")
    elif "QTDD INICIAL" in header:
        qtd_inicial_col = header.index("QTDD INICIAL")

    columns = {
        "product": header.index("SERVIÇO"),
        "provider": header.index("EMPRESA"),
        "prov_contact": header.index("CONTATO(S)"),
        "prov_phone": header.index("TELEFONE"),
        "start_date": header.index("INÍCIO"),
        "end_date": header.index("VIGENCIA"),
        "unit_price": header.index("UNIT"),
        "balance": header.index("QUANTIDADE"),
        "prov_email": header.index("E-MAIL"),
        "contract_number": contract_col,
        "process_number": header.index("SEI"),
        "initial_quantity": qtd_inicial_col,
    }

    return columns
