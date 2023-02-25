class Smartphone:
    def __init__(self, memory) -> None:
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on == False:
            self.is_on = True
        else:
            self.is_on = False
    
    def install(self, app, app_memory):
        
        if self.is_on == True:
            if self.memory - app_memory >= 0:
                self.memory -= app_memory
                self.apps.append(app)
                return f"Installing {app}"
            else:
                return f"Not enough memory to install {app}"


        else:
            if self.memory - app_memory >= 0:
                return f"Turn on your phone to install {app}"
    
    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.memory
        return f"Total apps: {total_apps_count}. Memory left: {memory_left}"
        

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
