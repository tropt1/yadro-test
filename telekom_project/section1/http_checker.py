import requests
import sys

URLS = [
    "https://httpstat.us/200",
    "https://httpstat.us/120",
    "https://httpstat.us/301",
    "https://httpstat.us/404",
    "https://httpstat.us/500"
]

def log_responce(status: int, body: str):
    print(f"[{status}] {body}")


def main():
    for url in URLS:
        try:
            responce = requests.get(url, timeout=5)
            responce.raise_for_status()

            if 100 <= responce.status_code < 400:
                log_responce(responce.status_code, responce.text)

        except requests.HTTPError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Fatal error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()

