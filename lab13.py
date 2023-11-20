from abc import ABC, abstractmethod


# Спільний інтерфейс (Subject)
class UniversityResource(ABC):
    @abstractmethod
    def access_resource(self):
        pass


# Реальний об'єкт (Real Subject)
class RealUniversityResource(UniversityResource):
    def access_resource(self):
        print("Доступ до реального університетського ресурсу")


# Заступник (Proxy)
class ProxyUniversityResource(UniversityResource):
    def __init__(self, real_resource):
        self.real_resource = real_resource

    def access_resource(self):
        if self.check_access():
            self.real_resource.access_resource()
        else:
            print("Доступ заборонено")

    def check_access(self):
        # Логіка перевірки доступу, наприклад, перевірка рівня прав або аутентифікація
        return True


# Клієнтський код
if __name__ == "__main__":
    real_resource = RealUniversityResource()
    proxy_resource = ProxyUniversityResource(real_resource)

    # Клієнт взаємодіє з ресурсом через заступник
    proxy_resource.access_resource()
