from unittest import TestCase
from com.vilela.operacoes import Elevador
elevador = Elevador(5, 20)

class TestOperacoes(TestCase):

	#def setUp(self):
		#self.elevador = Elevador(5, 20)
		

	def test_elevador1():
		assert elevador.andar_atual == 0
		assert elevador.quantidade_pessoas == 0
