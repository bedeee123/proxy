from abc import ABC, abstractmethod
import datetime

class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):

    def request(self) -> None:
        return "RealSubject: Handling request."

class Proxy(Subject):

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self,x):
        if self.check_access(x):
            real = self._real_subject.request()
            date = self.log_access()
            return f"{real}\n{date}"
        else:
            return "Access Denied"

    def check_access(self,x) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        if x == 0:
            return True
        else:
            return False

    def log_access(self) -> None:
        date = datetime.datetime.now()
        return f"Proxy Log: {date}"

if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    print(real_subject.request())

    print("")

    print("Client: Executing the same client code with a proxy:")
    access=0
    proxy = Proxy(real_subject)
    print(proxy.request(access))