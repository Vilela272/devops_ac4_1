from unittest import TestCase
from com.vilela.operacoes import Elevador

class TestOperacoes(TestCase):

	def setUp(self):
		self.elevador = Elevador(5, 20)
		

	def test_elevador1():
		self.assertEqual(self.operacoes.elevador.andar_atual == 0
		self.assertEqual(self.operacoes.elevador.quantidade_pessoas == 0
