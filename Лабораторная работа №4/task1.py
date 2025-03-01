class Vehicle:
    """Базовый класс для всех транспортных средств."""

    def __init__(self, make: str, model: str):
        """Инициализирует экземпляр транспортного средства.

        Args:
            make: Производитель транспортного средства.
            model: Модель транспортного средства.
        """
        self.__make = make  # Инкапсуляция для предотвращения изменения
        self.__model = model  # Инкапсуляция для предотвращения изменения

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self.__make} {self.__model}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление транспортного средства."""
        return f"Vehicle(make='{self.__make}', model='{self.__model}')"


class Car(Vehicle):
    """Класс для легковых автомобилей, наследуемый от Vehicle."""

    def __init__(self, make: str, model: str, doors: int):
        """Инициализирует экземпляр легкового автомобиля.

        Args:
            make: Производитель легкового автомобиля.
            model: Модель легкового автомобиля.
            doors: Количество дверей.
        """
        super().__init__(make, model)  # Вызов конструктора базового класса
        self.__doors = doors  # Инкапсуляция для предотвращения изменения

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} with {self.__doors} doors"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление легкового автомобиля."""
        return f"Car(make='{self._Vehicle__make}', model='{self._Vehicle__model}', doors={self.__doors})"

    def drive(self) -> str:
        """Симуляция движения автомобиля.

        Returns:
            Строка, описывающая движение.
        """
        return f"{self.__make} {self.__model} is driving."

    def drive(self) -> str:
        """Симуляция движения автомобиля с дополнительным описанием.

        Returns:
            Строка, описывающая движение.

        Переопределяющий метод добавляет свойства автомобиля к описанию.
        """
        return f"The {self.__doors}-door {self.__make} {self.__model} is driving smoothly."


class Truck(Vehicle):
    """Класс для грузовых автомобилей, наследуемый от Vehicle."""

    def __init__(self, make: str, model: str, capacity: float):
        """Инициализирует экземпляр грузового автомобиля.

        Args:
            make: Производитель грузового автомобиля.
            model: Модель грузового автомобиля.
            capacity: Грузоподъемность в тоннах.
        """
        super().__init__(make, model)  # Вызов конструктора базового класса
        self.__capacity = capacity  # Инкапсуляция для предотвращения изменения

    def __str__(self) -> str:
        """Возвращает строковое представление грузового автомобиля."""
        return f"{super().__str__()} with capacity of {self.__capacity} tons"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление грузового автомобиля."""
        return f"Truck(make='{self._Vehicle__make}', model='{self._Vehicle__model}', capacity={self.__capacity})"

    def load(self, weight: float) -> str:
        """Загрузка груза в автомобиль.

        Args:
            weight: Вес загружаемого груза в тоннах.

        Returns:
            Строка, подтверждающая загрузку.

        Документация подразумевает, что груз не может превышать грузоподъемность.
        """
        if weight > self.__capacity:
            return f"Cannot load {weight} tons. Exceeds capacity of {self.__capacity} tons."
        return f"Loaded {weight} tons in {self.__make} {self.__model}."
