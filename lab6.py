class Student:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.id = 0

class ObjectPool:
    def __init__(self):
        self.objects_list = []
        self.max_objects = 5
        self.counter = 0

    def get_object(self):
        if self.counter > 0:
            obj = self.objects_list.pop(0)
            self.counter -= 1
            return obj
        return Student()

    def release_object(self, item):
        if self.counter < self.max_objects:
            self.objects_list.append(item)
            self.counter += 1

# Пример использования
obj_pool = ObjectPool()

obj = obj_pool.get_object()
print("First object assigned")
obj_pool.release_object(obj)
count = obj_pool.counter
print("First object released back into the pool")
print("Current count of pool:", count)

obj2 = obj_pool.get_object()
print("Second object assigned")
count = obj_pool.counter
print("Current count of pool:", count)
obj_pool.release_object(obj2)
