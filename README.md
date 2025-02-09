# Key-Logging Detection

The Key Logging Derection project to detect and prevent unauthorized keylogging activities on Linux and Windows systems. The system monitors keyboard inputs, detects suspicious processes, and analyzes network activity to identify potential keyloggers.

---

## Features

- **Process Monitoring**: Detects suspicious background processes associated with keylogging.
- **Keyboard Input Monitoring**: Logs keyboard inputs to identify unusual behavior.
- **Network Activity Monitoring**: Monitors network connections of suspicious processes to detect data exfiltration.
- **Cross-Platform**: Works on both Linux and Windows systems.

---

## Prerequisites

Before using this project, ensure you have the following installed:

### 1. **Python 3.6 or higher**
   - Download and install Python from [python.org](https://www.python.org/downloads/).

### 2. **Required Python Libraries**
   Install the required libraries using `pip`:
   ```bash
   pip install psutil pynput
   ```

   **For Windows Users**:
   - Install `pywin32` for additional Windows-specific functionality:
     ```bash
     pip install pywin32
     ```

### 3. **Administrator/Root Privileges**
   - On Windows, run the script as an Administrator.
   - On Linux, run the script with `sudo` or as a root user.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/keylogger-detector.git
   cd keylogger-detector
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. **Detect Suspicious Processes**
   To detect suspicious processes associated with keylogging:
   ```bash
   python main.py --detect
   ```

### 2. **Monitor Keyboard Inputs**
   To monitor keyboard inputs for unusual behavior:
   ```bash
   python main.py --monitor
   ```

### 3. **Run Full Detection System**
   To run the full detection system (process monitoring + keyboard monitoring):
   ```bash
   python main.py
   ```

### 4. **View Logs**
   All detected activities are logged in `detection_log.txt` in the project directory.

---

## Project Structure

```
keylogger-detector/
├── main.py                # Main CLI interface
├── detector.py            # Core detection logic
├── logger.py              # Logging detected activities
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---



## Disclaimer

This project is for educational and ethical purposes only. Do not use it for malicious activities. The authors are not responsible for any misuse of this tool.

---

## Support

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/your-username/KEY-LOGGING-DETECTION/issues).
