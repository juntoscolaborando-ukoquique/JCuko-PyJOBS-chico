import reflex as rx
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
DEFAULT_PORT: int = 8000
DEFAULT_FRONTEND_PORT: int = 3000

# Get PORT from Render environment, default to 8000 for local dev
port: int = int(os.getenv("PORT", str(DEFAULT_PORT)))
is_production: bool = os.getenv("ENVIRONMENT") == "production"

logger.info(f"Using PORT: {port}")
logger.info(f"Environment: {'production' if is_production else 'development'}")
logger.info(f"Binding to: 0.0.0.0:{port}")

config = rx.Config(
    app_name="job_organizer",
    # Backend configuration
    backend_host="0.0.0.0",
    backend_port=port,
    # Frontend configuration - Use same port in production (Render), separate in development
    frontend_port=port if is_production else DEFAULT_FRONTEND_PORT,
    # Disable plugins
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
