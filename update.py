import os

print("Updating repo.")
os.system("git pull")
os.system("git add --all")
os.system("git commit . -m 'Update'")
os.system("git push")
print("Finished.")