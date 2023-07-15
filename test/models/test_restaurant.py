import pytest

from src.models.restaurant import Restaurant
import io
import sys

class TestRestaurant:

    def test_describe_restaurant(before_each):
        nome = 'Salgadinho da Marina'
        tipo = 'Salgados Diversos'
        qtd_consumidores = 0
        resultado_esperado = f"Esse restaurante chama {nome} e serve {tipo}.\n" + \
                             f"Esse restaurante está servindo {qtd_consumidores} consumidores desde que está aberto.\n"

        captura_saida = io.StringIO()
        sys.stdout = captura_saida

        user = Restaurant(restaurant_name=nome, cuisine_type=tipo)
        user.describe_restaurant()

        sys.stdout = sys.__stdout__
        saida_impressa = captura_saida.getvalue()

        assert saida_impressa == resultado_esperado, "A descrição do restaurante não bate com o valor esperado"

    def test_open_restaurant(self):
        nome = 'Salgadinho da Marina'
        tipo = 'Salgados Diversos'
        resultado_esperado = f"{nome} agora está aberto!\n"

        captura_saida = io.StringIO()
        sys.stdout = captura_saida

        user = Restaurant(restaurant_name=nome, cuisine_type=tipo)
        user.open_restaurant()

        sys.stdout = sys.__stdout__
        saida_impressa = captura_saida.getvalue()

        assert saida_impressa == resultado_esperado, "A mensagem de abertura de restaurante não bate com o valor esperado"

    def test_close_restaurant(self):
        nome = 'Salgadinho da Marina'
        tipo = 'Salgados Diversos'
        resultado_esperado = f"{nome} agora está fechado!\n"


        user = Restaurant(restaurant_name=nome, cuisine_type=tipo)
        user.open_restaurant()

        captura_saida = io.StringIO()
        sys.stdout = captura_saida
        user.close_restaurant()


        sys.stdout = sys.__stdout__
        saida_impressa = captura_saida.getvalue()

        assert saida_impressa == resultado_esperado, "A mensagem de abertura de restaurante não bate com o valor esperado"

    def test_set_number_served(self):
        nome = 'Salgadinho da Marina'
        tipo = 'Salgados Diversos'
        qtd_consumidores = 10
        resultado_esperado = qtd_consumidores

        user = Restaurant(restaurant_name=nome, cuisine_type=tipo)
        user.open_restaurant()
        user.set_number_served(total_customers=qtd_consumidores)

        assert user.number_served == resultado_esperado

    def test_increment_number_served(self):
        nome = 'Salgadinho da Marina'
        tipo = 'Salgados Diversos'
        qtd_consumidores = 10
        add_mais_consumidores = 40
        total_consumidores = qtd_consumidores + add_mais_consumidores

        user = Restaurant(restaurant_name=nome, cuisine_type=tipo)
        user.open_restaurant()
        user.set_number_served(total_customers=qtd_consumidores)

        user.increment_number_served(add_mais_consumidores)

        assert user.number_served == total_consumidores
