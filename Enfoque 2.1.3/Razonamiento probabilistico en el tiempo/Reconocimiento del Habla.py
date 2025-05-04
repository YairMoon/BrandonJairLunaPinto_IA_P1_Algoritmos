import speech_recognition as sr

# Crear un objeto reconocedor
recognizer = sr.Recognizer()

# Utilizar el micrófono como fuente de entrada
with sr.Microphone() as source:
    print("🎙️ Habla algo, estoy escuchando...")

    # Ajustar el ruido ambiental
    recognizer.adjust_for_ambient_noise(source)

    # Capturar audio del micrófono
    audio = recognizer.listen(source)

    print("🔎 Procesando audio...")

    try:
        # Reconocer el texto usando el servicio de Google
        texto = recognizer.recognize_google(audio, language='es-MX')
        print(f"✅ Lo que dijiste fue: {texto}")

    except sr.UnknownValueError:
        print("❌ No se entendió el audio.")
    except sr.RequestError as e:
        print(f"⚠️ No se pudo acceder al servicio de reconocimiento de voz; error: {e}")
