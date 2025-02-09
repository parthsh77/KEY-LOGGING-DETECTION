import psutil
import os
import platform
from pynput import keyboard

banner = r"""
        ______
     .-'      `-.
    /            \
   |              |
   |,  .-.  .-.  ,|
   | )(_o/  \o_)( |
   |/     /\     \|
   (_     ^^     _)
    \__|IIIIII|__/
     | \IIIIII/ |
     \          /
      `--------`

██████╗  █████╗ ██████╗ ████████╗██╗  ██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║  ██║
██████╔╝███████║██████╔╝   ██║   ███████║
██╔═══╝ ██╔══██║██╔══██╗   ██║   ██╔══██║
██║     ██║  ██║██║  ██║   ██║   ██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
                                         
"""

class KeyLoggerDetector:
    def __init__(self):
        self.system = platform.system()
        self.suspicious_processes = ["keylogger", "logkeys", "kidlogger"]  
        self.logger = Logger()

    def detect_suspicious_processes(self):
        """Detect suspicious processes running on the system."""
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                process_name = proc.info['name'].lower()
                for suspicious_name in self.suspicious_processes:
                    if suspicious_name in process_name:
                        self.logger.log(f"Suspicious process detected: {process_name} (PID: {proc.info['pid']})")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def monitor_keyboard(self):
        """Monitor keyboard inputs for unusual behavior."""
        def on_press(key):
            try:
                self.logger.log(f"Key pressed: {key.char}")
            except AttributeError:
                self.logger.log(f"Special key pressed: {key}")

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def run(self):
        """Run the detection system."""
        print("Starting Key-Logging Detection System...")
        self.detect_suspicious_processes()
        print("Monitoring keyboard inputs...")
        self.monitor_keyboard()
