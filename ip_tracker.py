from dotenv import load_dotenv
import os
import requests
import json
import pyfiglet
import colorama
import sys
import folium
from colorama import Style, Fore
import socket
import shutil

colorama.init()

#The banner styling
def banner_ip():
    banner = f"""
    {Fore.LIGHTRED_EX}              ██╗██████╗     ███████╗████████╗ █████╗ ██╗  ██╗██╗  ██╗               
    {Fore.LIGHTRED_EX}              ██║██╔══██╗    ██╔════╝╚══██╔══╝██╔══██╗██║ ██╔╝██║  ██║              
    {Fore.LIGHTRED_EX}              ██║██████╔╝    ███████╗   ██║   ███████║█████╔╝ ███████║              
    {Fore.LIGHTRED_EX}              ██║██╔═══╝     ╚════██║   ██║   ██╔══██║██╔═██╗ ██╔══██║              
    {Fore.LIGHTRED_EX}              ██║██║         ███████║   ██║   ██║  ██║██║  ██╗██║  ██║              
    {Fore.LIGHTRED_EX}              ╚═╝╚═╝         ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝              
    {Fore.LIGHTRED_EX}                       I  P   S  T  A  L  K  E  R                                   
    {Fore.LIGHTBLACK_EX}==============================================================================
    {Fore.GREEN}🔥 Author:  {Fore.LIGHTRED_EX}Yaro Godwin       {Fore.GREEN}🌍 GitHub:  {Fore.LIGHTRED_EX}https://github.com/webgod1   
    {Fore.GREEN}🛠  Version: {Fore.LIGHTRED_EX}1.0               
    {Fore.LIGHTBLACK_EX}==============================================================================
    {Style.RESET_ALL}
    """
    
    print(banner)
    term_width = shutil.get_terminal_size().columns
    banner.center(term_width)



def system_clear():
    os.system('cls' if os.name == "nt" else 'clear')
    if sys.platform.startswith('win'):
        os.system('title IPTracker - by Godwin')
    elif sys.platform.startswith("linux") or sys.platform.startswith('mac'):
        sys.stdout.write(f"\033]0;IP Stalker - by Godwin\007")
        sys.stdout.flush()
        sys.stdout.flush()

file = open('ip_address.txt', 'w')

# def check_abuse_ipdb(ip, api_key):
def check_abuse(ip_input):
    load_dotenv()
    url = "https://api.abuseipdb.com/api/v2/check"
    API_KEY = os.getenv("ABUSEIPDB_API_KEY")
    if API_KEY is None:
        print("Error: AbuseIPDB API key not found. Please set it in the .env file.")
        exit(1)
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    params = {"ipAddress" : ip_input}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print("Checking Threat Intelligence...")
    if "data" in data:
        print(f"Abuse Confidence Score: {data['data']['abuseConfidenceScore']}")
        print("")
        with open('ip_address.txt', 'a') as file:
            file.write(f"Abuse Confidence Score: {data['data']['abuseConfidenceScore']} \n")
    else:
        print("Abuse Confidence Score: 0")
        with open('ip_address.txt', 'a') as file:
            file.write(f"Abuse Confidence Score: 0 \n")
        print("")





def main():
    try:       
            
            system_clear()
            banner_ip()


            print(Fore.LIGHTGREEN_EX + "1. Get a website IP-ADDRESS")
            print(Fore.LIGHTGREEN_EX + "2. Track an ip address")
            print(Fore.LIGHTGREEN_EX + "3. Exit")
            print("")
            try:
                option = int(input(Fore.LIGHTGREEN_EX + 'Select 1, 2 or 3 to continue: ' + Fore.WHITE))
            except ValueError:
                print(Fore.RED + "Invalid input! Please enter a number (1, 2, or 3).")
            if option == 1:
                website_ipaddress = input(Fore.LIGHTGREEN_EX + "Website Domain: " + Fore.WHITE)
                sock = socket.gethostbyname(website_ipaddress)
                
                #Fore.LIGHTGREEN_EX + "\n💻 Enter Target IP Address: " + Fore.WHITE
                print(f"IP-ADDRESS is: {sock}")
                # break
            elif option == 2:
                os.system('cls' if os.name == "nt" else 'clear')
                ip_input = input(Fore.LIGHTGREEN_EX + "💻Enter Target IP Address / exit: " + Fore.WHITE)
                if ip_input.lower() == "exit" or ip_input.lower() == 'e':
                    sys.exit()
                else:
                    #These does the OSINT work, getting all information from the 
                    # targeted IP_address and using the ip-api website for the information
                    ip_tracker = requests.get(f"http://ip-api.com/json/{ip_input}")
                    data = ip_tracker.json()
                    print("")
                    print("Fetching IP details ....")
                    print('')
                    print(f"Status: {data['status']}")
                    print("")
                    print(f"IP-ADDRESS: {data['query']}")
                    print("")
                    print(f"Country: {data['country']}")
                    print("")
                    print(f"Country Code: {data['countryCode']}")
                    print("")
                    print(f"Region Name: {data['regionName']}")
                    print("")
                    print(f"City: {data['city']}")
                    print("")
                    print(f"Zip Code: {data['zip']}")
                    print("")
                    print(f"Latitude: {data['lat']}")
                    print("")
                    print(f"Longitude: {data['lon']}")
                    print("")
                    print(f"Time Zone: {data['timezone']}")
                    print("")
                    print(f"Internet Service Provider: {data['isp']}")
                    print("") 

                    #To check if the targeted IP_address is on the abuse database
                    check_abuse(ip_input)
                   
                    #To check if the hostname is connected to an website... like the owner 
                    try:
                        print("Performing Reverse DNS Lookup...")
                        host_name = socket.gethostbyaddr(ip_input)
                        print(f"Found host name attached to these IP-ADDRESS: {host_name[0]}")
                        print('')
                    except socket.herror:
                        print("Hostname: No hostname found.")
                        print('')
                  
                    #Creating the map ui
                   
                    lat = data['lat']
                    lon = data['lon']
                    if lat and lon:
                        mymap = folium.Map(location=[lat, lon], zoom_start=10)
                        folium.Marker([lat,lon], popup=f"IP: {ip_input}").add_to(mymap)
                        mymap.save("ip_location.html")
                        print("Map have been save to ip_location.html")
                    else:
                        print("Error: Could not retrive the latitude and longitude")
                    
                    #writing the information to the ip_address.txt file
                    with open('ip_address.txt', 'a') as file:
                        file.write(f"Track Info for these IP:{data['query']} is: \n")
                        file.write(f"IP-Address is {data['query']} \n")
                        file.write(f"Country is {data['country']} \n")
                        file.write(f"City is {data['city']} \n")
                        file.write(f"Longitude is {data['lon']} \n")
                        file.write(f"Latitude is {data['lat']} \n")
                        file.write(f"Timezone is {data['timezone']} \n")
                        file.write(f"Zip Code is {data['zip']} \n")
                        file.write(f"RegionName is {data['regionName']} \n")
                        file.write(f"Map have been save to ip_location.html \n")                   
                        print("An extra copy have been saved to ip_address.txt")
                        
            else:
                sys.exit()
    #If we provoke an error it, it exit
    except Exception as e:
        print(f"Unexpected error {e} ")

main()