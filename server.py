from flask import Flask, jsonify
import time, random


app = Flask(__name__)
COLD = True

@app.route("/invoke")

def invoke():
    global COLD
    start = time.perf_counter()

    if COLD:
        time.sleep(0.5)
        COLD = False
    
    time.sleep(random.uniform(0.01,0.05))
    latency = (time.perf_counter()-start)*1000
    return jsonify({"ok":True,"latency_ms":round(latency,2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
