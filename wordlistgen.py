import itertools
import string
import argparse
import os

def generate_wordlist(
    min_length=8,
    max_length=8,
    charset="abcdefghijklmnopqrstuvwxyz0123456789",
    output="wifite3_wordlist.txt",
    limit=1000000
):
    """
    Génère une wordlist de passwords en bruteforce, sauvegardée dans un fichier.

    :param min_length: longueur minimale des mots de passe générés
    :param max_length: longueur maximale des mots de passe générés
    :param charset: caractères utilisables
    :param output: fichier de sortie
    :param limit: nombre maximum de mots à générer (pour éviter les trop gros fichiers)
    """
    count = 0
    with open(output, "w") as f:
        for length in range(min_length, max_length+1):
            for pw_tuple in itertools.product(charset, repeat=length):
                word = "".join(pw_tuple)
                f.write(word + "\n")
                count += 1
                if limit and count >= limit:
                    print(f"Limite atteinte ({limit} mots). Arrêt.")
                    return
    print(f"Wordlist générée : {output} ({count} mots)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wifite3 - Générateur de wordlist custom")
    parser.add_argument("--min", type=int, default=8, help="Longueur minimale (default: 8)")
    parser.add_argument("--max", type=int, default=8, help="Longueur maximale (default: 8)")
    parser.add_argument("--charset", type=str, default="abcdefghijklmnopqrstuvwxyz0123456789", help="Caractères (default: lettres minuscules et chiffres)")
    parser.add_argument("--output", type=str, default="wifite3_wordlist.txt", help="Fichier de sortie")
    parser.add_argument("--limit", type=int, default=1000000, help="Nombre max de mots (default: 1 million)")
    args = parser.parse_args()

    if os.path.exists(args.output):
        print(f"Le fichier {args.output} existe déjà, il sera écrasé.")

    generate_wordlist(
        min_length=args.min,
        max_length=args.max,
        charset=args.charset,
        output=args.output,
        limit=args.limit
    )