import tkinter as tk
import pyautogui
import time
import threading

running = False  # Variable pour contrôler l'état de l'autoclicker
nb_clics = 0  # Compteur de clics

def auto_clicker():
    """
    La fonction démarre l'auto clicker qui clique à la position actuelle du curseur toutes les secondes.
    @param : Aucun
    @return : Aucun
    """
    global running, nb_clics # On utilise la variable globale
    if running:
        return
    running = True
    nb_clics = 0
    
    print("L'autoclicker va démarrer dans 3 secondes. Placez votre curseur à l'endroit souhaité.")
    fenetre.after(3000, launch_clicks)  # Attendre 3 secondes avant de démarrer
    
def launch_clicks():
    global running, nb_clics
    x, y = pyautogui.position()  # Obtenir la position actuelle du curseur
    print(f"Autoclicker démarré à la position ({x}, {y}).")
    click_once()
    
def click_once():
    global running, nb_clics
    if running:
        pyautogui.click()  # Effectuer un clic
        nb_clics += 1
        label_nb_clics.config(text=f"Nombre de clics effectués : {nb_clics}")
        interval_ms = int(speed_scale.get())
        fenetre.after(interval_ms, click_once)  # Replanifier le clic après x seconde
    

def start_thread():
    thread = threading.Thread(target=auto_clicker)
    thread.daemon = True
    thread.start()

def stop_auto_clicker():
    """
    La fonction arrête l'auto clicker.
    @param : Aucun
    @return : Aucun
    """
    global running
    running = False
    print("L'autoclicker a été arrêté.")

fenetre = tk.Tk()
fenetre.title("Autoclicker Simple")
fenetre.geometry("300x200")
fenetre.attributes("-topmost", True) # Toujours au premier plan

frame_gauche = tk.Frame(fenetre)
frame_gauche.pack(side="left", fill="y", padx=10, pady=10)

tk.Label(frame_gauche, text="Vitesse\n(ms)", justify="center").pack()
speed_scale = tk.Scale(frame_gauche, from_=1000, to=50, orient="vertical")  # inversé : haut = lent
speed_scale.set(500)
speed_scale.pack(fill="y")

frame_droite = tk.Frame(fenetre)
frame_droite.pack(side="right", expand=True, fill="both")

bouton_demarrer = tk.Button(frame_droite, text="Démarrer l'autoclicker", command=auto_clicker)
bouton_demarrer.pack(pady=10)

bouton_stopper = tk.Button(frame_droite, text="Arrêter l'autoclicker", command=stop_auto_clicker)
bouton_stopper.pack(pady=10)

label_nb_clics = tk.Label(frame_droite, text=f"Nombre de clics effectués : {nb_clics}")
label_nb_clics.pack(pady=10)

fenetre.mainloop()