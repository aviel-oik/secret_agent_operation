from classes import agent
from classes import fieldAgent
from classes import cyberAgent


def show_report(lst):
    for agent in lst:
        agent.report()

a = agent.Agent("moi", 1)
b = fieldAgent.FieldAgent("toi", 2, "jerusalem")
c = cyberAgent.CyberAgent("lui", 3,"developer")

lst_agent = [a, b, c]

show_report(lst_agent)