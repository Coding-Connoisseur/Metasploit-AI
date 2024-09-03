# ai_core/plugin_manager.py

import os
import importlib.util

class PluginManager:
    def __init__(self, ai):
        self.ai = ai
        self.plugins = {}

    def load_plugins(self):
        plugin_dir = "plugins"
        if not os.path.exists(plugin_dir):
            os.makedirs(plugin_dir)
        for file_name in os.listdir(plugin_dir):
            if file_name.endswith(".py"):
                plugin_name = file_name[:-3]
                plugin_path = os.path.join(plugin_dir, file_name)
                self.load_plugin(plugin_name, plugin_path)

    def load_plugin(self, name, path):
        spec = importlib.util.spec_from_file_location(name, path)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)
        self.plugins[name] = plugin
        self.ai.logging_manager.log_info(f"Loaded plugin: {name}")

    def execute_plugin(self, name, *args, **kwargs):
        if name in self.plugins:
            self.ai.logging_manager.log_info(f"Executing plugin: {name}")
            return self.plugins[name].execute(*args, **kwargs)
        else:
            return f"Plugin '{name}' not found."
