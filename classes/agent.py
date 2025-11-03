class Agent:
    total_agents = 0

    def __init__(self, code_name, clearance_level):
        self.code_name = code_name
        self.__clearance_level = clearance_level
        Agent.total_agents += 1

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self.__clearance_level}")

    def get(self):
        return self.__clearance_level

    def set(self, clearance_level):
        if 0 < clearance_level < 11:
            self.__clearance_level = clearance_level

    @staticmethod
    def get_total_agents():
        print(f"total_agents : {Agent.total_agents}")

        
