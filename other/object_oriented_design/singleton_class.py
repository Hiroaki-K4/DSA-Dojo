class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value


if __name__ == "__main__":
    obj1 = Singleton("First")
    obj2 = Singleton("Second")

    print(obj1 is obj2)
    print(obj1.value)
