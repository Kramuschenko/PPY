import webbrowser
import requests

if __name__ == '__main__':
    print("hello world")
    url1 = input("Podaj stronę internetową: ")

    for x in range(3):
        date = input("podaj {} date: ".format(x+1))
        url = "http://archive.org/wayback/available?url=" + url1 + "&timestamp=" + str(date)
        response = requests.get(url)
        d = response.json()
        page = d["archived_snapshots"]["closest"]["url"]
        webbrowser.open(page)