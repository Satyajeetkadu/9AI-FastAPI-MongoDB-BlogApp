from fastapi import APIRouter

entry_root = APIRouter()

@entry_root.get("/")
def apiRunning():
    """
    Endpoint to check if the API is running.

    Returns:
        dict: Response containing the status and message indicating the API is running.
    """
    res = {
        "status": "ok",
        "message": "API is running"
    }
    return res
