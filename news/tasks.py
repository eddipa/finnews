from celery import shared_task
from celery.exceptions import Retry
from feeds.utils import update_feeds
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def update_all_feeds(self):
    """
    Refreshes all active feed URLs stored in the database.
    Retries failed feed fetches up to 3 times.
    """
    try:
        logger.info(f"Fetching feeds")
        update_feeds(50)# this number can be changed or simply extracted
    except Exception as e:
        logger.error(f"Failed to fetch {feed.feed_url}: {str(e)}")
        try:
            raise self.retry(exc=e)
        except Retry:
            logger.warning(f"Retrying fetch for feeds after delay...")
