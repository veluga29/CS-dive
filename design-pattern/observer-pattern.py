from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register(self, observer: Observer):
        pass

    @abstractmethod
    def unregister(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def get_update(self):
        pass


class Topic(Subject):
    def __init__(self):
        self.observers: set[Observer] = set()
        self.message: str = ""

    def register(self, observer: Observer):
        if observer not in self.observers:
            self.observers.add(observer)

    def unregister(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def get_update(self):
        return self.message

    def post_message(self, message):
        print("Message sended to Topic: " + message)
        self.message = message
        self.notify()


class TopicSubscriber(Observer):
    def __init__(self, name: str, topic: Topic):
        self.name = name
        self.topic = topic

    def update(self):
        message = self.topic.get_update()
        print(f"{self.name} received message: {message}")


topic: Topic = Topic()
c: Observer = TopicSubscriber("Charmander", topic)
b: Observer = TopicSubscriber("Bulbasaur", topic)
s: Observer = TopicSubscriber("Squirtle", topic)
topic.register(c)
topic.register(b)
topic.register(s)

topic.post_message("Pikachu win the battle!")
