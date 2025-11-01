import requests, time
URL = "http://127.0.0.1:8080/invoke"

if __name__ == "__main__":
    print("Scheduler: ping every 30s to keep warm")
    while True:
        try: requests.get(URL, timeout=2)
        except: pass
        time.sleep(30)
