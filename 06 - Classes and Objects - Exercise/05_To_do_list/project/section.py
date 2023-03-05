from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task_name):
        if task_name not in self.tasks:
            self.tasks.append(task_name)
            return f"Task {task_name.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        tasks_dictionary = {task.name: task for task in self.tasks}
        if task_name in tasks_dictionary.keys():
            tasks_dictionary[task_name].completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        for task in self.tasks:
            if task.completed == True:
                self.tasks.remove(task)
                counter += 1

        return f"Cleared {counter} tasks."

    def view_section(self):
        all_tasks = '\n'.join([task.details() for task in self.tasks])
        return f"Section {self.name}:\n {all_tasks}"


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
