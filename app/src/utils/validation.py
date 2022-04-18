import re

cpf_cnpj_regex = re.compile(r"^\d{14}|000\d{11}$")
