import reflex as rx
import os

# Get PORT from Render environment, default to 8000 for local dev
port = int(os.getenv("PORT", "8000"))
print(f"[RXCONFIG] Using PORT: {port}")
print(f"[RXCONFIG] Binding to: 0.0.0.0:{port}")

config = rx.Config(
    app_name="job_organizer",
    # Backend configuration
    backend_host="0.0.0.0",
    backend_port=port,
    # Frontend configuration - MUST use same port as backend
    frontend_port=port,
    # Disable plugins
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
