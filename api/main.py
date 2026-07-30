from fastapi import FastAPI


app = FastAPI(
    title="AI Order Platform"
)


@app.get("/")
def root():

    return {
        "service": "AI Order Platform",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "ok"
    }

