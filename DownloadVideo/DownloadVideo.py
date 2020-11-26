
import webbrowser
import time

print("Você será direcionado para uma página de download de vídeo")

time.sleep(2.0)

urlvideo= input("Informe a url do Youtube: ")
urlvideo = urlvideo[:12]+'ss'+urlvideo[12:]
webbrowser.open(urlvideo)