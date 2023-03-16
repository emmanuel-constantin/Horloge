import time

# Fonction pour afficher l'heure actuelle
def afficher_heure(heures, minutes, secondes):
    print(f"\r{heures:02}:{minutes:02}:{secondes:02}", end="", flush=True)

# Demande à l'utilisateur de rentrer l'heure souhaitée
heure_demandee = input("Entrez l'heure souhaitée (format hh:mm:ss) : ")
heures, minutes, secondes = map(int, heure_demandee.split(':'))

# Demande à l'utilisateur de programmer une alarme
programmer_alarme = input("Voulez-vous programmer une alarme ? (o/n) : ")
if programmer_alarme.lower() == "o":
    heure_alarme = input("Entrez l'heure de l'alarme (format hh:mm:ss) : ")
    heure_alarme = tuple(map(int, heure_alarme.split(':')))
    alarme_programmee = True
else:
    alarme_programmee = False

# Boucle pour actualiser l'heure demandée toutes les secondes
while True:
    afficher_heure(heures, minutes, secondes)
    time.sleep(1)
    secondes += 1
    if secondes == 60:
        secondes = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        heures += 1
    if heures == 24:
        heures = 0

    # Vérification si l'heure actuelle correspond à l'heure demandée
    heure_actuelle = time.localtime()
    if heure_actuelle.tm_hour == heures and heure_actuelle.tm_min == minutes and heure_actuelle.tm_sec == secondes:
        print("\nHeure demandée atteinte !")

    # Vérification si l'heure actuelle correspond à l'heure de l'alarme programmée
    if alarme_programmee and heure_actuelle.tm_hour == heure_alarme[0] and heure_actuelle.tm_min == heure_alarme[1] and heure_actuelle.tm_sec == heure_alarme[2]:
        print("\nAlarme !")
        break
