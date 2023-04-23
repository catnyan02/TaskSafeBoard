from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(docs_url="/api/docs")

process = None


def is_running(proc):
    pass


@app.post("/api/top")
async def start_process():
    global process

    if is_running(process):
        raise HTTPException(status_code=400, detail="Already running")

    # start process

    return {"message": "Process started"}


@app.delete("/api/top")
async def stop_process():
    global process

    if not is_running(process):
        raise HTTPException(status_code=400, detail="Not running")

    # stop process

    return {"message": "Process stopped"}


@app.get("/api/top")
async def get_process_status():
    global process
    return {"status": "Not running" if not is_running(process) else "Running"}


@app.get("/api/top/result")
async def get_process_result():
    global process

    if is_running(process) or process is None:
        raise HTTPException(status_code=404, detail="Not Found")

    # get result from process

    return {"result": ""}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

