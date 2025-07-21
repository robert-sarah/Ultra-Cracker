import argparse
from wifite3.banner import WIFITE3_BANNER
from wifite3.core import Wifite3Core

def main():
    print(WIFITE3_BANNER)
    parser = argparse.ArgumentParser(
        description="Wifite3: All-in-one, extensible and automated WiFi pentest suite"
    )
    parser.add_argument("-i", "--interface", help="Interface WiFi à utiliser (ex: wlan0)")
    parser.add_argument("-m", "--mode", choices=[
        "scan", "handshake", "pmkid", "wps", "eviltwin", "brute", "crack", "auto", "analyze"
    ], default="scan", help="Mode d'action")
    parser.add_argument("-t", "--threads", type=int, default=4, help="Threads max pour attaques")
    parser.add_argument("-w", "--wordlist", help="Wordlist (pour WPA/PMKID etc)")
    parser.add_argument("--ai", action="store_true", help="Active l'analyse auto/AI")
    parser.add_argument("--plugins", nargs='*', help="Plugins à charger")
    parser.add_argument("--logfile", type=str, default="wifite3.log", help="Fichier de log")
    parser.add_argument("--output", type=str, default="results/", help="Dossier de résultats")
    parser.add_argument("--cleanup", action="store_true", help="Nettoie tous les fichiers temporaires")
    parser.add_argument("--all", action="store_true", help="Tout attaquer automatiquement")
    parser.add_argument("--target", type=str, help="BSSID/ESSID cible directe")
    parser.add_argument("--auto", action="store_true", help="Attaque automatisée après scan")
    parser.add_argument("--no-interact", action="store_true", help="Tout en mode non-interactif")
    args = parser.parse_args()
    w3 = Wifite3Core(args)
    w3.run()