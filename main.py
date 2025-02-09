import argparse
from detector import KeyLoggerDetector

def main():
    parser = argparse.ArgumentParser(description="Key-Logging Detection System")
    parser.add_argument("--detect", action="store_true", help="Detect suspicious processes")
    parser.add_argument("--monitor", action="store_true", help="Monitor keyboard inputs")
    args = parser.parse_args()

    detector = KeyLoggerDetector()

    if args.detect:
        detector.detect_suspicious_processes()
    elif args.monitor:
        detector.monitor_keyboard()
    else:
        detector.run()

if __name__ == "__main__":
    main()
