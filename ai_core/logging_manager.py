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
        self.session_actions = []

    def log_info(self, message):
        logging.info(message)
        self.session_actions.append({"timestamp": self.get_current_timestamp(), "description": message})

    def log_error(self, message):
        logging.error(message)
        self.session_actions.append({"timestamp": self.get_current_timestamp(), "description": message})

    def get_session_actions(self):
        return self.session_actions

    def get_current_timestamp(self):
        return logging.Formatter().formatTime(logging.LogRecord('', '', '', '', '', '', '', ''))

    def generate_report(self, session_data):
        report_file = f"report_{session_data['session_name']}.txt" if session_data else "session_report.txt"
        with open(report_file, 'w') as f:
            f.write("Session Report\n")
            f.write("================
