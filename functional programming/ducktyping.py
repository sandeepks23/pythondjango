class Pycharm:
    def open(self):
        print("Open Pycharm")
    def run(self):
        print("Run in Pycharm")
    def debug(self):
        print("debug in pycharm")

class Vscode:
    def open(self):
        print("Open Vscode")
    def run(self):
        print("Run in Vscode")
    def debug(self):
        print("debug in Vscode")


class Programmer:
    def coding(self,ide):
        ide.open()
        ide.run()
        ide.debug()
vsc=Vscode()
pr=Programmer()
pr.coding(vsc)