class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, num):
    self.width = num

  def set_height(self, num):
    self.height = num

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    perimeter = 2 * (self.width + self.height)
    return perimeter

  def get_diagonal(self):
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal

  def get_picture(self):
    width = self.width
    height = self.height

    if width > 50 or height > 50:
      return 'Too big for picture.'

    picture = ''

    for row in range(height):
      picture += '*' * width + '\n'

    return picture

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def set_side(self, num):
    self.height = num
    self.width = num

  def __str__(self):
    return f'Square(side={self.width})'
