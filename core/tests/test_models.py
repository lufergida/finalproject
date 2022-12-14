from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Prueba para crear un nuevo usuario correctamente"""
        email = 'lufergida@gmail.com'
        password = 'luisa123'
        user = get_user_model().objects.create_user(
            email= email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Prueba de email para un usuario normalizado"""
        email = 'lufergida@gmail.com'
        user = get_user_model().objects.create_user(email,'luisa123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Nuevo usuario email invalido"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'luisa123')

    def test_create_new_superuser(self):
        """Probar super usuario creado"""
        email = 'lufergida@gmail.com'
        password = 'luisa123'
        user = get_user_model().objects.create_superuser(
            email= email,
            password = password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)