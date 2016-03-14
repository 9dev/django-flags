from ._base import BaseTestCase


class TestFlags(BaseTestCase):

    def test_registered_user_can_flag_an_object(self):
        self.fail()

    def test_unregistered_user_cannot_flag_an_object(self):
        self.fail()

    def test_cannot_flag_object_if_approved(self):
        self.fail()

    def test_object_is_removed_after_hitting_flag_threshold_if_threshold_set(self):
        self.fail()

    def test_object_is_never_removed_if_threshold_not_set(self):
        self.fail()
