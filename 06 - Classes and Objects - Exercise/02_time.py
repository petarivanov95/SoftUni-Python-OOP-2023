class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59
    
    def __init__(self,hours: int,minutes: int,seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def set_time(self, new_hours: int, new_minutes: int, new_seconds: int):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        hh = str(self.hours).zfill(2)
        mm = str(self.minutes).zfill(2)
        ss = str(self.seconds).zfill(2)
        return f"{hh}:{mm}:{ss}"
    
    def next_second(self):
        if self.seconds == Time.max_seconds:
            self.seconds = 0
            if self.minutes == Time.max_minutes:
                self.minutes = 0
                if self.hours == Time.max_hours:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1           
        else:
            self.seconds += 1
            
            
        return self.get_time()                        

time = Time(9, 30, 59)
print(time.next_second())