def calcular_promedio_ponderado(notas_creditos):
    suma_productos = 0
    total_creditos = 0

    for nota, creditos in notas_creditos:
        suma_productos += nota * creditos
        total_creditos += creditos

    if total_creditos == 0:
        return 0  # Evita la división por cero si no se ingresaron créditos

    promedio_ponderado = suma_productos / total_creditos
    return promedio_ponderado

