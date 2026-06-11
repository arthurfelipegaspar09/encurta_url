import pyshorteners


url = input("Digite uma URL para encurtar: ")


encurtador = pyshorteners.Shortener()

url_curta = encurtador.tinyurl.short(url)


print(f"Link original: {url}")

print(f"Link encurtado: {url_curta}")