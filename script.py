'''
    Auto Script to add, commit and push code to GitHub
    Arguments:
    ----------
    commands.txt
'''

import pexpect, os, sys, time, json

# Variables
username = os.environ["username"]
password = os.environ["access_token"]
repo_name = os.environ["repository_name"]
firebase_proj = os.environ["firebase_proj_name"]

print("Pushing code to GitHub repo '"+repo_name+"'...")
# Clone user's repo
pexpect.run(
    "git clone -b add-deployment-github-action https://github.com/"+username+"/"+repo_name+".git",
    cwd="/Educative/")

cmd_dir = "/Educative/" + repo_name + "/"

# Handling .firebaserc
data = {
  "projects": {
    "default": firebase_proj
  }
}
with open(cmd_dir+"services/web/firebase/.firebaserc", "w") as jsonFile:
    json.dump(data, jsonFile, indent=2)

pexpect.run("cp /Educative/cnwa-solution-files/files/services-web-deploy.yml "+cmd_dir+".github/workflows/")
pexpect.run("git add .", cwd=cmd_dir)
pexpect.run("git commit -m 'removed test workflow changes and enabled workflow optimization'", cwd=cmd_dir)
ch = pexpect.spawn('git push', cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(5)
print("Done")
