from selenium.webdriver.support.ui import Select

from django.contrib.auth.models import User

from flags.models import Approve, Flag

from main.models import Article

from ._base import BaseTestCase


class TestFlags(BaseTestCase):

    def setUp(self):
        super(TestFlags, self).setUp()
        self.obj = Article.objects.create(title='My first article', content='Some content')

    def test_registered_user_can_flag_an_object(self):
        # Florence logs in as an admin.
        self.login_as_admin()

        # She hits a detail page for an Article object.
        self.get('/article/{}'.format(self.obj.pk))

        # She clicks on a link to flag the object.
        self.browser.find_element_by_partial_link_text('Report abuse').click()

        # She confirms she want to flag this article.
        self.submit()

        # She hits flags admin panel.
        self.get('/admin/flags/flag')

        # She sees a new flag object.
        self.assertIn('<Article id={}>'.format(self.obj.pk), self.get_text())

    def test_unregistered_user_cannot_flag_an_object(self):
        # Florence hits a detail page for an Article object.
        self.get('/article/{}'.format(self.obj.pk))

        # She clicks on a link to flag the object.
        self.browser.find_element_by_partial_link_text('Report abuse').click()

        # She is asked to log in first.
        self.assertEqual(
            self.browser.current_url,
            '{}/accounts/login/?next=/flags/create/main/article/{}'.format(self.live_server_url, self.obj.pk)
        )

    def test_can_approve_an_object(self):
        # There is a flagged Article object.
        Flag.objects.create(content_object=self.obj, creator=User.objects.get(pk=1))

        # Florence logs in as an admin.
        self.login_as_admin()

        # She hits flags admin panel.
        self.get('/admin/flags/flag')

        # She approves an Article object.
        self.get_by_id('action-toggle').click()
        select = Select(self.browser.find_element_by_css_selector('select[name="action"]'))
        select.select_by_visible_text('Approve')
        self.browser.find_element_by_css_selector('button[name="index"]').click()

        # She confirms that existing flag for an object disappeared.
        self.assertIn('0 flags', self.get_text())

    def test_cannot_flag_object_if_approved(self):
        # There is an approved object.
        Approve.objects.create(content_object=self.obj, creator=User.objects.get(pk=1))

        # Florence logs in as an admin.
        self.login_as_admin()

        # She hits a detail page for an Article object.
        self.get('/article/{}'.format(self.obj.pk))

        # She clicks on a link to flag the object.
        self.browser.find_element_by_partial_link_text('Report abuse').click()

        # She confirms she want to flag this article.
        self.submit()

        # She hits flags admin panel.
        self.get('/admin/flags/flag')

        # She doesn't see any new flag object.
        self.assertIn('0 flags', self.get_text())

    def test_object_is_removed_after_hitting_flag_threshold_if_threshold_set(self):
        self.fail()

    def test_object_is_never_removed_if_threshold_not_set(self):
        self.fail()
