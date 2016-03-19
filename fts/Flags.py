from ._base import BaseTestCase

from main.models import Article


class TestFlags(BaseTestCase):

    def setUp(self):
        super(TestFlags, self).setUp()
        self.obj = Article.objects.create(title='My first article', content='Some content')

    def test_registered_user_can_flag_an_object(self):
        # Florence logs in as an admin.
        self.login_as_admin()

        # She hits a detail page for an Article object.
        pk = Article.objects.latest('pk').pk
        self.get('/article/{}'.format(pk))

        # She clicks on a link to flag the object.
        self.browser.find_element_by_partial_link_text('Report abuse').click()

        # She confirms she want to flag this article.
        self.submit()

        # She hits flags admin panel.
        self.get('/admin/flags/flag')

        # She sees a new flag object.
        self.assertIn('<Article id={}>'.format(self.obj.pk), self.get_text())

    def test_unregistered_user_cannot_flag_an_object(self):
        self.fail()

    def test_cannot_flag_object_if_approved(self):
        self.fail()

    def test_object_is_removed_after_hitting_flag_threshold_if_threshold_set(self):
        self.fail()

    def test_object_is_never_removed_if_threshold_not_set(self):
        self.fail()
