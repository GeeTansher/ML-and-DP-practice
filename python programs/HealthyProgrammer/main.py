import time
from pygame import mixer
from datetime import datetime
from datetime import date

def music(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input("Enter to stop reminder:")
        if a == stopper:
            mixer.music.stop()
            break

def log(message):
    with open("Logs.txt","a") as f:
        f.write(f"{message} {datetime.now()} \n")


if __name__ == '__main__':
    # start = int(input("Enter the starting hour time of office in 24h format:"))
    # end = int(input("Enter the ending hour time of office in 24h format:"))
    # if end is 0:
    #     end=24
    init_water_time = time.time()
    init_eyes_time = time.time()
    init_exercise_time = time.time()
    total_time = time.time()
    wateramounthr = (((8/ 3.5)/1000) * 200)    #(((end - start)/3.5)/1000)*200
    watersecs = wateramounthr*360
    eyessecs = 30*60    # in every 30 min
    exercisesecs = 45 * 60  # in every 45 min
    watersecs=10
    eyessecs = 20
    exercisesecs = 30
    print("Time Started. Hope you will follow !!!")
    with open("Logs.txt", "a") as f:
        f.write(f"\n{date.today()} logs:\n")
    while (time.time()-total_time <= (8*60*60)):
        if time.time()-init_water_time > watersecs:
            print("It's time to drink water. Enter 'drank' after drinking water.")
            music('water.mp3','drank')
            log("Drank water at ")
            init_water_time = time.time()
        if time.time()-init_eyes_time > eyessecs:
            print("It's time to do some eyes exercise. Enter 'done' after doing exercise.")
            music('eye.mp3','done')
            log("Done eye exercise at ")
            init_eyes_time = time.time()
        if time.time()-init_exercise_time > exercisesecs:
            print("It's time to do some physical exercise. Enter 'done' after doing exercise.")
            music('physical.mp3','done')
            log("Done physical exercise at ")
            init_exercise_time = time.time()
