import importlib
from wifite3.utils import log

class PluginManager:
    def __init__(self, plugins):
        self.plugins = []
        self.plugin_names = plugins or [
            "scanner", "handshake", "pmkid", "wps", "eviltwin", "brute", "crack", "analyze"
        ]

    def load_all(self):
        for name in self.plugin_names:
            try:
                mod = importlib.import_module(f"wifite3.plugins.{name}")
                self.plugins.append(mod)
                log(f"[green]Plugin {name} chargé[/green]")
            except Exception as e:
                log(f"[red]Echec chargement plugin {name}: {e}[/red]", "error")

    def hook(self, event, core):
        results = []
        for mod in self.plugins:
            if hasattr(mod, event):
                try:
                    res = getattr(mod, event)(core)
                    if res:
                        results.extend(res)
                except Exception as e:
                    log(f"[red]Erreur plugin {mod}: {e}[/red]", "error")
        return results

    def attack_dispatch(self, core, target, semaphore):
        # Chaine d'attaque, pour mode "auto" ou attaque spécifique
        try:
            for mod in self.plugins:
                if hasattr(mod, "attack") and mod.attack(core, target):
                    log(f"[green]Succès attaque {mod.__name__} sur {target.get('essid', target.get('bssid','?'))}[/green]")
        except Exception as e:
            log(f"[red]Erreur attaque: {e}[/red]", "error")
        finally:
            semaphore.release()