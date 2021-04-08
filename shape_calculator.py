class Rectangle:
  def __init__(self, width, height):
    self.height = height
    self.width = width

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_height(self, height):
    self.height = height

  def set_width(self, width):
    self.width = width

  def get_amount_inside(self, rectangle):
    if rectangle.get_area() > self.get_area():
      return 0
    return self.get_area() // rectangle.get_area()

  def get_area(self):
    return self.width * self.height

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_picture(self):
    picture = ""
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    for i in range(0, self.height, 1):
      picture += "*" * self.width + "\n"
    return picture

class Square(Rectangle):

  def __init__(self, width):
    self.height = width
    self.width = width

  def __str__(self):
    return f"Square(side={self.width})"
  def set_side(self, width):
    self.height = width
    self.width = width