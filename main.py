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

# Initialisation du temps écoulé
temps_ecoule = 0

# Boucle pour actualiser l'heure réglée toutes les secondes
while True:
    heures_actuelles = (heures + temps_ecoule // 3600) % 24
    minutes_actuelles = (minutes + (temps_ecoule // 60) % 60) % 60
    secondes_actuelles = (secondes + temps_ecoule % 60) % 60
    # Vérification si l'heure actuelle correspond à l'heure demandée
    if heures_actuelles == heures and minutes_actuelles == minutes and secondes_actuelles == secondes:
        print("\nHorloge réglée !")

    # Vérification si l'heure actuelle correspond à l'heure de l'alarme programmée
    if alarme_programmee and heures_actuelles == heure_alarme[0] and minutes_actuelles == heure_alarme[1] and secondes_actuelles == heure_alarme[2]:
        print("\nDriiiing  !!!!")
        
    afficher_heure(heures_actuelles, minutes_actuelles, secondes_actuelles)
    time.sleep(1)
    temps_ecoule += 1


