class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name #bug: funcao title() estava colocando a primeira letra maiuscula mesmo enviando essa letra minuscula, retiramos o title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        print(f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}.") #bug: palavras 'restaurante' e 'and' foram alteradas - bug2: o nome do restaurante estava chamando a variável cuisine_type quando deveria chamar a variável restaurant_name
        print(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True #bug: ajuste da variável para True, pois o restaurante está abrindo
            self.number_served = 0 #bug: o restaurante já abria com consumidores negativos  - melhoria tirar essa linha
            print(f"{self.restaurant_name} agora está aberto!")
        else:
            print(f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            print(f"{self.restaurant_name} agora está fechado!")
        else:
            print(f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
        else:
            print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers #bug: variável não estava incrementando
        else:
            print(f"{self.restaurant_name} está fechado!")
