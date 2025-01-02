class Circle:
    def draw(self):
        print("Drawing a Circle")


class Square:
    def draw(self):
        print("Drawing a Square")


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str):
        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "square":
            return Square()
        else:
            return ValueError("Unknown shape type: {0}".format(shape_type))


if __name__ == "__main__":
    factory = ShapeFactory()
    shape1 = factory.create_shape("circle")
    shape1.draw()
    shape2 = factory.create_shape("square")
    shape2.draw()
