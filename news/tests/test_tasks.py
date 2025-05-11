import pytest
from django.utils.timezone import now
from feed_reader.models import Feed
from your_app.tasks import update_all_feeds

@pytest.mark.django_db
def test_update_all_feeds_task_success(monkeypatch):
    # Setup: create a mock feed
    feed = Feed.objects.create(
        title="Test Feed",
        feed_url="http://example.com/rss.xml",
        site_url="http://example.com",
        is_active=True,
    )

    # Monkeypatch the fetch method to avoid real HTTP call
    def mock_fetch(self):
        self.title = "Updated Title"
    
    monkeypatch.setattr(Feed, "fetch", mock_fetch)

    # Run the task
    update_all_feeds()

    # Refresh and assert
    feed.refresh_from_db()
    assert feed.title == "Updated Title"
    assert feed.last_fetched is not None
