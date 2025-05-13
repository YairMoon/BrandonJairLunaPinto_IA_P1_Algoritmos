import speech_recognition as sr
# Importamos la biblioteca SpeechRecognition para realizar el reconocimiento de voz.

# Crear un objeto reconocedor
recognizer = sr.Recognizer()
# Creamos una instancia de la clase Recognizer para manejar el reconocimiento de voz.

# Utilizar el micrófono como fuente de entrada
with sr.Microphone() as source:
    print("🎙️ Habla algo, estoy escuchando...")
    # Indicamos al usuario que puede comenzar a hablar.

    # Ajustar el ruido ambiental
    recognizer.adjust_for_ambient_noise(source)
    # Ajustamos el reconocimiento para reducir el impacto del ruido ambiental.

    # Capturar audio del micrófono
    audio = recognizer.listen(source)
    # Escuchamos y capturamos el audio desde el micrófono.

    print("🔎 Procesando audio...")
    # Indicamos que el audio está siendo procesado.

    try:
        # Reconocer el texto usando el servicio de Google
        texto = recognizer.recognize_google(audio, language='es-MX')
        # Usamos el servicio de Google para convertir el audio en texto en español (es-MX).

        print(f"✅ Lo que dijiste fue: {texto}")
        # Mostramos el texto reconocido.

    except sr.UnknownValueError:
        print("❌ No se entendió el audio.")
        # Mostramos un mensaje si no se pudo entender el audio.

    except sr.RequestError as e:
        print(f"⚠️ No se pudo acceder al servicio de reconocimiento de voz; error: {e}")
        # Mostramos un mensaje si hubo un problema al acceder al servicio de Google.