class Task:
    def __init__(self, name: str, due_date: str) -> None:
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str) -> None:
        if self.name == new_name:
            return "Name cannot be the same."
        else:
            self.name = new_name
            return self.name

    def change_due_date(self, new_date: str) -> None:
        if self.due_date == new_date:
            return "Date cannot be the same."
        else:
            self.due_date = new_date
            return self.due_date

    def add_comment(self, new_comment: str) -> None:
        self.comments.append(new_comment)

    def edit_comment(self, index: int, new_comment: str) -> None:
        if index < 0 or index >= len(self.comments):
            return "Cannot find comment."
        else:
            self.comments[index] = new_comment

        return ", ".join(self.comments)

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"