class Input:
    def html_teg(self) -> str:
        pass


class CheckBox:
    def html_teg(self) -> str:
        pass


class Button:
    def html_teg(self) -> str:
        pass


class WinInput(Input):
    def html_teg(self) -> str:
        return "<wininput/>"


class WinCheckBox:
    def html_teg(self) -> str:
        return "<wincheckbox/>"


class WinButton:
    def html_teg(self) -> str:
        return "<winbutton/>"


class LinInput(Input):
    def html_teg(self) -> str:
        return "<lininput/>"


class LinCheckBox(Input):
    def html_teg(self) -> str:
        return "<lincheckbox/>"


class LinButton(Input):
    def html_teg(self) -> str:
        return "<linbutton/>"


class Factory:
    def create_input(self) -> Input:
        pass

    def create_checkbox(self) -> CheckBox:
        pass

    def create_button(self) -> Button:
        pass


class WinFactory(Factory):
    def create_input(self) -> Input:
        return WinInput()

    def create_checkbox(self) -> CheckBox:
        return CheckBox()

    def create_button(self) -> Button:
        return Button()


class LinFactory(Factory):
    def create_input(self) -> Input:
        return LinInput()

    def create_checkbox(self) -> CheckBox:
        return CheckBox()

    def create_button(self) -> Button:
        return Button()



factory = WinFactory()
print(factory.create_input())
