IP Stalker - Advanced IP Tracking Tool

🔥 About IP Stalker

IP Stalker is an advanced IP tracking tool designed for OSINT (Open-Source Intelligence) investigations. It allows users to retrieve detailed geolocation information, ISP data, abuse reports, and perform reverse DNS lookups on any given IP address or domain.

🚀 Features

🌍 IP Geolocation Tracking – Get country, city, ISP, timezone, latitude, and longitude of any IP.

🔎 Threat Intelligence Lookup – Check if an IP is flagged in the AbuseIPDB database.

🖥 Website to IP Lookup – Resolve any domain name to its IP address.

🏷 Reverse DNS Lookup – Find hostnames associated with an IP address.

🗺 Interactive Map Generation – Displays IP location on a Folium-generated map.

📜 Automatic Data Logging – Saves gathered data into ip_address.txt for later analysis.

🛠 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/webgod1/IP-Stalker.git
cd IP-Stalker

2️⃣ Install Dependencies

Ensure you have Python installed, then install the required libraries:

pip install -r requirements.txt

3️⃣ Set Up API Key for AbuseIPDB

🔑 How to Get an AbuseIPDB API Key
Go to the AbuseIPDB Website

Visit: https://www.abuseipdb.com/
Create an Account (If You Don’t Have One)

Click on Sign Up and complete the registration.
Verify your email.
Get Your API Key

After logging in, go to API from the dashboard.
Click Generate API Key.
Copy the key provided.
Set Up the API Key in Your Project

Open the .env file in your project directory.
Add the following line:
plaintext
Copy
Edit
ABUSEIPDB_API_KEY=your_api_key_here
Save the file.
You're Ready to Go! 🚀

Now, the script will automatically use your API key to check IP reputation.

🔴 Security Warning: Never share your API key publicly (e.g., in GitHub repositories). If you accidentally expose it, go to AbuseIPDB and regenerate a new
Create a .env file in the project directory and add your AbuseIPDB API Key:

⚠ Do NOT share your API key or upload your .env file to GitHub.

🔧 Usage

Run the script with:

python ip_stalker.py

Then, choose from the menu options:

Option 1: Get the IP address of a website.

Option 2: Track an IP address.

Option 3: Exit the program.

📍 Example Output

Fetching IP details ...
IP-ADDRESS: 192.168.1.1
Country: United States
City: New York
ISP: Comcast Cable
Threat Intelligence Score: 85
Map saved as ip_location.html

🛡 Security Considerations

Ethical Use Only: This tool is for educational and cybersecurity research purposes only.

Respect Privacy Laws: Ensure compliance with legal regulations before using this tool.

Keep API Keys Secure: Never expose your .env file.

🤝 Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Commit your changes (git commit -m "Added new feature").

Push to the branch (git push origin feature-name).

Submit a Pull Request.


🔗 Connect with Me

💡 Author: Yaro Godwin
📧 Email: godwinsamue0@example.com
📌 GitHub: https://github.com/webgod1

