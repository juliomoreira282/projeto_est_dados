cadastro_cooperados = {
    "154.784.694-23": { "nome": "Josivaldo", "saldo": 3500.0 },
    "845.234.674-23": { "nome": "Letícia", "saldo": 4000.0 },
    "748.092.094-11": { "nome": "Gilberto", "saldo": 2000.0 },
    "897.453.344-99": { "nome": "Beatriz", "saldo": 3600.0 }
}

def obter_registro(cadastro: dict, cpf_cooperado: str):
    return cadastro.get(cpf_cooperado, "Usuário não encontrado.")

buscar_cooperado = input("Digite o CPF do cooperado que deseja procurar: ")
print(obter_registro(cadastro_cooperados, buscar_cooperado))