import os
import subprocess
import platform

def abrir_url_en_perfiles(url, perfiles, ruta_chrome=None):
    """
    Abre una URL en diferentes perfiles de Chrome.
    
    :param url: URL a abrir.
    :param perfiles: Lista de nombres de perfiles de Chrome.
    :param ruta_chrome: Ruta al ejecutable de Chrome (opcional, se usa la predeterminada si es None).
    """
    sistema_operativo = platform.system()
    
    if ruta_chrome is None:
        if sistema_operativo == "Windows":
            ruta_chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        elif sistema_operativo == "Darwin":  # macOS
            ruta_chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        else:  # Linux
            ruta_chrome = "/usr/bin/google-chrome"
    
    if not os.path.exists(ruta_chrome):
        print(f"No se encontró Chrome en la ruta especificada: {ruta_chrome}")
        return
    
    for perfil in perfiles:
        comando = [
            ruta_chrome,
            f"--profile-directory={perfil}",
            url
        ]
        try:
            subprocess.Popen(comando)
            print(f"Abriendo URL en perfil: {perfil}")
        except Exception as e:
            print(f"Error al abrir el perfil {perfil}: {e}")

# Configuración
url_a_abrir = "https://www.ticketmaster.cl/event/stray-kids-dominate-world-tour-2025"
perfiles_chrome = []

for i in range(1, 12):
    perfiles_chrome.append(f"Profile {i}")

abrir_url_en_perfiles(url_a_abrir, perfiles_chrome)
