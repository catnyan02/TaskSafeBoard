from fastapi import FastAPI, HTTPException
import uvicorn
from subprocess import Popen, PIPE

import time
from psutil import Process

app = FastAPI(docs_url="/api/docs")

process = None


def is_running(proc):
    return proc and proc.poll() is None


@app.post("/api/top")
async def start_process():
    global process

    if is_running(process):
        raise HTTPException(status_code=400, detail="Already running")

    process = Popen(['top', '-b', '-d', '60', '-n', '5'], stdout=PIPE, stderr=PIPE)

    return {"message": "Process started"}


@app.delete("/api/top")
async def stop_process():
    global process

    if not is_running(process):
        raise HTTPException(status_code=400, detail="Not running")

    process.terminate()

    return {"message": "Process stopped"}


@app.get("/api/top")
async def get_process_status():
    global process
    if not is_running(process):
        return {"status": "Not running"}
    proc = Process(process.pid)
    return {"status": "Running", "time_elapsed": time.time() - proc.create_time(), "cpu%": proc.cpu_percent(),
            "memory%": proc.memory_percent()}


@app.get("/api/top/result")
async def get_process_result():
    global process

    if is_running(process) or process is None:
        raise HTTPException(status_code=404, detail="Not Found")

    output, error = process.communicate()
    if error:
        return {"error": error.decode()}
    return {"result": output.decode()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
