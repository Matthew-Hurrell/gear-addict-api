from django.contrib.auth.models import User
from .models import Gear
from rest_framework import status
from rest_framework.test import APITestCase


class GearListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='michael', password='password1234')

    def test_can_list_gear(self):
        michael = User.objects.get(username='michael')
        Gear.objects.create(owner=michael, name='My test gear', value=2000)
        response = self.client.get('/gear/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_gear(self):
        self.client.login(username='michael', password='password1234')
        response = self.client.post(
            '/gear/',
            {'name': 'A gear name', 'value': 2000}
        )
        count = Gear.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_gear(self):
        response = self.client.post(
            '/gear/',
            {'name': 'A gear name', 'value': 2000}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GearDetailViewTests(APITestCase):
    def setUp(self):
        michael = User.objects.create_user(
            username='michael',
            password='password1234'
        )
        rosie = User.objects.create_user(
            username='rosie',
            password='password1234'
        )
        Gear.objects.create(
            owner=michael,
            name='Michael gear',
            description='This gear is awesome',
            value=2000
        )
        Gear.objects.create(
            owner=rosie,
            name='Rosie gear',
            description='This gear is sweet',
            value=2000
        )

    def test_can_retrieve_gear_using_valid_id(self):
        response = self.client.get('/gear/1/')
        self.assertEqual(response.data['name'], 'Michael gear')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_fetch_gear_by_invalid_id(self):
        response = self.client.get('/gear/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_gear(self):
        self.client.login(username='michael', password='password1234')
        response = self.client.put('/gear/1/', {'name': 'Michaels new gear'})
        gear = Gear.objects.filter(pk=1).first()
        self.assertEqual(gear.name, 'Michaels new gear')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_cant_update_gear_they_dont_own(self):
        self.client.login(username='rosie', password='password1234')
        response = self.client.put(
            '/gear/1/',
            {'name': 'This is rosies gear now!'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_logged_in_user_cannot_update_gear(self):
        response = self.client.put('/gear/1/', {'name': 'Anonymous was here!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_gear(self):
        self.client.login(username='michael', password='password1234')
        response = self.client.delete('/gear/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_gear_they_dont_own(self):
        self.client.login(username='rosie', password='password1234')
        response = self.client.delete('/gear/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_logged_in_user_cant_delete_gear(self):
        response = self.client.delete('/gear/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
