from PIL import Image


def main():
	default_ration = 1366//768
	new_ratio = (1920//1080)//default_ration
	img = Image.open("./4.png")
	size = img.size
	new_size = new_ratio*size
	
if __name__ == "__main__":
	main()
