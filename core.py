import os
import threading
from wifite3.banner import WIFITE3_BANNER
from wifite3.utils import log, console
from wifite3.plugins.manager import PluginManager

class Wifite3Core:
    def __init__(self, args):
        self.args = args
        self.plugins = PluginManager(args.plugins or [])
        self.max_threads = args.threads
        self.thread_semaphore = threading.Semaphore(self.max_threads)
        self.attack_threads = []

    def run(self):
        console.print(f"[bold magenta]{WIFITE3_BANNER}[/bold magenta]")
        self.plugins.load_all()
        if self.args.mode == "scan":
            targets = self.plugins.hook("scan", self)
        elif self.args.mode in ("handshake", "pmkid", "wps", "eviltwin", "brute", "crack", "analyze"):
            targets = self.plugins.hook("pre_attack", self)
            self._attack(targets)
        elif self.args.mode in ("auto",):
            targets = self.plugins.hook("scan", self)
            self._attack(targets)
        else:
            log("[red]Mode inconnu.[/red]")
            return
        self.wait_attacks()
        self.plugins.hook("post", self)
        if self.args.cleanup:
            self.plugins.hook("cleanup", self)
            log("[cyan]Nettoyage complet effectué[/cyan]")

    def _attack(self, targets):
        if not targets:
            log("[red]Aucune cible à attaquer.[/red]")
            return
        for target in targets:
            self.thread_semaphore.acquire()
            t = threading.Thread(target=self.plugins.attack_dispatch, args=(self, target, self.thread_semaphore))
            t.start()
            self.attack_threads.append(t)

    def wait_attacks(self):
        for t in self.attack_threads:
            t.join()