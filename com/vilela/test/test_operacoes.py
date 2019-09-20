from unittest import TestCase
from com.vilela.operacoes import Multiplicacao

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Multiplicacao()
	
	def test_mult(self):
		sel.assertEqual(sel.operacoes.mult([5,5]), 25, "Resultado 25" )