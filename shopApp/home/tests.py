from django.test import TestCase
from django.urls import reverse, resolve
from .views import index, board_topics
from .models import Board


# Create your tests here.


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/home/')
        self.assertEquals(view.func, index)


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    # def test_board_topics_view_success_status_code(self):
    #     url = reverse('topic', kwargs={'pk': 1})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('home/1/')
        self.assertEquals(view.func, board_topics)
