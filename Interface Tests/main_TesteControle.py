# Teste de controle: captura informacoes e exibe grafico de niveis da PulseAudio x comandos capturados x formato esperado

import ModMixer as mm
import numpy as np
import pulsectl
import matplotlib.pyplot as plt

pulse = pulsectl.Pulse("user")


def CapturaSinal_Volume():
    volumes = []
    sinal = modmixer.TESTE_info.Sinais_Recebidos
    if sinal:
        try:
            tipo, fonte, volume0 = sinal[0]
            tipo, fonte, volume1 = sinal[1]

        except:
            volume0 = 0
            volume1 = 0

        volumes.append(float(volume0))
        volumes.append(float(volume1))
    else:
        volumes = [0, 0]
    return volumes


def CapturaVolumePulseaudio():
    volumes = []
    sinks = pulse.sink_input_list()
    for fonte in sinks:
        volumes.append(fonte.volume.value_flat)

    if not volumes:
        volumes.append(0)

    return volumes


modmixer = mm.ModMixer()
modmixer.TESTE_setup()

sinal_volume = []
niveis_volume = []

while True:
    isExit = modmixer.TESTE_loop_step()
    if isExit:
        break

    sinal = CapturaSinal_Volume()
    nivel = CapturaVolumePulseaudio()
    sinal_volume.append(sinal)
    niveis_volume.append(nivel)

modmixer.TESTE_encerra()

sinal_volume0 = list(list(zip(*sinal_volume))[0])
sinal_volume1 = list(list(zip(*sinal_volume))[1])
nivel_volume0 = list(list(zip(*niveis_volume))[0])
nivel_volume1 = list(list(zip(*niveis_volume))[1])

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(sinal_volume0)
ax1.plot(nivel_volume0)

ax2.plot(sinal_volume1)
ax2.plot(nivel_volume1)

plt.show()
