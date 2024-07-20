import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import threading
#pip install sounddevice scipy

SAMPLING_RATE = 44100  # Taxa de amostragem do áudio
CHANNELS = 1  # Gravação mono

# Variáveis globais para controle da gravação
global recording, frames
recording = False
framess = []

def audio_callback(indata, frames, time, status):
    """Callback para captura de áudio."""
    global recording, framess
    if recording:
        for n in indata.copy():
            
            if n[0]>0.0035:
                print("->"+str(n[0]))

def start_recording():
    global recording, framess
    framess = []
    recording = True
    with sd.InputStream(samplerate=SAMPLING_RATE, channels=CHANNELS, callback=audio_callback):
        print("press a key to exit.")
        input()  # Aguarda o usuário pressionar Enter para parar a gravação

        recording = False


def main():
    global recording, framess
    # Nome do arquivo para salvar a gravação
    output_filename =""
    
    # Iniciar a gravação em um thread separado para permitir a interrupção com Enter
    recording_thread = threading.Thread(target=start_recording)
    recording_thread.start()
    recording_thread.join()  # Aguarda a gravação terminar
    
    
    
    
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()

