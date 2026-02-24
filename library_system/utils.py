import datetime

# Logging Decorator: Logs the timestamp when an action runs [cite: 289]
def track_access(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] LOG: Action '{func.__name__}' was executed.")
        return func(*args, **kwargs)
    return wrapper

# Access Control Closure: Checks if the user has the required role (e.g., "Admin") [cite: 290, 291]
# 2. Access Control Closure
def permission_check(required_role):
    def decorator(func):
        # We add 'self' here so it properly catches the object, leaving 'user_role' to catch the string!
        def wrapper(self, user_role, *args, **kwargs):
            if user_role != required_role:
                print(f"Access Denied! You need '{required_role}' privileges to do this.")
                return None
            return func(self, user_role, *args, **kwargs)
        return wrapper
    return decorator