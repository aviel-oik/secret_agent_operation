from classes import agent
from classes import fieldAgent
from classes import cyberAgent
from classes import mission


def show_report(lst):
    for agent in lst:
        agent.report()

