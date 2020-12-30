import random
import datetime
import time

severity_random = ["INFO", "WARN", "ERROR"]
http_status_random = {0: ["200", "201", "202", "203"], 1: ["400", "404", "409"], 2: ["505", "504", "508"]}
resource_path_random = ["/api/users/", "/api/books/", "/api/films/", "/api/videos/", "/api/pictures/", "/api2/users/",
                        "/api2/books/", "/api2/films/", "/api2/videos/", "/api2/pictures/", "/api2/messages/",
                        "/api2/favourites/", "/api2/likes/", "/api2/drugs_shop/"]
user_randoms = ["timpo", "weslyG", "imosk72", "ViV_99", "Lycoris_nya", "goge_lozh", "asdminerpro", "Oleninochka",
                "KawaiiAxonny", "pupupug", "artamaney", "Cardstell", "uralgoods"]

while True:
    file = open("log3", "a")
    now = datetime.datetime.now()

    log_string = now.strftime("%Y.%m.%d-%H:%m:%S")

    randomed = random.randrange(0, 3, 1)

    log_string += " " + severity_random[randomed]
    randomed_inner = random.randrange(0, len(http_status_random.get(randomed)), 1)
    log_string += " " + http_status_random.get(randomed)[randomed_inner]

    randomed_user = random.randrange(0, len(user_randoms), 1)

    log_string += " " + user_randoms[randomed_user]

    log_string += " " + str(random.randrange(1, 101, 1))

    log_string += " " + resource_path_random[random.randrange(0, len(resource_path_random))]
    file.write(log_string + "\n")
    #print(log_string)
    file.close()
    time.sleep(1)

