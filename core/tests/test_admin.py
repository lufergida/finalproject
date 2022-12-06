from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class adminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'lufergida@gmail.com',
            password = 'luisa123'

        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='luisatest@gmail.com',
            password= 'luisa',
            name= 'test user nombre completo'
        )

    def test_users_listed(self):
        """Prueba de que los usuarios estan enlistados en la pagina de usuario"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Prueba que la pagina editada por el usuario funciona"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Prueba de que la página de crear usuarios funciona"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)




