from django.contrib.auth.models import User
from .models import Rig
from rest_framework import status
from rest_framework.test import APITestCase


class RigListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='george', password='password1234')

    def test_can_list_rigs(self):
        george = User.objects.get(username='george')
        Rig.objects.create(owner=george, name='My test rig')
        response = self.client.get('/rigs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_rig(self):
        self.client.login(username='george', password='password1234')
        response = self.client.post('/rigs/', {'name': 'A rig name'})
        count = Rig.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_rig(self):
        response = self.client.post('/rigs/', {'name': 'A rig name'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RigDetailViewTests(APITestCase):
    def setUp(self):
        brian = User.objects.create_user(
            username='brian',
            password='password1234'
        )
        jonathon = User.objects.create_user(
            username='jonathon',
            password='password1234'
        )
        Rig.objects.create(
            owner=brian,
            name='Brian rig',
            description='This rig is awesome'
        )
        Rig.objects.create(
            owner=jonathon,
            name='Jonathon rig',
            description='This rig is sweet'
        )

    def test_can_retrieve_rig_using_valid_id(self):
        response = self.client.get('/rigs/1/')
        self.assertEqual(response.data['name'], 'Brian rig')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_fetch_rig_by_invalid_id(self):
        response = self.client.get('/rigs/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_rig(self):
        self.client.login(username='brian', password='password1234')
        response = self.client.put('/rigs/1/', {'name': 'Brians new rig'})
        rig = Rig.objects.filter(pk=1).first()
        self.assertEqual(rig.name, 'Brians new rig')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_cant_update_rig_they_dont_own(self):
        self.client.login(username='jonathon', password='password1234')
        response = self.client.put(
            '/rigs/1/',
            {'name': 'This is jonathons rig now!'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_logged_in_user_cannot_update_rig(self):
        response = self.client.put('/rigs/1/', {'name': 'Anonymous was here!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_rig(self):
        self.client.login(username='brian', password='password1234')
        response = self.client.delete('/rigs/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_rig_they_dont_own(self):
        self.client.login(username='jonathon', password='password1234')
        response = self.client.delete('/rigs/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_logged_in_user_cant_delete_rig(self):
        response = self.client.delete('/rigs/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
