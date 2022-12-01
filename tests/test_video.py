from playwright.sync_api import sync_playwright
from forms.play import Play


class Video(Play):
    def test_new(self):
        login_form = Play()
        login_form.search()

