import requests
import socket
import whois
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# =============================
# USERNAME CHECKER
# =============================

def check_username(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}"
    }

    print("\n[+] Username Search Results:\n")

    for site, url in sites.items():
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)

            if response.status_code == 200:
                print(f"[FOUND] {site}: {url}")
            else:
                print(f"[NOT FOUND] {site}")

        except Exception as e:
            print(f"[ERROR] {site}: {e}")


# =============================
# DOMAIN INFORMATION
# =============================

def domain_info(domain):
    print("\n[+] Domain Information:\n")

    try:
        info = whois.whois(domain)

        print(f"Domain: {domain}")
        print(f"Registrar: {info.registrar}")
        print(f"Creation Date: {info.creation_date}")
        print(f"Expiration Date: {info.expiration_date}")
        print(f"Name Servers: {info.name_servers}")

    except Exception as e:
        print(f"Error: {e}")


# =============================
# DNS + IP LOOKUP
# =============================

def ip_lookup(domain):
    print("\n[+] DNS / IP Information:\n")

    try:
        ip = socket.gethostbyname(domain)

        print(f"Domain: {domain}")
        print(f"IP Address: {ip}")

    except Exception as e:
        print(f"Error: {e}")


# =============================
# WEBSITE METADATA
# =============================

def website_metadata(url):
    print("\n[+] Website Metadata:\n")

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No Title"

        print(f"Title: {title}")

        description = soup.find("meta", attrs={"name": "description"})

        if description:
            print(f"Description: {description.get('content')}")
        else:
            print("Description: Not Found")

        links = soup.find_all("a")

        print(f"Total Links Found: {len(links)}")

    except Exception as e:
        print(f"Error: {e}")


# =============================
# GOOGLE DORK GENERATOR
# =============================

def generate_google_dorks(target):
    print("\n[+] Google Dorks:\n")

    dorks = [
        f'site:{target}',
        f'site:{target} ext:pdf',
        f'site:{target} inurl:login',
        f'site:{target} intitle:index.of',
        f'site:{target} filetype:sql'
    ]

    for dork in dorks:
        print(dork)


# =============================
# MAIN MENU
# =============================

def main():
    while True:
        print("""
==============================
 Educational OSINT Toolkit
==============================
1. Username Search
2. Domain Information
3. DNS/IP Lookup
4. Website Metadata
5. Google Dork Generator
6. Exit
==============================
""")

        choice = input("Select Option: ")

        if choice == "1":
            username = input("Enter Username: ")
            check_username(username)

        elif choice == "2":
            domain = input("Enter Domain: ")
            domain_info(domain)

        elif choice == "3":
            domain = input("Enter Domain: ")
            ip_lookup(domain)

        elif choice == "4":
            url = input("Enter Website URL: ")

            if not url.startswith("http"):
                url = "https://" + url

            website_metadata(url)

        elif choice == "5":
            target = input("Enter Target Domain: ")
            generate_google_dorks(target)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid Option")


if __name__ == "__main__":
    main()
