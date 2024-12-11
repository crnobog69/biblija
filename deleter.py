from pathlib import Path

# Putanja do glavnog direktorijuma
direktorijum = Path(".")

# Pretraga svih HTML datoteka u glavnom direktorijumu i poddirektorijumima
html_datoteke = direktorijum.rglob("*.htm")

# Obriši svaku HTML datoteku
for datoteka in html_datoteke:
    try:
        datoteka.unlink()  # Briše datoteku
        print(f"Обрисана датотека: {datoteka}")
    except Exception as e:
        print(f"Дошло је до грешке приликом брисања датотеке: {datoteka}: {e}")
