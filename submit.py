import requests

# CHANGE THE FOLLOWING LINE TO YOUR URL
url = "https://Conditional-grading-server.iswassi.repl.co/loops_1"

def submit():
	with open("main.py", "rb") as f:
		files = {'codefile': f}
		r = requests.post(url, files=files)
		if r.ok:
			print("Your code has been submitted")
		else:
			print("Sorry, something went wrong")

