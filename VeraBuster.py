# VeraCrypt wordlist attack tool
#
# Copyright (c) 2023    Nastya Grifon
# This software is licensed under the Original BSD License

import argparse
import subprocess
import sys
import os

# Function to check for root privileges
def check_root():
    if not os.geteuid() == 0:
        try:
            subprocess.check_call(['sudo', 'true']) 
        except subprocess.CalledProcessError:
            sys.exit("Administrator privileges are required to run the script.")  # Exit if sudo access is not granted

# Function to crack VeraCrypt on Linux
def linuxCrack(p, veracryptPath, volume, total, total_passwords, debug=False):
    cmd = f'veracrypt -t "{volume}" -p {p} --non-interactive'  # Command to execute VeraCrypt
    if debug:
        print(f"Executing command: {cmd}")  # Print the executed command if in debug mode
    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
    out, err = process.communicate()  
    procreturn = str(out, "utf-8").strip() if out else str(err, "utf-8").strip()  # Convert the output to a string
    printProgressBar(total, total_passwords)  
    total += 1 
    return procreturn.find("Error: Operation failed due to one or more of the following:") == -1  # Check if there was an error

# Function to print the progress bar
def printProgressBar(iteration, total, prefix='Progress', suffix='Complete', decimals=1, length=50, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))  
    filledLength = int(length * iteration // total)  
    bar = fill * filledLength + '-' * (length - filledLength)  
    print(f'\r{prefix} ({iteration}/{total}) |{bar}| {percent}% {suffix}', end=printEnd) 
    if iteration == total:
        print() 

if __name__ == '__main__':
    check_root()  

    parser = argparse.ArgumentParser(description='VeraCrypt volume cracker') 
    parser.add_argument('-v', metavar='volume', type=str, required=True, help='Path to volume')  
    parser.add_argument('-p', metavar='wordlist', type=str, nargs="?", help='Path to wordlist')  
    parser.add_argument('-d', action='store_true', help='Enable debug mode')  
    args = parser.parse_args() 

    try:
        if args.d:
            print("Checking for VeraCrypt installation...")  # Print the status if in debug mode
        subprocess.check_output(["which", "veracrypt"])  # Check if VeraCrypt is installed
    except subprocess.CalledProcessError as e:
        if args.d:
            print("Error: VeraCrypt not found. Please install VeraCrypt or check the path.")  
        sys.exit()  

    if not os.path.isfile(args.v) or not os.path.isfile(args.p):
        if args.d:
            print("Error: Volume file or wordlist not found or inaccessible.")
        sys.exit()  

    wordlist = [x.strip() for x in open(args.p, 'r')] if args.p else [] 

    total_passwords = len(wordlist)  
    total = 1 
    password_found = False  
    printProgressBar(total, total_passwords)  
    print("Starting the cracking process...")

    for p in wordlist:  
        printProgressBar(total, total_passwords) 
        print(f"\nTrying password: {p}")  # Print the currently tested password
        if linuxCrack(p, "veracrypt", args.v, total, total_passwords, args.d): 
            if password_found or args.d:
                print(f"Password found: {p}")  
            password_found = True  
            break  
        total += 1  
    if not password_found:
        printProgressBar(total, total_passwords)  
        print("\nPassword not found")
