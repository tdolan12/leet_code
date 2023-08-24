class RecentCounter:

    def __init__(self):
        self.ping_list = []
        
        

    def ping(self, t):
        self.ping_list.append(t)
        lower_bound = t - 3000
        ping_count = int()
        for ping in self.ping_list:
            if ping >= lower_bound:
                ping_count += 1
        return [ping_count]
                
        