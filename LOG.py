# Import all modules
import datetime

# Allows you to create multi-colored text in cmd using Colorama.
from colorama import Fore, Back, Style
from colorama import init

# Create LOG Class
class LOG:
	def INFO(message, save_log=True):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(f"{CurrentTime} - INFO: {message}")

		# Save Log
		if save_log == True:
			open("Debug.log", "a", encoding = "utf-8").write(f"{CurrentTime} - INFO: {message}\n")

	def STATUS(message, save_log=True):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(Fore.BLUE + Style.BRIGHT + f"{CurrentTime} - STATUS: {message}")

		# Save Log
		if save_log == True:
			open("Debug.log", "a", encoding = "utf-8").write(f"{CurrentTime} - STATUS: {message}\n")

	def ERROR(message, save_log=True):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(Fore.RED + Style.BRIGHT + f"{CurrentTime} - ERROR: {message}")

		# Save Log
		if save_log == True:
			open("Debug.log", "a", encoding = "utf-8").write(f"{CurrentTime} - ERROR: {message}\n")

	def WARN(message, save_log=True):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(Fore.YELLOW + Style.BRIGHT + f"{CurrentTime} - WARNING: {message}")

		# Save Log
		if save_log == True:
			open("Debug.log", "a", encoding = "utf-8").write(f"{CurrentTime} - WARNING: {message}\n")
