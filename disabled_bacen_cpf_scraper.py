import requests
from bs4 import BeautifulSoup

# Returns true if there is CPF from Bacen table.
# CPF has just numbers.
# Bacen website: https://www.bcb.gov.br/estabilidadefinanceira/quadroinabilitados
def isDisabledByBacen(cpf):
    # This url is from <iframe> tag.
    ROOT_URL = 'https://www3.bcb.gov.br/gepad/publicobcb/qgi/relatorioInternet'
    page = requests.get(ROOT_URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    bacen_table = soup.find(class_='centralizado')
    bacen_table_items = bacen_table.find_all('span')

    for item in bacen_table_items:
        if (target_cpf == item.contents[0]):
            return True
    
    return False

# Test
target_cpf = "00742567850"

if (isDisabledByBacen(target_cpf)):
    print("I found it.")
else:
    print("I did not find it.")