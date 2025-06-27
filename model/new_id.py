def new_id(lista_registros):
    if not isinstance(lista_registros, list):
        raise TypeError("Se esperaba una lista de diccionarios")

    ids_utilizados = set()

    for registro in lista_registros:
        if isinstance(registro, dict):
            id_valor = registro.get("id")
            if isinstance(id_valor, int) and id_valor > 0:
                ids_utilizados.add(id_valor)

    if not ids_utilizados:
        return 1

    # Buscar el menor ID libre, desde 1 en adelante
    for candidato_id in range(1, max(ids_utilizados) + 2):
        if candidato_id not in ids_utilizados:
            return candidato_id