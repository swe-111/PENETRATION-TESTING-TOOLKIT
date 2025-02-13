from modules.port_scanner import scan_ports
from modules.brute_forcer import brute_force_ssh

def main():
    print("Welcome to the Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    choice = input("Select a module (1/2): ")

    if choice == '1':
        target = input("Enter the target IP address: ")
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        open_ports = scan_ports(target, start_port, end_port)
        print(f"Open ports: {open_ports}")
    elif choice == '2':
        target = input("Enter the target IP address: ")
        username = input("Enter the username: ")
        password_file = input("Enter the path to the password list: ")
        
        with open(password_file, 'r') as file:
            passwords = file.read().splitlines()
        
        brute_force_ssh(target, username, passwords)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()