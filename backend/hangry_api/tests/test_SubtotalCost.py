from api.controllers import Subtotal
from tests.helpers import mock_model

def test_SimpleCost():
  #Arrange
  order = []
  order.append(mock_model(quantity=5, item=mock_model(price=1.0)))
  order.append(mock_model(quantity=5, item=mock_model(price=1.0)))
  order.append(mock_model(quantity=5, item=mock_model(price=1.0)))
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 15


def test_ComplexCost():
  #Arrange
  order = []
  order.append(mock_model(quantity=2, item=mock_model(price=3.5)))
  order.append(mock_model(quantity=1, item=mock_model(price=4.5)))
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 11.5
