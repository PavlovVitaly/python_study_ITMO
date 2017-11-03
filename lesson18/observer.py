# Observer
from abc import ABCMeta, abstractmethod
from random import randrange


class Event(metaclass=ABCMeta):
    def __init__(self, event_name):
        self.event_name = event_name


class Subject(object):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        assert isinstance(observer, Observer)
        self._observers.append(observer)

    def remove_observer(self, observer):
        assert isinstance(observer, Observer)
        self._observers.remove(observer)

    def notify_observers(self, event):
        assert isinstance(event, Event)
        for observer in self._observers:
            observer.handle_event(event)


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def handle_event(self, event):
        pass


class Login(Subject):
    def __init__(self):
        super().__init__()
        self.result = None

    def authorize(self, user, pswd):
        """
        0 - успешный вход
        1 - щшибка в воде пароля или имени пользователя
        2 - ошибка провайдера Ростелеком
        """
        self.result = randrange(3)
        event = LoginEvent(self.result)
        self.notify_observers(event)


class ErrorObserver(Observer):
    def handle_event(self, event):
        if event.result == 0:
            print("Error to log")


class LoggerObserver(Observer):
    def handle_event(self, event):
        if event.result == 1:
            print("Write to log")


class CookieObserver(Observer):
    def handle_event(self, event):
        if event.result == 2:
            print('Send Cookie')


class LoginEvent(Event):
    def __init__(self, result):
        super().__init__('login')
        self.result = result


login_handler = Login()
login_handler.add_observer(LoggerObserver())
login_handler.add_observer(ErrorObserver())
login_handler.add_observer(CookieObserver())
login_handler.authorize('root', 'toor')
