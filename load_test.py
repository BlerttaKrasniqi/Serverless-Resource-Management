import requests, time, json

URL = "http://127.0.0.1:8080/invoke"

PHASES  = [(10,1),(20,8),(20,0),(20,10)]

def pct(a,p):
    a = sorted(a)
    if not a: return 0.0
    i = max(0,min(len(a)-1, int(round((p/100)*len(a)-1))))
    return a[i]

def run():
    lat = []
    for duration, rate in PHASES:
        end = time.time()+duration
        if rate <= 0:
            time.sleep(duration)
            continue
        iv = 1.0/rate
        while time.time()<end:
            t0 = time.perf_counter()
            try:
                r = requests.get(URL, timeout=3); r.raise_for_status()
                lat.append((time.perf_counter()-t0)*1000.0)
            except: pass
            time.sleep(iv)

    stats={"count":len(lat),
           "avg_ms": sum(lat)/len(lat) if lat else 0,
           "p50_ms": pct(lat,50),"p95_ms": pct(lat,95),"p99_ms": pct(lat,99)}
    print(json.dumps(stats, indent=2))
    return {"latencies_ms":lat,"stats":stats}

if __name__=="__main__":
    open("baseline.json","w").write(json.dumps(run(), indent=2))
