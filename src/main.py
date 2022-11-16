import pyautogui as pag
import os
from time import sleep

#Felipe Macedo

# The idea behide this script is to supply the action as images, where is only needed of the program
# to find and click the said image
def main():
    # Images directory
	actions_dir = "./buttons"
    # Dictionary associating file names to pyautogui commands
	actions_script = { "3.png" : "pag.scroll(-2)"}
	
    actions = os.listdir(actions_dir)
	actions.sort()

	for action in actions:
			icon_location = pag.locateOnScreen("".join([actions_dir, "/", action]), confidence=0.8)
			pag.click(icon_location)
			sleep(3)
			try:
				eval(actions_script[action])
			except(KeyError) as e:
				pass
			sleep(5)
			

if __name__ == "__main__":
	main()
