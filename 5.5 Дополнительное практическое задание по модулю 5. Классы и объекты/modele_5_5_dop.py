from multiprocessing.dummy import current_process
from time import sleep

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __str__(self, nickname):
        return f'{self.nickname}'

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    # def __str__(self):
    #     return f'{"self.title"}'
    def __repr__(self):
        return f'{self.title}'

class UrTube:

    def __init__(self):
        self.age = []
        self.nickname = []
        self.password = []
        #self.users = User.users
        #self.videos = Video.videos
        self.current_user = None
        self.users = []
        self.videos =[]


    def log_in (self, nickname, password):
        for user in self.users:
            if user["nickname"] == nickname and user ["password"] == hash(password):
                self.current_user = user["nickname"]
                self.age = user["age"]
                #print(f'вошел{self.current_user}')

    def register (self, nickname, password, age):
        for user in self.users:
            if user["nickname"] == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.users.append({"nickname": nickname, "password": hash(password), "age": age})
        UrTube.log_in(self, nickname, password)
        #print(self.users)

    def log_out (self):
        self.current_user = None

    def add (self,*video):
        for v in video:
            if v not in self.videos:
                self.videos.append(v)

    def get_videos (self, text):
        all_videos = []
        text_l = text.lower()
        for t in self.videos:
            if text_l in t.title.lower():
                all_videos.append(t)
        return all_videos

    def watch_video (self, name):

        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        if int(self.age) < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for n in self.videos:
            if n.title == name:
                for number in range(n.time_now,n.duration):
                    sleep(1)
                    print(number+1, end=' ', flush=True)
                print("Конец видео")
                n.time_now = 0
                return

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
