# ai_core/module_loader.py

import os
import importlib.util

class ModuleLoader:
    def __init__(self, logging_manager):
        self.logging_manager = logging_manager
        self.modules = {}
        self.plugins = {}

    def load_modules(self):
        module_dir = "modules"
        if not os.path.exists(module_dir):
            os.makedirs(module_dir)
        for file_name in os.listdir(module_dir):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]
                module_path = os.path.join(module_dir, file_name)
                self.load_module(module_name, module_path)

    def load_plugins(self):
        plugin_dir = "plugins"
        if not os.path.exists(plugin_dir):
            os.makedirs(plugin_dir)
        for file_name in os.listdir(plugin_dir):
            if file_name.endswith(".py"):
                plugin_name = file_name[:-3]
                plugin_path = os.path.join(plugin_dir, file_name)
                self.load_plugin(plugin_name, plugin_path)

    def load_module(self, name, path):
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.modules[name] = module
        self.logging_manager.log_info(f"Loaded module: {name}")

    def load_plugin(self, name, path):
        spec = importlib.util.spec_from_file_location(name, path)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)
        self.plugins[name] = plugin
        self.logging_manager.log_info(f"Loaded plugin: {name}")
