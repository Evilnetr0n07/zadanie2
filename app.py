from flask import Flask, render_template, request
import datetime
import os

AUTHOR = "Marek Zając"
PORT = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

#Dane pogodowe
weather_data = {
    "Warszawa": {"temp": 18, "desc": "Słonecznie", "humidity": 50, "wind": 3},
    "Krakow": {"temp": 16, "desc": "Pochmurno", "humidity": 60, "wind": 2},
    "Gdansk": {"temp": 14, "desc": "Deszcz", "humidity": 70, "wind": 5},
    "Berlin": {"temp": 17, "desc": "Słonecznie", "humidity": 55, "wind": 3},
    "Munich": {"temp": 15, "desc": "Zachmurzenie umiarkowane", "humidity": 65, "wind": 4},
    "Hamburg": {"temp": 13, "desc": "Deszcz", "humidity": 75, "wind": 6},
    "Nowy York": {"temp": 20, "desc": "Ciepło", "humidity": 55, "wind": 5},
    "Los Angeles": {"temp": 25, "desc": "Gorąco", "humidity": 40, "wind": 2},
    "Chicago": {"temp": 10, "desc": "Wietrznie", "humidity": 65, "wind": 7}
}

#Lista lokalizacji
locations = {
    "Polska": ["Warszawa", "Krakow", "Gdansk"],
    "Niemcy": ["Berlin", "Munich", "Hamburg"],
    "USA": ["Nowy York", "Los Angeles", "Chicago"]
}

#definicja ścieżki zwracającej szablon z danymi
@app.route("/", methods=["GET", "POST"])
def index():
    selected_country = list(locations.keys())[0]
    selected_city = locations[selected_country][0]
    data = None

    if request.method == "POST":
        selected_country = request.form.get("country")
        selected_city = request.form.get("city")
        data = weather_data.get(selected_city)

    return render_template("index.html",
                           locations=locations,
                           selected_country=selected_country,
                           selected_city=selected_city,
                           weather=data)

#sprawdzenie czy aplikacja nie jest modułem
if __name__ == "__main__":
    #wyświetlenie w logach date, autora i port
    log_message = f"Data uruchomienia: {datetime.datetime.now()}, Autor: {AUTHOR}, Nasłuchuje na porcie: {PORT}"
    print(log_message)
    #uruchimienie aplikacji na porcie zawartym w zmiennej PORT
    app.run(host="0.0.0.0", port=PORT)

