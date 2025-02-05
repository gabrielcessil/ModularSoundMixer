# Teste de selecao: verificar se app selecionado na tela eh o mesmo que esta alterando som

# Primeiro teste: se a lista de apps selecionados esta contida na de fontes emitindo som.
# Ou seja, apenas podemos selecionar apps que sao fontes de som

# Segundo teste: mantem um volume sendo alterado constantemente, e os demais estaticos.
# o a fonte de som que mudar entre uma iteracao e outra deve ser igual ao aplicativo
# selecionado na interface

import ModMixer as mm
import pulsectl

modmixer = mm.ModMixer()
modmixer.TESTE_setup()
pulse = pulsectl.Pulse("user")


def GetFontesNames():
    names = []
    sink_inputs = pulse.sink_input_list()
    for sink in sink_inputs:
        names.append(sink.proplist["application.name"])

    return names


def Teste_Restricao(sinks_name, apps_name):
    # Se ha apps selecionados
    if apps_name:
        if all(elem in sinks_name for elem in apps_name):
            return True
        else:
            return False
    # Se nao teste eh considerado verdadeiro
    else:
        return True


class Teste_AppMudouVolume:
    def __init__(self):
        self.oldVolume = []
        self.oldName = []

    def run(self, appSelecionado):
        if appSelecionado:
            appSelecionadoMudouVolume = False
            # Captura informacao atual sobre as fontes de som
            newVolume = []
            newName = []
            for fonte in pulse.sink_input_list():
                newVolume.append(fonte.volume.value_flat)
                newName.append(fonte.proplist["application.name"])

            # Se existe volume anterior
            if self.oldVolume:

                # Para cada fonte de som
                for new_vol, new_name, old_vol, old_name in zip(
                    newVolume, newName, self.oldVolume, self.oldName
                ):
                    # Se a ordenacao da PulseAudio se manteve o teste pode ser feito
                    if new_name == old_name:
                        # Se mudou de volume
                        if new_vol != old_vol:
                            # Se o app que mudou de volume eh o mesmo um selecionado na interface
                            if all(elem in appSelecionado for elem in [new_name]):
                                appSelecionadoMudouVolume = True
                        # Se nao eh considerada como verdadeiro
                        else:
                            appSelecionadoMudouVolume = True

                    # Se nao eh considerada como verdadeiro
                    else:
                        appSelecionadoMudouVolume = True
            # Se nao eh considerada como verdadeiro
            else:
                appSelecionadoMudouVolume = True

            self.oldVolume = newVolume
            self.oldName = newName

            return appSelecionadoMudouVolume
        else:
            return True


testeEnglobamento_count_success = 0
testeMudouVolume_count_sucess = 0
teste_count = 0
Teste_MudancaVolume = Teste_AppMudouVolume()
while True:
    isExit = modmixer.TESTE_loop_step()
    if isExit:
        break

    appsList = modmixer.TESTE_info.appsName
    sinks_names = GetFontesNames()

    teste_count += 1
    if Teste_Restricao(sinks_names, appsList):
        testeEnglobamento_count_success += 1

    if Teste_MudancaVolume.run(appsList):
        testeMudouVolume_count_sucess += 1

print("Teste de restricao: ", testeEnglobamento_count_success, "/", teste_count)
print(
    "Teste de selecao de aplicativo: ", testeMudouVolume_count_sucess, "/", teste_count
)

modmixer.TESTE_encerra()
