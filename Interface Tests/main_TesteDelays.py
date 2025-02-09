import ModMixer as mm
import numpy as np

delayIniciar = []
media_delayResposta = []

for i in range(10):
    modmixer = mm.ModMixer()
    modmixer.TESTE_setup()

    while True:
        isExit = modmixer.TESTE_loop_step()
        if isExit or modmixer.TESTE_info.iteracao == 1000:
            break

    modmixer.TESTE_encerra()

    delayIniciar.append(
        modmixer.TESTE_info.timeStamp_PrimeiraInteracao
        - modmixer.TESTE_info.timeStamp_Inicializacao
    )
    media_delayResposta.append(
        np.mean(
            np.array(modmixer.TESTE_info.timeStamp_MudancasVolume)
            - np.array(modmixer.TESTE_info.timeStamp_LeiturasUSB)
        )
    )

media_delayInicial = np.mean(np.array(delayIniciar))
media_geral_delayResposta = np.mean(np.array(media_delayResposta))


print(
    "Tempo entre a criacao do objeto e a primeira leitura de janela: ",
    media_delayInicial,
)
print(
    "Tempo medio geral entre um sinal de mudanca de volume e sua atuacao(chamada PulseAudio): ",
    media_geral_delayResposta,
)
