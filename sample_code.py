from djitellopy import Tello
from apscheduler.schedulers.background import BackgroundScheduler
import time

print("Create Tello object")
tello = Tello()

print("Connect to Tello Drone")
tello.connect()


def my_function():
	print("Function executed at", time.strftime("%Y-%m-%d %H:%M:%S"))
	print("Takeoff!")
	tello.takeoff()

	print("Move Up")
	tello.move_up(40)

	print("Move Down")
	tello.move_down(40)

	print("landing")
	tello.land()
	print("touchdown.... goodbye")

# Set the desired execution time (e.g., 14:45)
desired_time = "11:30"

# Create a scheduler
scheduler = BackgroundScheduler()

# Schedule the function to run once at the desired time
scheduler.add_job(my_function, 'cron', hour=int(desired_time.split(':')[0]), minute=int(desired_time.split(':')[1]))

# Start the scheduler in the background
scheduler.start()


# You can do other tasks here while the scheduler is running in the background

#OTHER TASKS
battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")


try:
    # Keep the main thread alive
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    # Shut down the scheduler gracefully on keyboard interrupt
    scheduler.shutdown()







