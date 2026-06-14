from api.controllers import Delivery
from tests.helpers import mock_model

def test_LotsOfItems():
  #Arrange
  order = []
  order.append(mock_model(quantity=3))
  order.append(mock_model(quantity=1))
  delivery_distance = 2
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 3.5

def test_MiddleOfTheRoadItems():
  #Arrange
  order = []
  order.append(mock_model(quantity=2))
  order.append(mock_model(quantity=2))
  order.append(mock_model(quantity=2))
  delivery_distance = 4
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 5

def test_LittleItems():
 #Arrange
  order = []
  order.append(mock_model(quantity=3))
  order.append(mock_model(quantity=1))
  delivery_distance = 2
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 3.50
  pass
