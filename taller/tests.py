from django.test import TestCase
from datetime import datetime
from taller.validaciones import ValMail, ValCelular, ValEdadGrupo
from taller.models import Contacto

# Create your tests here.
# class ValMailTestCase(TestCase):
#     def setUp(self):
#         pass
#     def test_casos(self):
#         self.assertEqual(ValMail ('a@c'), False)
#         self.assertEqual(ValMail ('a@g.c'), True)
#         self.assertEqual(ValMail ('aB_0.-@gM9.cO5.'), True)

# class ValCelularTestCase(TestCase):
#     def setUp(self):
#         pass
#     def test_casos(self):
#         self.assertEqual(ValCelular('(54)(11)(15)1111-9999'), True)
#         self.assertEqual(ValCelular('15 1111-9999'), True)
#         self.assertEqual(ValCelular('11119999') , True)

# class ValEdadGrupoTestCase(TestCase):
#     def setUp(self):
#         pass
#     def test_casos(self):
#         self.assertEqual(ValEdadGrupo('N',datetime.strptime('2000-01-01','%Y-%m-%d')), True)
#         self.assertEqual(ValEdadGrupo('N',datetime.strptime('2020-01-01','%Y-%m-%d')), False)
#         self.assertEqual(ValEdadGrupo('J',datetime.strptime('2000-01-01','%Y-%m-%d')), False)
#         self.assertEqual(ValEdadGrupo('J',datetime.strptime('2018-01-01','%Y-%m-%d')), True)
#         self.assertEqual(ValEdadGrupo('A',datetime.strptime('2000-01-01','%Y-%m-%d')), True)
