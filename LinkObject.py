from dataclasses import dataclass

@dataclass
class LinkObject():
    title: str
    link: str
    time: str

    def __str__(self):
        return f'{self.time}\n{self.title}\n{self.link}'
