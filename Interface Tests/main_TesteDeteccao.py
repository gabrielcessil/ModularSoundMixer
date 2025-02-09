import ModMixer as mm
import numpy as np

modmixer = mm.ModMixer()
modmixer.TESTE_setup()

identificado = []
visibilidades = []
start = False
esperado = list(np.arange(1, 10, 1, dtype=int))
while True:
    isExit = modmixer.TESTE_loop_step()
    if isExit:
        break

    nModulos_identificado = modmixer.TESTE_info.nModules
    if nModulos_identificado == 1:
        start = True
    if start:
        identificado.append(nModulos_identificado)
        visibilidades.append(modmixer.TESTE_info.nVisibilidades)
        if nModulos_identificado == 9:
            break

identificado = [item for item in identificado if item != 0]
visibilidades = [item for item in visibilidades if item != 0]

modmixer.TESTE_encerra()

print("Teste de deteccao, status de sucesso: ", identificado == esperado)

print("Teste de visibilidades, status de sucesso: ", visibilidades == esperado)
