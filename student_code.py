import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """

        # if factq(fact):
        #     for f in self.facts:
        #         if f == fact:
        #             break
        #     self.facts.append(fact)
        if isinstance(fact,Fact):
            self.facts.append(fact)
        # print("Asserting {!r}".format(fact))
        # print(self.facts[0])

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        # print("Asking {!r}".format(fact))
        # print("")

        # if isinstance(fact,Fact):
        #     for f in self.facts:
        #         bindings.extend(fact,f)

        bindings = []

        for f in self.facts:
            if f.__eq__(fact):
                # print("they are equal!")
                bindings.append(Bindings())
                continue
            # print(f.statement.terms)
            if match(fact.statement,f.statement):
                bindings.append(match(fact.statement,f.statement))


        # print("bindings is {!r}".format(bindings))

        if len(bindings) == 0:
            return False
        else:
            return bindings
