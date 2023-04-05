from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        try:
            list(filter(lambda x: x.name == task_name, self.tasks))[0].completed = True
            # current_task.completed = True
            # self.tasks.append(current_task)
            return f'Completed task {task_name}'
        except IndexError:
            return f'Could not find task with the name {task_name}'

    def clean_section(self):
        new_tasks_list = list(filter(lambda x:  x.completed is not True, self.tasks))
        removed_tasks_count = len(self.tasks) - len(new_tasks_list)
        self.tasks = new_tasks_list
        return f'Cleared {removed_tasks_count} tasks.'

    def view_section(self):
        tasks_details = "\n".join([x.details() for x in self.tasks])
        return f'Section {self.name}:\n{tasks_details}'


# task = Task("Make bed", "27/05/2020")
#
# print(task.change_name("Go to University"))
#
# print(task.change_due_date("28.05.2020"))
#
# task.add_comment("Don't forget laptop")
#
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
#
# print(task.details())
#
# section = Section("Daily tasks")
#
# print(section.add_task(task))
#
# second_task = Task("Make bed", "27/05/2020")
#
# section.add_task(second_task)
#
# print(section.clean_section())
#
# print(section.view_section())
