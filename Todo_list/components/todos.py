from django_unicorn.components import UnicornView, QuerySetType
from Todo_list.models import Todos


class TodosView(UnicornView):
    # id: int = None
    name: str = ''
    todos: QuerySetType[Todos] = Todos.objects.none()

    def mount(self):
        self.todos = Todos.objects.all()

    def add_todo(self):
        if self.name == '':
            pass
        else:
            Todos.objects.create(name=self.name)
            self.todos = Todos.objects.all()
            self.name = ''

    def delete_all(self):
        Todos.objects.all().delete()
        self.todos = Todos.objects.none()

    def delete(self, id=None):

        # print(id)
        todo = Todos.objects.get(id=id)
        if todo is not None:
            todo.delete()
        else:
            pass
        self.todos = Todos.objects.all()
