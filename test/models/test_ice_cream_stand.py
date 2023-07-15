from src.models.ice_cream_stand import IceCreamStand
import io
import sys


class TestIceCreamStand:

    def test_flavors_available(self):
        nome = 'Sorveteria Doce Sabor'
        tipo = 'Sorveteria'
        sabores = ['Morango, Chocolate, Nutella']

        resultado_esperado = f'No momento temos os seguintes sabores de sorvete disponíveis: {", ".join(sabores)}'

        captura_saida = io.StringIO()
        sys.stdout = captura_saida

        user = IceCreamStand(restaurant_name=nome, cuisine_type=tipo, flavors_list=sabores)
        user.flavors_available()

        sys.stdout = sys.__stdout__
        resultado = captura_saida.getvalue().replace('\n-', '').strip()

        assert resultado == resultado_esperado

    def test_find_flavor(self):
        nome = 'Sorveteria Doce Sabor'
        tipo = 'Sorveteria'
        sabores = 'Morango, Chocolate, Nutella'

        resultado_esperado = f'Temos no momento {sabores}!'

        captura_saida = io.StringIO()
        sys.stdout = captura_saida

        user = IceCreamStand(restaurant_name=nome, cuisine_type=tipo, flavors_list=sabores)
        user.find_flavor(flavor='Morango')

        sys.stdout = sys.__stdout__
        resultado = captura_saida.getvalue().strip()

        assert resultado == resultado_esperado

    def test_add_flavor(self):
        nome = 'Sorveteria Doce Sabor'
        tipo = 'Sorveteria'
        sabores = ['Morango, Chocolate, Nutella']
        sabor = 'Tamarindo'

        resultado_esperado = f'{sabor} adicionado ao estoque!'

        captura_saida = io.StringIO()
        sys.stdout = captura_saida

        user = IceCreamStand(restaurant_name=nome, cuisine_type=tipo, flavors_list=sabores)
        user.add_flavor(flavor=sabor)

        sys.stdout = sys.__stdout__
        resultado = captura_saida.getvalue().strip()

        assert resultado == resultado_esperado
