import requests
import sys
from requests.exceptions import Timeout, HTTPError

URLS = [
    "https://httpstat.us/200",
    "https://httpstat.us/101",
    "https://httpstat.us/300",
    "https://httpstat.us/418",
    "https://httpstat.us/500"
]

def log_response(status: int, body: str):
    print(f"[SUCCESS] Status: {status}, Body: {body}")

def log_error(message: str):
    print(f"[ERROR] {message}")

def main():
    errors = 0

    for url in URLS:
        try:
            print(f"Checking {url}...")
            response = requests.get(url, timeout=10)  # Увеличили таймаут до 10 сек
            response.raise_for_status()
            
            if 100 <= response.status_code < 400:
                log_response(response.status_code, response.text)
                
        except Timeout as e:
            log_error(f"Timeout for {url}: {str(e)}")
            errors += 1
        except HTTPError as e:
            log_error(f"HTTP Error for {url}: {str(e)}")
            errors += 1
        except Exception as e:
            log_error(f"Unexpected error for {url}: {str(e)}")
            errors += 1

    if errors > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
