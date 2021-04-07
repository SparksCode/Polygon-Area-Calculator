class Rectangle:
  def __init__(self, height, width):
    self.height = height
    self.width = width

  def set_height(self, height):
    return ""

  def set_width(self, width):
    return ""

  def get_amount_inside(self):
    return ""

  def get_area(self):
    return ""

  def get_diagonal(self):
    return ""

  def get_perimeter(self):
    return ""

  def get_picture(self):
    return ""

class Square(Rectangle):

  def __init__(self, width):
    self.height = width
    self.width = width

  def set_side(self, width):
    return ""