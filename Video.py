class Video:

    def __init__(self,title,tags,description,duration):
        self.title = title
        self.tags = tags
        self.description = description
        self.duration = duration
    
    def __str__(self):
        return f"Title: {self.title}, Tags: {self.tags[:]} \nDescription: {self.description} \nDuration: {self.duration}\n\n"