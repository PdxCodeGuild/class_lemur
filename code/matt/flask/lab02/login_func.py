def login(username_attempt, password_attempt, profile):
    if username_attempt == profile["username"] and password_attempt == profile["password"]:
        return True
    else:
        return False
