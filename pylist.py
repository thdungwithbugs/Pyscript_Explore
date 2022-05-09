from datetime import datetime as time

class PyItem(PyItemTemplate):
    def on_click(self, evt=None):
        # self.data["deleted"] = !self.data["deleted"]
        self.data["deleted"] = not self.data["deleted"]
        # Gạch bỏ đối tượng có thuộc tính "deleted"
        self.strike(self.data["deleted"])
        # Đồng thời tick/ bỏ tick input tương ứng
        self.select("input").element.checked = self.data["deleted"]

    def render_content(self):
        string = " - ".join([self.data[item] for item in self.labels])
        thoiGian = self.data["time"].strftime("%H:%M - Day %d, %b/%y")
        return string + "<br/>" + f"<small> Tạo lúc : {thoiGian}</small>"

class PyList(PyListTemplate):
    item_class = PyItem

    def add(self, item):
        if isinstance(item, str):
            worktodo, deadline = [str.strip() for str in item.split('-')]

            item = {"worktodo": worktodo, "deadline": deadline, "deleted": False, "time": time.now()}

        super().add(item, labels=['worktodo', "deadline"], state_key="deleted")
