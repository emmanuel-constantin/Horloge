import time
import threading

class Horloge:
    def __init__(self, heure_initiale):
        self.heure_debut = time.time()
        self.heure_initiale = heure_initiale
        self.alarme = None
        self.alarme_activee = False

    def afficher_heure(self, heure_tuple):
        self.heure_initiale = heure_tuple
        self.heure_debut = time.time()

    def regler_alarme(self, heure_alarme):
        self.alarme = heure_alarme
        self.alarme_activee = True

    def verifier_alarme(self):
        if self.alarme_activee:
            heure_actuelle = (self.heure_actuelle.tm_hour, self.heure_actuelle.tm_min, self.heure_actuelle.tm_sec)
            if heure_actuelle == self.alarme:
                print("L'alarme sonne !")
                self.alarme_activee = False

    def actualiser_heure(self):
        while True:
            time.sleep(1)
            temps_ecoule = time.time() - self.heure_debut
            heure_base = time.struct_time((1970, 1, 1, self.heure_initiale[0], self.heure_initiale[1], self.heure_initiale[2], 0, 0, 0))
            timestamp = time.mktime(heure_base) + temps_ecoule
            self.heure_actuelle = time.localtime(timestamp)
            self.verifier_alarme()
            print(f"{self.heure_actuelle.tm_hour:02d}:{self.heure_actuelle.tm_min:02d}:{self.heure_actuelle.tm_sec:02d}")

heure_initiale = (16, 30, 0)
horloge = Horloge(heure_initiale)
thread = threading.Thread(target=horloge.actualiser_heure)
thread.daemon = True
thread.start()

horloge.regler_alarme((16, 30, 10))

# Le programme continuera de s'exécuter jusqu'à ce qu'il soit interrompu manuellement.
while True:
    time.sleep(1)
