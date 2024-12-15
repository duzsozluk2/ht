import sys
import os
import signal
import time
from ss7.tracking import *
from ss7.interception import *
from ss7.fraud import *
from ss7.dos import *
from ss7main import *
from gtpmain import *
from gtp import *
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

# Initialize colorama for terminal output formatting
init()

# Define some basic functionality for the tool
class Sigploit:
    def __init__(self):
        self.running = True

    def banner(self):
        # Display a banner using pyfiglet
        banner = figlet_format("Sigploit")
        cprint(banner, "yellow")

    def display_menu(self):
        cprint("Sigploit - Telecom Security Tool", "green")
        cprint("1. SS7 Tracking", "blue")
        cprint("2. SS7 Interception", "blue")
        cprint("3. SS7 Fraud Detection", "blue")
        cprint("4. SS7 DoS Prevention", "blue")
        cprint("5. GTP Tunneling", "blue")
        cprint("0. Exit", "red")
        choice = input("Select an option: ")
        return choice

    def ss7_tracking(self):
        cprint("Starting SS7 Tracking...", "yellow")
        # Example: Initialize SS7 tracking module
        track = SS7Tracking()
        track.start_tracking()

    def ss7_interception(self):
        cprint("Starting SS7 Interception...", "yellow")
        # Example: Initialize SS7 interception module
        intercept = SS7Interception()
        intercept.start_interception()

    def ss7_fraud_detection(self):
        cprint("Starting SS7 Fraud Detection...", "yellow")
        # Example: Initialize SS7 fraud detection
        fraud = SS7Fraud()
        fraud.detect_fraud()

    def ss7_dos_protection(self):
        cprint("Starting SS7 DoS Prevention...", "yellow")
        # Example: Initialize SS7 DoS prevention
        dos = SS7DosProtection()
        dos.prevent_dos()

    def gtp_tunneling(self):
        cprint("Starting GTP Tunneling...", "yellow")
        # Example: Initialize GTP tunneling
        gtp = GTP()
        gtp.create_tunnel()

    def handle_signal(self, signal, frame):
        cprint("\n[!] Exiting gracefully...", "red")
        self.running = False
        sys.exit(0)

    def run(self):
        # Handle SIGINT (Ctrl+C) to exit gracefully
        signal.signal(signal.SIGINT, self.handle_signal)

        while self.running:
            self.banner()
            choice = self.display_menu()

            if choice == '1':
                self.ss7_tracking()
            elif choice == '2':
                self.ss7_interception()
            elif choice == '3':
                self.ss7_fraud_detection()
            elif choice == '4':
                self.ss7_dos_protection()
            elif choice == '5':
                self.gtp_tunneling()
            elif choice == '0':
                cprint("Exiting Sigploit...", "red")
                self.running = False
            else:
                cprint("[!] Invalid choice. Please try again.", "red")

            time.sleep(1)

if __name__ == "__main__":
    sigploit = Sigploit()
    sigploit.run()
