class AgencyDirector:
    single = None

    def __init__(self):
        print("one more")

    @classmethod
    def init_one_time(cls):
        if cls.single is None:
            AgencyDirector.single = cls()
        return AgencyDirector.single

a = AgencyDirector.init_one_time()
b = AgencyDirector.init_one_time()


print(a is b)


