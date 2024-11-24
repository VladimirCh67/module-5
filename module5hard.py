import time


class User:
    def __init__(self, nicname, password, age):
        self.nicname = nicname
        self.password = password
        self.age = age

        #print(self.nicname)


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

        print((self.title, self.duration))




class UrTube:

    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user


    def login(self, nicname, password, reg):
        self.nicname = nicname
        self.password = password
        self.reg = reg
        x = bool(len(self.users))
        if x:
            for i in range(len(self.users)):
                if self.nicname == self.users[i][0]:
                    if hash(self.password) == hash(self.users[i][1]):
                        self.current_user = self.nicname
                        print(f"Пользователь {self.users[i][0]} найден.")
                        print("Удачный вход")
                        x = True
                        break
                    else:
                        self.current_user = None
                        print(f"Пользователь {self.users[i][0]} найден, но пароль не тот")
                        x = False
                else:
                    self.current_user = None
                    x = False
        else:
            self.current_user = None
                    
        return self.current_user

    def register(self, nicname, password, age):
        self.nicname = nicname
        self.password = password
        self.age = age
        if not self.login(nicname, password, True):

            self.users.append([self.nicname, self.password, self.age])
            self.current_user = self.nicname

    def log_in(self, nicname, password):
        self.nicname = nicname
        self.password = password

        self.login(nicname, password, False)

    def log_out(self):
        self.current_user = None


    def add(self,*args):
        x = bool(len(args))
        y = bool(len(self.videos))
        z = True
        if x:
            for i in range(len(args)):
                if y:
                    for j in range(len(self.videos)):
                        #print(self.videos[j].title)
                        if args[i].title == self.videos[j].title:
                            print(f"Видео {args[i].title} уже существует")
                            z = False
                            break
                    if z:
                        self.videos.append(args[i])
                else:
                    self.videos.append(args[i])

        if bool(len(self.videos)):
            print("Список видео:")
            for j in range(len(self.videos)):
                print(self.videos[j].title)
            print()


    def get_videos(self, title):
        self.title = title

        self.fvideos = []

        for i in range(len(self.videos)):
            if self.title.lower() in  self.videos[i].title.lower():
               self.fvideos.append(self.videos[i].title)

        return self.fvideos


    def watch_video(self, title):
        self.title = title

        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for i in range(len(self.videos)):
                if self.title.lower() ==  self.videos[i].title.lower():
                    if self.videos[i].adult_mode:
                        for j in range(len(self.users)):
                            if self.current_user.lower() == self.users[j][0].lower() and self.users[j][2] < 18:
                                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                                break

                    print("Начало просмотра видео ", self.title, "для ", self.current_user)
                    for y in range(10):
                        time.sleep(1)
                        print(y+1)
                    print("Конец видео")
                    break





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования', 150)
us_1 = User("Denis", 'D1234567s',23)

# Добавление видео
ur.add(v1, v2)
ur.add(v3, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

