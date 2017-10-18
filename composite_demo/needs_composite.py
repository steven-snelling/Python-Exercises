from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, title, salary):
        self._name = name
        self._title = title
        self._salary = salary

    def add(self, employee):
        pass

    def remove(self, employee):
        pass

    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

    @property
    def salary(self):
        return self._salary

    @abstractmethod
    def to_string(self, tab):
        print("{}Name: {}, Title: {}, Salary: {}".format(
            tab, self._name, self._title, self._salary))


class Junior(Employee):
    def __init__(self, name, title, salary):
        super().__init__(name, title, salary)

    def to_string(self, tab):
        super().to_string(tab)


class Senior(Employee):
    def __init__(self, name, title, salary):
        super().__init__(name, title, salary)
        self._subordinates = []

    def add(self, employee):
        self._subordinates.append(employee)

    def remove(self, employee):
        self._subordinates.remove(employee)

    def to_string(self, tab):
        super().to_string(tab)
        for an_employee in self._subordinates:
            an_employee.to_string('\t' + tab)


if __name__ == '__main__':
    ceo = Senior("John", "CEO", 30000)
    head_sales = Senior("Robert", "Head Sales", 20000)
    head_marketing = Senior("Michel", "Head Marketing", 20000)

    ceo.add(head_sales)
    ceo.add(head_marketing)

    sales_executive1 = Junior("Richard", "Sales", 10000)
    sales_executive2 = Junior("Rob", "Sales", 10000)

    head_sales.add(sales_executive1)
    head_sales.add(sales_executive2)

    clerk1 = Junior("Laura", "Marketing", 10000)
    clerk2 = Junior("Bob", "Marketing", 10000)

    head_marketing.add(clerk1)
    head_marketing.add(clerk2)

    # print all _subordinates of the organization
    ceo.to_string('')

    ceo.remove(head_sales)
    ceo.to_string('')
