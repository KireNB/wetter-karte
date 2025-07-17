![Wetter Icon](https://img.icons8.com/emoji/48/sun-behind-cloud.png)  
# WetterVorhersage Web App 📍🌤️

Eine simple, interaktive Webanwendung, die dir basierend auf deinem Standort die **aktuellen Wetterdaten** sowie eine **3-Tage-Vorhersage** anzeigt. 🌍📅

---

## 🚀 Funktionen

- 🌡️ **Tages-Max/Min/Ø Temperatur**  
- 📍 **Geolokalisierung (Lat/Lon)** Eingabe durch Nutzer  
- ⏪ **Wetterdaten der letzten 7 Tage** (Vergleichswerte)  
- ⚡ API-Anbindung an [Open-Meteo.com](https://open-meteo.com/)  
- 📊 Übersichtliches UI mit Datenvisualisierung (Frontend: HTML + JS)

---

## 🛠️ Installation & Nutzung

```bash
# 1. Repo klonen
git clone <REPO-URL>
cd wetter_proj

# 2. Python-Umgebung vorbereiten
python3 -m venv venv
source venv/bin/activate

# 3. Abhängigkeiten installieren
pip install -r requirements.txt

# 4. App starten
python main.py
