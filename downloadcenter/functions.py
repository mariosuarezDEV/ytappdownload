import os
import yt_dlp


# Funcion para descargar la musica
def download_file(url, nombre_archivo="music"):
    try:
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        # Limpiar extensión si viene incluida
        if nombre_archivo.endswith(".mp3"):
            nombre_archivo = nombre_archivo[:-4]

        output_path = f"downloads/{nombre_archivo}.mp3"

        # Validar que el archivo no exista
        if os.path.exists(output_path):
            print("El archivo ya existe.")
            return False

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"/media/audio/{nombre_archivo}.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "quiet": False,
            "no_warnings": False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Descarga completada.")
        return True

    except Exception as e:
        print(f"Error en la descarga: {str(e)}")
        return False
