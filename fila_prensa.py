fila_prensa = ["Caminhão 7", "Caminhão 2", "Caminhão 5"]

print("\nMenu de Comandos")
print("Digite 'A' para adicionar um caminhão à fila.")
print("Digite 'R' para remover um caminhão da fila.")
print("Digite 'S' para sair.")

def adicionar_caminhao(caminhao: str):
    if caminhao.startswith("Caminhão"):
            fila_prensa.append(caminhao)
            print(f"Caminhão adicionado à fila: {caminhao}")

def remover_caminhao():
    caminhao_retirado = fila_prensa.pop(0)
    print(f"Caminhão retirado: {caminhao_retirado}")

while True:
    comando = input("Comando: ").strip()
    if comando.lower() == 's':
        print("Encerrando...")
        break

    elif comando.lower() == 'a':
        caminhao = input("Qual caminhão deseja adicionar? (Formato: Caminhão + Número) \n").capitalize()
        adicionar_caminhao(caminhao)

    elif comando.lower() == 'r':
        remover_caminhao()

    else:
        print("O comando não existe. Tente novamente.")