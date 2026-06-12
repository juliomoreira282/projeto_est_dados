placas_no_patio = set()

def registrar_verificar_placas(conjunto_placas: set, nova_placa: str):
    nova_placa = nova_placa.upper()
    if nova_placa in conjunto_placas:
        return f"O veículo de placa {nova_placa} já está no pátio."
    
    conjunto_placas.add(nova_placa)
    return f"Placa {nova_placa} adicionada com sucesso."

while True:
    entrada = input("Digite uma placa para adicioná-la: (LLLNLNN) ou (LLLNNNN) ou digite 'S' para encerrar. \n").strip().upper()
    
    entrada = entrada.replace("-", "")

    if entrada == 'S':
        print("Encerrando...")
        break

    print(registrar_verificar_placas(placas_no_patio, entrada))

print(f"Resumo de placas ativas: {placas_no_patio}")