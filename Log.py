from abc import abstractmethod


class Log:
    @abstractmethod
    def Debug(self):
        pass

    @abstractmethod
    def Info(self):
        pass

    @abstractmethod
    def Warn(self):
        pass

    @abstractmethod
    def Error(self):
        pass

    @abstractmethod
    def Crit(self):
        pass

class ConsoleLog(Log):
    def Debug(self):
        print("\033[32m {}" .format("Debug"))

    def Info(self):
        print("\033[34m {}".format("Info"))

    def Warn(self):
        print("\033[35m {}".format("Warn"))

    def Error(self):
        print("\033[31m {}".format("Error"))

    def Crit(self):
        print("\033[33m {}".format("Crit"))

test = ConsoleLog()
test.Debug()
test.Info()
test.Warn()
test.Error()
test.Crit()

