
import psutil
from pynput import keyboard

class KeyLoggerDetector:
    def __init__(self):
        self.logger = Logger()  

    def detect_suspicious_processes(self):
        suspicious_names = ["keylogger", "spyware", "remoteaccess"]  
        running_processes = [p.info["name"].lower() for p in psutil.process_iter(attrs=["name"])]
        for name in suspicious_names:
            if any(name in proc for proc in running_processes):
                print(f"Warning: Suspicious process found containing '{name}'")

    def monitor_keyboard(self):
        print("Monitoring keyboard input...")
        with keyboard.Listener(on_press=self.logger.on_press, on_release=self.logger.on_release) as listener:
            listener.join()

    def run(self):
        print("Running the Key-Logging Detection System. Use --detect or --monitor for specific actions.")

class Logger:
    def __init__(self):
        print("Logger initialized.")

    def on_press(self, key):
        try:
            print(f"Key pressed: {key.char}")
         
        except AttributeError:
            print(f"Special key pressed: {key}")
           
    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            return False

if __name__ == "__main__":
  
    detector = KeyLoggerDetector()
    detector.run()
