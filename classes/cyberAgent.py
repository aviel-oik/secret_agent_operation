import agent

class CyberAgent(agent.Agent):
    def __init__(self, code_name, clearance_level, specialty):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self.__clearance_level}, specialty : {self.specialty}")
