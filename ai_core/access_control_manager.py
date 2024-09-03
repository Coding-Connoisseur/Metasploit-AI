# ai_core/access_control_manager.py

class AccessControlManager:
    def __init__(self, ai):
        self.ai = ai
        self.users = {}
        self.roles = {
            "admin": {"can_execute_exploits": True, "can_manage_sessions": True},
            "user": {"can_execute_exploits": True, "can_manage_sessions": False},
            "guest": {"can_execute_exploits": False, "can_manage_sessions": False}
        }

    def add_user(self, username, password, role="guest"):
        if username in self.users:
            return f"User {username} already exists."
        if role not in self.roles:
            return f"Role {role} does not exist."
        self.users[username] = {"password": password, "role": role}
        self.ai.logging_manager.log_info(f"Added user {username} with role {role}")
        return f"User {username} added with role {role}."

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            self.ai.logging_manager.log_info(f"User {username} authenticated successfully")
            return True
        self.ai.logging_manager.log_warning(f"Failed authentication attempt for user {username}")
        return False

    def authorize_action(self, username, action):
        user = self.users.get(username)
        if not user:
            self.ai.logging_manager.log_warning(f"Authorization failed: user {username} does not exist")
            return False
        role = user["role"]
        if self.roles[role].get(action, False):
            self.ai.logging_manager.log_info(f"User {username} authorized for action {action}")
            return True
        self.ai.logging_manager.log_warning(f"User {username} not authorized for action {action}")
        return False
