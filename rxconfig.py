import reflex as rx
import os

# Get PORT from Render environment, default to 8000 for local dev
port = int(os.getenv("PORT", "8000"))
print(f"[RXCONFIG] Using PORT: {port}")
print(f"[RXCONFIG] Binding to: 0.0.0.0:{port}")

config = rx.Config(
    app_name="job_organizer",
    # CRITICAL: Must bind to 0.0.0.0 for Render to detect
    frontend_host="0.0.0.0",
    backend_host="0.0.0.0",
    backend_port=port,
    frontend_port=port,  # Use same port for frontend
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
