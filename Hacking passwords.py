import hashlib
rainbow_table = {}
stolen_data = {}

def hasher(password):
    b = bytes(password, 'utf-8')
    m = hashlib.sha256(b)
    m = m.hexdigest()
    return m

def make_RT():
    file = open("passwords.txt", "r")
    for password in file:
        hashed = hasher(password.strip('\n'))
        rainbow_table[hashed] = password.strip('\n')

def get_stolen_data():
    file = open("accounts.txt", "r")
    for account in file:
        words = accounts.split(" ")
        hashed = words[0]
        username = [1]
        stolen_data[hashed]= username
    f.close()

def crack_passwords():
    file = open("cracked passwords.txt", "a+")
    for hpass in rainbow_table:
        if stolen_data.get(hpass):
            file.write("username: " + stolen_data[hpass])
            file.write(" password: " + rainbow_table[hpass])
            file.write("\n")

make_RT()
get_stolen_data()
crack_passwords()


