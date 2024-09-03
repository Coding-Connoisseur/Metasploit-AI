# ai_core/logging_manager.py

import logging
import os

class LoggingManager:
    def __init__(self):
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        logging.basicConfig(
            filename=os.path.join(log_dir, 'ai_log.log'),
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def log_info(self, message):
        logging.info(message)
    
    def log_error(self, message):
        logging.error(message)

    def generate_report(self, session_data):
        report_file = f"report_{session_data['session_name']}.txt"
        with open(report_file, 'w') as f:
            f.write("Session Report\n")
            f.write("=================\n")
            for action in session_data['actions']:
                f.write(f"{action['timestamp']}: {action['description']}\n")
        logging.info(f"Report generated: {report_file}")
        return f"Report generated: {report_file}"