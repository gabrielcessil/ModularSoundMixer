# Teste de comandos: arduino lanca sequencia conhecida ([A->Z],[0.0->1.0]), usb captura e compara com o esperado
# Assim sabemos que nossa captura de letras e valores esta correta para esse range de valores
import ModMixer as mm
import numpy as np
import string
import collections


def cria_esperado():

    vol_esperado = np.around(np.arange(0, 1, 0.01), 2).tolist()
    letras = list(string.ascii_uppercase)
    i = 0
    comando_esperado = []
    for vol in vol_esperado:
        comando_esperado.append([letras[i], "0", str(round(vol, 2))])
        i += 1
        if letras[i] == "Z":
            i = 0
    return comando_esperado


def cria_identificado():

    comando_identificado = []
    modmixer = mm.ModMixer()
    modmixer.TESTE_setup()
    start = False
    while True:
        isExit = modmixer.TESTE_loop_step()
        if isExit:
            return comando_identificado
        sinal = modmixer.TESTE_info.Sinais_Recebidos

        if sinal:
            start_input = ["A", "0", "0.00"]
            if collections.Counter(sinal[0]) == collections.Counter(start_input):
                start = True
            if start:
                comando_identificado.append(sinal[0])
            if sinal[0] == ["Y", "0", "0.99"] and start:
                modmixer.TESTE_encerra()
                return comando_identificado


esperado = cria_esperado()
identificado = cria_identificado()

total_itens_esperados = len(esperado)
total_itens_identificados = len(identificado)

itens_corretos = 0
for item_esperado, item_identificado in zip(esperado, identificado):

    item_esperado = [item_esperado[0]] + [float(item) for item in item_esperado[1:2]]
    item_identificado = [item_identificado[0]] + [
        float(item) for item in item_identificado[1:2]
    ]

    if item_esperado == item_identificado:
        itens_corretos += 1

print("Teste de numero de itens identificados: ", len(identificado), "/", len(esperado))
print(
    "Teste de identificacao correta: ", itens_corretos, "/", total_itens_identificados
)
