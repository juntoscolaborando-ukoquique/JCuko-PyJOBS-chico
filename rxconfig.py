import reflex as rx
import os

# Get PORT from Render environment, default to 8000 for local dev
port = int(os.getenv("PORT", "8000"))

config = rx.Config(
    app_name="job_organizer",
    backend_host="0.0.0.0",
    backend_port=port,
    frontend_port=port,  # Use same port for frontend
)
