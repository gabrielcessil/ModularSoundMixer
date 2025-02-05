from numpy import character
import serial
import serial.tools.list_ports
import time
import sys

# 576000
class ColetorUSB:
    def __init__(self, BaudRate=576000, Timeout=1, Port=0):
        self.bundrate = BaudRate
        self.timeout = Timeout

        self.myPort = serial.Serial(
            timeout=Timeout,
            baudrate=BaudRate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
        )

        self.timestampEnvio = time.time()

    def close(self):
        try:

            self.myPort.flushInput()
            self.myPort.flushOutput()

            while self.myPort.isOpen():
                time.sleep(0.1)
                self.myPort.close()
        except:
            time.sleep(0.5)

    def ProcuraPortaMixer(self):
        ports = serial.tools.list_ports.comports()
        if not ports:
            return []
        return ports[0]

    def EstabeleceConexao(self):
        port = self.ProcuraPortaMixer()
        ehAberta = self.AbrePorta(port)
        return ehAberta

    def AbrePorta(self, port):
        if not port:
            return False
        else:
            try:
                self.myPort.port = str(port.device)
                if not self.myPort.isOpen():
                    try:
                        time.sleep(0.022)
                        self.myPort.open()
                        self.myPort.reset_input_buffer()
                        time.sleep(0.1)
                    except:
                        return False

            except:
                return False

            if self.myPort.isOpen():
                print("DEBUG: porta aberta")
                return True
            else:
                return False

    def GetPortsList(self):
        ports = list(serial.tools.list_ports.comports())

        portsList = []
        for port in sorted(ports):
            portsList.append(port.device)

        return portsList

    def FormataMensagem(self, mensagem):
        try:
            mensagem = mensagem.decode("utf-8")
            mensagemFormatada = str(mensagem)
        except:
            mensagemFormatada = str(mensagem)
            mensagemFormatada = mensagemFormatada.replace("\\", "")
            mensagemFormatada = mensagemFormatada.replace("n", "")
            mensagemFormatada = mensagemFormatada.replace("b", "")
            mensagemFormatada = mensagemFormatada.replace("r", "")
            mensagemFormatada = mensagemFormatada.replace("'", "")

        mensagemFormatada = mensagemFormatada.split()

        return mensagemFormatada

    # Se receber uma lista vazia
    def EhParada(self, entradaFormatada):
        if entradaFormatada:
            if entradaFormatada[0] == "stop":
                return True
            else:
                return False
        else:
            return True

    def EhMensagemValida(self, mensagem_formatada):
        if self.EhParada(mensagem_formatada):
            return True

        if len(mensagem_formatada) != 3:
            return False

        comando, fonte_index, volume = mensagem_formatada

        try:
            str(comando)
            float(volume)
            int(fonte_index)
        except ValueError:
            return False
        return True

    def LeLinhaEntrada(self):
        try:
            entrada = self.myPort.read_until(expected=b"\r\n", size=20)

            return entrada
        except Exception as var:

            exc_type, value, traceback = sys.exc_info()
            return ""

    def CapturaComando(self, maxEntradas):
        entradasFormatadas = []

        if self.myPort.isOpen():
            try:
                self.myPort.write(b"\r\n")
                self.myPort.flush()
                time.sleep(0.001)
                for i in range(maxEntradas):
                    try:
                        entrada = self.LeLinhaEntrada()
                        entradaFormatada = self.FormataMensagem(entrada)
                        print("DEBUG: ", entradaFormatada)
                        if not self.EhMensagemValida(entradaFormatada):
                            break
                        if self.EhParada(entradaFormatada):
                            break
                        entradasFormatadas.append(entradaFormatada)

                    except Exception:
                        exc_type, value, traceback = sys.exc_info()
                        entradasFormatadas = []
                        break
            except Exception:
                exc_type, value, traceback = sys.exc_info()
                entradasFormatadas = []

        nMixers = len(entradasFormatadas)
        return [entradasFormatadas, nMixers]
