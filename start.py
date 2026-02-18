import uvicorn
import os

if __name__ == "__main__":
    # Render provides the port in an environment variable
    port = int(os.environ.get("PORT", 8000))
    # Run uvicorn programmatically
    uvicorn.run("main:app", host="0.0.0.0", port=port)
