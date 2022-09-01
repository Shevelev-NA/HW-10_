import json


class Utils:
    """---> class создал новый экземпляр класса!\n"""

    def __init__(self, pk=None, name=None, picture=None, position=None, gender=None, age=None, skills=None):
        print(self.__class__.__name__, self.__doc__)
        self.path = None  # Загруженные данные из файла
        self.pk = pk
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills
        self.arr = []  # список всех кандидатов

    def load_candidates(self, filename):
        """ Загружает данные из файла"""
        with open(filename, 'r', encoding='utf-8') as f:
            self.path = json.load(f)
        return self.path

    def get_all(self):
        """Показывает всех кандидатов"""
        # arr = [] # список всех кандидатов
        for item in self.path:
            # self.pk = item['pk']
            # self.name = item['name']
            # self.picture = item['picture']
            # self.position = item['position']
            # self.gender = item['gender']
            # self.age = item['age']
            # self.skills = item['skills']
            # arr.append(Utils(self.pk, self.name, self.picture, self.position, self.gender, self.age, self.skills))

            self.arr.append(
                Utils(item['pk'], item['name'], item['picture'], item['position'], item['gender'], item['age'],
                      item['skills']))
        return self.arr

    def get_by_pk(self, pk):
        """Вернет кандидата по pk"""
        for item in self.arr:
            if item.pk == pk:
                return item


    def get_by_skill(self, skill_name):
        """Вернет кандидатов по навыку"""
        arr_skill = []  # Список кандидатов по навыку
        for item in self.arr:
            for i in [item.skills.lower()]:
                if skill_name.lower() in i:
                    arr_skill.append(item)
        return arr_skill

    def __repr__(self):
        return f"{self.pk} {self.name} {self.picture} {self.position} {self.gender} {self.age} {self.skills}"

    def __str__(self):
        return f"{self.pk} {self.name} {self.picture} {self.position} {self.gender} {self.age} {self.skills}"




""" Для тестирования работы функций"""

# req = Utils()
#
# req.load_candidates('candidates.json')
#
# print(req.get_all())
#
# print(req.get_by_pk(7))
#
# print(req.get_by_skill('пользоваться календарем'))
