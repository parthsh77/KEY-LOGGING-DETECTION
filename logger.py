import datetime

class Logger:
    def __init__(self, log_file="detection_log.txt"):
        self.log_file = log_file

    def log(self, message):
        """Log a message with a timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"
        with open(self.log_file, "a") as f:
            f.write(log_message)
        print(log_message.strip())
