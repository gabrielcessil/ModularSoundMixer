import PySimpleGUI as psg


class GUI:
    def __init__(self, maxModulos=9, guiRefreshTimeout=0.001):
        self.janelaAberta = False
        self.refreshTimeoutTime = guiRefreshTimeout
        self.NumeroMaximoModulos = maxModulos
        self.modules = ModulesCollection()
        self.appsName = []

        self.dicEstadosJanela = {
            "None": 0,
            "Iniciando": 1,
            "Ativado": 2,
            "Desativado": 3,
        }
        self.estadoJanela = self.dicEstadosJanela["None"]
        self.PortaConectada = False

    def SetPortaConectada(self, estado):
        self.PortaConectada = estado

    def getNomeAplicacao(self, moduleIndex):
        return self.modules.GetNomeFonte(moduleIndex)

    def setEstadoLayout(self, estado):
        self.estadoJanela = estado

    def IdentificaEstadoJanela(self):
        if self.modules.GetNumeroModulos() < 0:
            return self.dicEstadosJanela["Iniciando"]
        elif self.modules.GetNumeroModulos() == 0 or self.PortaConectada == False:
            return self.dicEstadosJanela["Desativado"]
        else:
            return self.dicEstadosJanela["Ativado"]

    def getNumeroModulos(self):
        return self.modules.GetNumeroModulos()

    def AtualizaNumeroModulos(self, nModules):
        self.modules.AtualizaNumeroModulos(nModules)

    def AtualizaNomeAplicativos(self, mixer):
        self.appsName = mixer.GetNomeFontes()

    def GetAppsName(self):
        return self.appsName

    def setVisibles(self):
        # Verifica todos os possiveis modulos
        for index in range(self.NumeroMaximoModulos):
            # Os indices 0 - Nmodulos sao visiveis
            if index < self.getNumeroModulos():
                isVisible = True
            else:
                isVisible = False

            self.win["volumeBar" + str(index)].Update(visible=isVisible)
            self.win["apps_List" + str(index)].Update(visible=isVisible)
            self.win["mixer_line" + str(index)].Update(visible=isVisible)

    def CreateLayoutMixerAtivado(self):

        layout = []

        title_line = psg.Text(
            "Selecione as aplicações", font="ArialBaltic 15", justification="center"
        )
        layout.append([title_line])

        # Gera menu para cada possivel mixer
        nomes_app = self.GetAppsName()
        nomes_app.append("none")
        for index in range(self.NumeroMaximoModulos):
            mixer_line = psg.Text(
                "Mixer (" + str(index) + ")",
                key="mixer_line" + str(index),
                font="ArialBaltic 15",
                justification="left",
                visible=False,
            )

            layout.append(
                [
                    psg.Combo(nomes_app, key="apps_List" + str(index), visible=False),
                    mixer_line,
                ]
            )

            layout.append(
                [
                    psg.ProgressBar(
                        max_value=1,
                        orientation="h",
                        bar_color=("green", "grey"),
                        style="vista",
                        size=(22, 5),
                        key="volumeBar" + str(index),
                        visible=False,
                    )
                ]
            )
        layout.append(
            [
                psg.Button("Atualizar lista", button_color=("white", "RoyalBlue4")),
                psg.Button("Aplicar", button_color=("black", "rosybrown")),
            ]
        )

        return layout

    def CreateLayoutMixerDesativado(self):
        layout = []
        mixer_line = psg.Text(
            "Por favor, conecte os módulos e aguarde",
            font="ArialBaltic 15",
            justification="center",
        )
        layout.append([mixer_line])
        return layout

    def CreateLayoutMixerIniciando(self):
        layout = []
        mixer_line = psg.Text(
            "Olá, estamos ajustando sua experiência ...",
            font="ArialBaltic 15",
            justification="center",
        )
        layout.append([mixer_line])
        return layout

    def getLayout(self, estadoJanela):
        layout = []

        if estadoJanela == self.dicEstadosJanela["Iniciando"]:
            layout = self.CreateLayoutMixerIniciando()
        elif estadoJanela == self.dicEstadosJanela["Ativado"]:
            layout = self.CreateLayoutMixerAtivado()
        else:
            layout = self.CreateLayoutMixerDesativado()

        return layout

    def ehMudancaEstado(self, novoEstadoJanela):
        if novoEstadoJanela != self.estadoJanela:
            return True
        else:
            return False

    def CriaJanela(self, novoEstadoJanela):
        if self.janelaAberta:
            self.FechaJanela()

        self.janelaAberta = True
        self.setEstadoLayout(novoEstadoJanela)
        layout = self.getLayout(novoEstadoJanela)
        self.win = psg.Window(
            "ModMixer",
            layout,
            finalize=True,
            enable_close_attempted_event=True,
            resizable=True,
        )

    def IniciaJanela(self):
        estadoJanela = self.dicEstadosJanela["Iniciando"]
        self.CriaJanela(estadoJanela)
        return estadoJanela

    def EhFechamento(self, event):
        if (
            event == psg.WINDOW_CLOSE_ATTEMPTED_EVENT
            or event == psg.WIN_CLOSED
            or event == psg.WINDOW_CLOSED
            or event == None
            or event == "none"
            or event == "_EXIT_"
            or event == "Exit"
        ):
            return True
        else:
            return False

    def AtualizaColecao(self, DicValues):
        self.modules.AtualizaColecao(DicValues)

    def FechaJanela(self):
        self.janelaAberta = False
        self.win.close()

    def LeituraDeJanela(self, timoutOn=False):
        if timoutOn:
            event, values = self.win.read(timeout=self.refreshTimeoutTime)
        else:
            event, values = self.win.read()
        return [event, values]

    # Atuliza lista exibida no menu de aplicacoes emitindo som
    def AtualizaListaApps(self):
        nomes_app = self.GetAppsName()
        nomes_app.append("none")
        for index in range(self.NumeroMaximoModulos):
            self.win["apps_List" + str(index)].Update(value="", values=nomes_app)

    def AtualizaBarrasTela(self, mixer):
        # Para cada fonte selecianada no menu:
        for module in self.modules.GetCollection():
            # Coleta o volume dessa fonte pelo seu nome
            volFonte = mixer.GetVolume(module.getAppName())
            # Atualiza a barra com esse valor de volume
            progress_bar = self.win["volumeBar" + str(module.getFisicalIndex())]
            progress_bar.UpdateBar(volFonte)

    def AtualizaInfos(self, nModules, mixer):
        # Atualiza conhecimento de numero de modulos conectados
        self.AtualizaNumeroModulos(nModules)
        # Atualiza conhecimento do nome do aplicativos fonte de som
        self.AtualizaNomeAplicativos(mixer)

    def EncerraJanela(self):
        self.win.close()

    def InteracaoComUsuario(self):
        [event, values] = self.LeituraDeJanela(timoutOn=True)

        if self.EhFechamento(event):
            return False

        elif event == "Aplicar":
            self.AtualizaColecao(values)
            return True

        elif event == "Atualizar lista":
            self.AtualizaListaApps()
            return True

        elif event == psg.TIMEOUT_KEY:
            return True
        else:
            return False

        return True

    def AtualizaVisibilidades(self, mixer):
        self.AtualizaBarrasTela(mixer)
        self.setVisibles()

    def AtualizaJanela(self):
        novoEstadoJanela = self.IdentificaEstadoJanela()
        if self.ehMudancaEstado(novoEstadoJanela):
            self.CriaJanela(novoEstadoJanela)
        return novoEstadoJanela


# Informacoes do modulo visto pela interface grafica
class Module:
    def __init__(self, appName="", fisicalIndex=-1):
        self.AppName = appName
        self.FisicalIndex = fisicalIndex

    def getAppName(self):
        return self.AppName

    def getFisicalIndex(self):
        return self.FisicalIndex

    def setAppName(self, name):
        self.appName = name

    def setFisicalIndex(self, index):
        self.FisicalIndex = index


# Gerenciamento do grupo de modulos
class ModulesCollection:
    def __init__(self):
        self.Modules = []
        self.numerModulos = 0

    def AddModulo(self, appName, fisicalIndex):
        self.Modules.append(Module(appName, fisicalIndex))

    def AtualizaColecao(self, DicValues):
        self.Modules = []
        for elem, index in zip(DicValues, range(len(DicValues))):
            self.AddModulo(DicValues[elem], index)

    def GetCollection(self):
        return self.Modules

    def GetNomeFonte(self, moduleIndex):
        for module in self.GetCollection():
            if moduleIndex == module.getFisicalIndex():
                return module.getAppName()
        return []

    def AtualizaNumeroModulos(self, nModules):
        self.numerModulos = nModules

    def GetNumeroModulos(self):
        return self.numerModulos
