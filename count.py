import datetime
import os

def change_day(): 
  return datetime.timedelta(days=1) 

def change_time(): 
  return datetime.timedelta(minutes=1) 

now = datetime.datetime.now() 
commit_date = now - datetime.timedelta(days=15) 

while commit_date < now: 
  commit_date = commit_date + change_day() 
  for i in range(5): 
    f = open('data.txt', 'a+') 
    commit_date = commit_date + change_time() 
    f.writelines(commit_date.isoformat() + '\n') 
    f.close()
    os.system('git add .') 
    os.system('git commit --date={time} -m "Update {time}"'.format(time=commit_date.isoformat()))
os.system('git pull')
os.system('git push')
