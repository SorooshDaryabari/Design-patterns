class Singleton:
    __shared_instance = "Singleton"

    @staticmethod
    def get_instance():
        if Singleton.__shared_instance == "Singleton":
            Singleton()
        return Singleton.__shared_instance

    def __init__(self):
        if Singleton.__shared_instance != "Singleton":
            raise Exception("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self


if __name__ == "__main__":
    obj = Singleton()
    print(obj)

    obj = Singleton.get_instance()
    print(obj)
