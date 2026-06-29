class Symbol:

    def __init__(self, name):
        self.name = name

    def evaluate(self, facts):
        return self.name in facts



class And:

    def __init__(self, *args):
        self.args = args


    def evaluate(self, facts):

        for item in self.args:
            if not item.evaluate(facts):
                return False

        return True



class Or:

    def __init__(self, *args):
        self.args = args


    def evaluate(self, facts):

        for item in self.args:

            if item.evaluate(facts):
                return True

        return False



class Rule:


    def __init__(self, condition, result):

        self.condition = condition
        self.result = result



    def check(self, facts):

        if self.condition.evaluate(facts):

            return self.result

        return None
