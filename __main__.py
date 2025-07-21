import sys
from wifite3.cli import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[red]Interruption utilisateur, arrêt propre de Wifite3.[/red]")
        sys.exit(0)