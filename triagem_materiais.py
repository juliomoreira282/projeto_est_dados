lista_materiais = ["Plástico", "Vidro", "Papel", "Metal", "Orgânico", "Plástico"]

def remover_item(item: str, list: list):
    if item not in list:
        raise ValueError("O item não está na lista.")
    
    list.remove(item)
    print(f"Material removido: {item}")
    print(f"Lista de materiais: {list}")

material_remover = "Orgânico"
remover_item(material_remover, lista_materiais)