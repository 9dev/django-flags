from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse


CHROMEDRIVER_PATH = '/usr/bin/chromedriver'


class BaseTestCase(StaticLiveServerTestCase):
    fixtures = ['base.json']

    def setUp(self):
        self.browser = webdriver.Chrome(CHROMEDRIVER_PATH)

    def tearDown(self):
        self.browser.close()

    def reopen_browser(self):
        self.browser.close()
        self.browser = webdriver.Chrome(CHROMEDRIVER_PATH)

    def get(self, url=None, name=None, *args, **kwargs):
        if name:
            url = reverse(name, *args, **kwargs)
        self.browser.get('{}{}'.format(self.live_server_url, url))

    def login_as_admin(self):
        self.get(url='/admin')
        self.set_field('id_username', 'admin')
        self.set_field('id_password', 'admin')
        self.submit()

    def login_as_regular_user(self):
        self.get(url='/login')
        self.set_field('id_username', 'test_user1')
        self.set_field('id_password', 'admin')
        self.submit()

    def get_by_id(self, selector):
        return self.browser.find_element_by_id(selector)

    def set_field(self, field_id, value):
        field = self.get_by_id(field_id)
        field.clear()
        field.send_keys(value)

    def submit(self):
        form = self.browser.find_element_by_tag_name('form')
        form.submit()

    def get_text(self):
        return self.browser.find_element_by_tag_name('body').text
