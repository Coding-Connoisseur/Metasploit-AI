# ai_core/module_loader.py

import os
import importlib.util
from glob import glob

class ModuleLoader:
    def __init__(self, logging_manager):
        self.modules = {}
        self.logging_manager = logging_manager

    def load_modules(self):
        module_files = glob("modules/*.py")
        for module_file in module_files:
            self.load_module(module_file)
    
    def load_plugins(self):
        plugin_files = glob("plugins/*.py")
        for plugin_file in plugin_files:
            self.load_module(plugin_file, is_plugin=True)

    def load_module(self, file_path, is_plugin=False):
        module_name = os.path.basename(file_path)[:-3]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.modules[module_name] = module
        module_type = "plugin" if is_plugin else "module"
        self.logging_manager.log_info(f"Loaded {module_type}: {module_name}")

    def change_directory(self, args):
        if len(args) > 0:
            os.chdir(args[0])
            return f"Changed directory to {os.getcwd()}"
        else:
            return "No directory specified."

    def list_directory(self):
        return "\n".join(os.listdir(os.getcwd()))

    def execute_module(self, args):
        if len(args) > 0 and args[0] in self.modules:
            return self.modules[args[0]].execute(*args[1:])
        else:
            return "Module not found or not specified."
