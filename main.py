from src.models.ice_cream_stand import IceCreamStand
from src.models.restaurant import Restaurant

abrir = Restaurant(restaurant_name='Mari cake shop', cuisine_type='Patisserie')
a = abrir.open_restaurant()
a = abrir.open_restaurant()
b = abrir.describe_restaurant()


sorveteria = IceCreamStand(restaurant_name='Renas Burguer', cuisine_type='Haburgue', flavors_list='Morango, Chocolate, Nutella')
disponivel = sorveteria.flavors_available()
ache = sorveteria.find_flavor(flavor='Morango')
add = sorveteria.add_flavor(flavor='Flocos')
