class Song:
    
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = set()
        
    def how_many(self, listeners):
        count_new = 0
        for element in listeners:
            if element.lower() not in self.listeners:
                self.listeners.add(element.lower())
                count_new += 1
        return count_new
