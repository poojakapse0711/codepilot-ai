from app.core.logging import configure_logging

import logging

configure_logging()

logger = logging.getLogger(__name__)

logger.info("Logging configured successfully")