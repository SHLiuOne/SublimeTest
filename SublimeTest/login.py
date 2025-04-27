users = {'alice': 'password123', 'bob': 'qwerty'}

def login(username, password):
    # 这里写验证逻辑
    if username in users:
        if users[username] == password:
            return True
        else:
            return False
    else:
        return False

# Tests
print(login('alice', 'password123'))  # 应该True
print(login('bob', 'wrongpass'))       # 应该False
print(login('charlie', 'password'))    # 应该False
