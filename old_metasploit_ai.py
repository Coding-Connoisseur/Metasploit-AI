import os
import shutil
import logging
import platform
import importlib.util
from glob import glob
import requests
import json

# Configure logging
logging.basicConfig(
    filename='logs/ai_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class SelfLearningAI:
    def __init__(self):
        self.cwd = os.getcwd()
        self.modules = {}
        self.load_modules()
        self.command_history = []
        self.sessions = {}
        self.current_session = None
        self.custom_commands = {}
        self.load_plugins()

    def load_modules(self):
        module_files = glob("modules/*.py")
        for module_file in module_files:
            module_name = os.path.basename(module_file)[:-3]
            spec = importlib.util.spec_from_file_location(module_name, module_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            self.modules[module_name] = module
            logging.info(f"Loaded module: {module_name}")

    def query_vulnerability_db(self, query):
        try:
            url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?keyword={query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'result' in data:
                    return json.dumps(data['result']['CVE_Items'], indent=2)
                else:
                    return "No results found."
            else:
                return f"Failed to query database: HTTP {response.status_code}"
        except Exception as e:
            logging.error(f"Error querying vulnerability database: {e}")
            return f"Error querying database: {e}"
            
    def chain_exploits(self, *payloads):
	    results = []
	    for payload in payloads:
	        if payload in self.modules:
	            result = self.modules[payload].execute()
	            results.append(result)
	            logging.info(f"Executed payload {payload} in chain with result: {result}")
	        else:
	            logging.warning(f"Payload {payload} not found in chain.")
	            results.append(f"Payload {payload} not found.")
	    return "\n".join(results)
	    logging.info(f"Starting exploit chain with payloads: {payloads} at {datetime.now()}")

    def manage_payload(self, action, name=None, payload=None):
        payloads_dir = "payloads"
        os.makedirs(payloads_dir, exist_ok=True)
        payload_path = os.path.join(payloads_dir, f"{name}.txt")
        
        if action == "create" and name and payload:
            with open(payload_path, 'w') as f:
                f.write(payload)
            return f"Payload {name} created."

        elif action == "list":
            return "\n".join(os.listdir(payloads_dir))

        elif action == "delete" and name:
            if os.path.exists(payload_path):
                os.remove(payload_path)
                return f"Payload {name} deleted."
            else:
                return f"Payload {name} not found."

        elif action == "view" and name:
            if os.path.exists(payload_path):
                with open(payload_path, 'r') as f:
                    return f.read()
            else:
                return f"Payload {name} not found."

        else:
            return "Invalid action or parameters."

    def manage_session(self, action, name=None):
        session_dir = "sessions"
        os.makedirs(session_dir, exist_ok=True)
        session_path = os.path.join(session_dir, f"{name}.json")
        
        if action == "save" and name:
            if self.current_session:
                with open(session_path, 'w') as f:
                    json.dump(self.current_session, f)
                return f"Session {name} saved."
            else:
                return "No active session to save."

        elif action == "load" and name:
            if os.path.exists(session_path):
                with open(session_path, 'r') as f:
                    self.current_session = json.load(f)
                return f"Session {name} loaded."
            else:
                return f"Session {name} not found."

        elif action == "list":
            return "\n".join(os.listdir(session_dir))

        elif action == "delete" and name:
            if os.path.exists(session_path):
                os.remove(session_path)
                return f"Session {name} deleted."
            else:
                return f"Session {name} not found."

        else:
            return "Invalid action or parameters."

    def interactive_shell(self):
        print("Entering interactive shell. Type 'exit' to leave.")
        while True:
            cmd = input("shell> ")
            if cmd == "exit":
                break
            else:
                result = self.execute_command(cmd)
                print(result)

    def advanced_network_scan(self, target):
        # Simulated network scan logic
        logging.info(f"Scanning target: {target}")
        return f"Scanning target {target}...\nOpen ports: 22, 80, 443\nServices: SSH, HTTP, HTTPS\nOS: Linux"
        
    def add_custom_command(self, alias, command):
		    self.custom_commands[alias] = command
		    logging.info(f"Added custom command: {alias} -> {command}")
		    return f"Custom command '{alias}' added."
		    
		
    def remove_custom_command(self, alias):
		    if alias in self.custom_commands:
		        del self.custom_commands[alias]
		        logging.info(f"Removed custom command: {alias}")
		        return f"Custom command '{alias}' removed."
		    else:
		        return f"Custom command '{alias}' not found."
		        
    def pivot_network(self, target_network):
			    logging.info(f"Pivoting to network: {target_network}")
			    # Simulated logic to switch network
			    self.current_network = target_network
			    return f"Pivoted to network: {target_network}"
			    logging.info(f"Starting exploit chain with payloads: {payloads} at {datetime.now()}")
			    
    def execute_custom_command(self, alias):
			    if alias in self.custom_commands:
			        return self.execute_command(self.custom_commands[alias])
			    else:
			        return f"Custom command '{alias}' not found."
			        
    def load_plugins(self):
		    plugin_files = glob("plugins/*.py")
		    for plugin_file in plugin_files:
		        plugin_name = os.path.basename(plugin_file)[:-3]
		        spec = importlib.util.spec_from_file_location(plugin_name, plugin_file)
		        plugin = importlib.util.module_from_spec(spec)
		        spec.loader.exec_module(plugin)
		        if hasattr(plugin, 'register'):
		            plugin.register(self)
		        logging.info(f"Loaded plugin: {plugin_name}")

    def execute_command(self, command):
        try:
            self.command_history.append(command)
            args = command.split()

            if not args:
                return "No command entered."

            cmd = args[0]

            # Directory navigation
            if cmd == "cd":
                if len(args) > 1:
                    os.chdir(args[1])
                    self.cwd = os.getcwd()
                    result = f"Changed directory to {self.cwd}"
                else:
                    result = "No directory specified."

            # List directory contents
            elif cmd == "ls":
                result = "\n".join(os.listdir(self.cwd))

            # Make directory
            elif cmd == "mkdir":
                if len(args) > 1:
                    os.mkdir(args[1])
                    result = f"Directory {args[1]} created."
                else:
                    result = "No directory name specified."

            # Remove directory
            elif cmd == "rmdir":
                if len(args) > 1:
                    os.rmdir(args[1])
                    result = f"Directory {args[1]} removed."
                else:
                    result = "No directory name specified."
                    
            elif cmd == "chain":
             		if len(args) > 1:
             				result = self.chain_exploits(*args[1:])
             		else:
             				result = "No payloads specified for chaining."

            # Remove file
            elif cmd == "rm":
                if len(args) > 1:
                    os.remove(args[1])
                    result = f"File {args[1]} removed."
                else:
                    result = "No file specified."

            # Create empty file
            elif cmd == "touch":
                if len(args) > 1:
                    open(args[1], 'a').close()
                    result = f"File {args[1]} created."
                else:
                    result = "No file name specified."

            # Copy file
            elif cmd == "cp":
                if len(args) > 2:
                    shutil.copy(args[1], args[2])
                    result = f"Copied {args[1]} to {args[2]}."
                else:
                    result = "Source or destination not specified."

            # Move file
            elif cmd == "mv":
                if len(args) > 2:
                    shutil.move(args[1], args[2])
                    result = f"Moved {args[1]} to {args[2]}."
                else:
                    result = "Source or destination not specified."

            # Display file contents
            elif cmd == "cat":
                if len(args) > 1:
                    with open(args[1], 'r') as f:
                        result = f.read()
                else:
                    result = "No file specified."

            # Print working directory
            elif cmd == "pwd":
                result = self.cwd

            # Display current user
            elif cmd == "whoami":
                result = platform.node()

            # Clear the screen (simulated by just printing several newlines)
            elif cmd == "clear":
                result = "\n" * 100

            # Simulate head command
            elif cmd == "head":
                if len(args) > 1:
                    with open(args[1], 'r') as f:
                        lines = f.readlines()
                        result = ''.join(lines[:10])
                else:
                    result = "No file specified."

            # Simulate tail command
            elif cmd == "tail":
                if len(args) > 1:
                    with open(args[1], 'r') as f:
                        lines = f.readlines()
                        result = ''.join(lines[-10:])
                else:
                    result = "No file specified."

            # Simulate grep command
            elif cmd == "grep":
                if len(args) > 2:
                    with open(args[2], 'r') as f:
                        lines = f.readlines()
                        result = ''.join([line for line in lines if args[1] in line])
                else:
                    result = "Pattern or file not specified."

            # Execute a module
            elif cmd == "exec":
                if len(args) > 1 and args[1] in self.modules:
                    result = self.modules[args[1]].execute(*args[2:])
                else:
                    result = "Module not found or not specified."

            # Vulnerability database query
            elif cmd == "vuln":
                if len(args) > 1:
                    result = self.query_vulnerability_db(" ".join(args[1:]))
                else:
                    result = "No query specified."

            # Payload management
            elif cmd == "payload":
                if len(args) > 1:
                    action = args[1]
                    name = args[2] if len(args) > 2 else None
                    payload = " ".join(args[3:]) if len(args) > 3 else None
                    result = self.manage_payload(action, name, payload)
                else:
                    result = "No action specified."

            # Session management
            elif cmd == "session":
                if len(args) > 1:
                    action = args[1]
                    name = args[2] if len(args) > 2 else None
                    result = self.manage_session(action, name)
                else:
                    result = "No action specified."

            # Interactive shell
            elif cmd == "shell":
                self.interactive_shell()
                result = "Exited shell."

            # Advanced network scan
            elif cmd == "scan":
                if len(args) > 1:
                    result = self.advanced_network_scan(args[1])
                else:
                    result = "No target specified."
                    
            elif cmd == "pivot":
                if len(args) > 1:
                    result = self.pivot_network(args[1])
                else:
                    result = "No target network specified."
                    
            elif cmd == "alias":
                if len(args) > 2:
                    result = self.add_custom_command(args[1], " ".join(args[2:]))
                else:
                    result = "No alias or command specified."
                    
            elif cmd == "unalias":
                if len(args) > 1:
                    result = self.remove_custom_command(args[1])
                else:
                    result = "No alias specified."
                    
            elif cmd in self.custom_commands:
                result = self.execute_custom_command(cmd)

            else:
                result = f"Command '{cmd}' is not supported."
             
            logging.info(f"Executed command: {command}")
            return result
        except Exception as e:
            return f"Error executing command: {e}"
            logging.info(f"Command '{command}' executed at {datetime.now()}")
            logging.debug(f"Command details: {command}, Args: {args[1:]}")

    def show_help(self):
        help_text = """
        =========================================
        AI Framework Help Menu
        =========================================

        General Commands:
        -----------------
        help                     : Display this help menu.
        version                  : Show the current AI version.
        features                 : List all learned features.

        File and Directory Commands:
        ----------------------------
        cd <directory>           : Change the current directory.
        ls                       : List the contents of the current directory.
        mkdir <directory>        : Create a new directory.
        rmdir <directory>        : Remove an existing directory.
        rm <file>                : Remove a file.
        touch <file>             : Create an empty file.
        cp <source> <destination>: Copy a file.
        mv <source> <destination>: Move a file.
        cat <file>               : Display the contents of a file.
        pwd                      : Display the current directory.
        whoami                   : Display the current user (device name).
        clear                    : Clear the screen.
        head <file>              : Display the first 10 lines of a file.
        tail <file>              : Display the last 10 lines of a file.
        grep <pattern> <file>    : Search for a pattern in a file.

        Module Management Commands:
        ---------------------------
        install_module <name> <code>: Install a new module.
        update_module <name> <code> : Update an existing module.
        remove_module <name>        : Remove an existing module.

        Vulnerability Commands:
        -----------------------
        vuln <query>                : Query an online vulnerability database.

        Payload Management Commands:
        ----------------------------
        payload create <name> <code> : Create a new payload.
        payload list                 : List all stored payloads.
        payload delete <name>        : Delete a specified payload.
        payload view <name>          : View a specified payload.

        Session Management Commands:
        ----------------------------
        session save <name>          : Save the current session.
        session load <name>          : Load a saved session.
        session list                 : List all saved sessions.
        session delete <name>        : Delete a specified session.

        Exploitation Commands:
        ----------------------
        exploit <target> <payload>   : Simulate an exploit on a target with a payload.

        Shell and Network Commands:
        ---------------------------
        shell                        : Enter an interactive shell.
        scan <target>                : Perform an advanced network scan on a target.

        =========================================
        """
        logging.info("Displayed help menu.")
        print(help_text)

    def run(self):
        while True:
            try:
                user_input = input("ai> ")
                if user_input == "help":
                    self.show_help()
                else:
                    print(self.execute_command(user_input))
            except Exception as e:
                logging.error(f"Error in main loop: {e}")
                print("An unexpected error occurred. Please check the logs for details.")

if __name__ == "__main__":
    ai = SelfLearningAI()
    ai.run()
