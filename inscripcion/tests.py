from django.test import TestCase

from .models import Estudiante


class TestEstudiante(TestCase):
    # fixtures = ['dump_inventario.json']

    def test_grabacion(self):
        q =  Estudiante(nombres="Elio")
        q.save()
        self.assertEqual(Estudiante.objects.count(), 1)
