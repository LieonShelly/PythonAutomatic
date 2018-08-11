from git import Repo
import os
import datetime, time
import pathlib

repo_path = "/Users/lieon/Desktop/CompanyProjects/NBCartoon"
user_name = "lieoncx"
log_file_path = "/Users/lieon/Desktop/log.md"

def is_same_day(t1, t2):
    t1_str = time.strftime('%Y-%m-%d', time.localtime(t1))
    t2_str = time.strftime('%Y-%m-%d', time.localtime(t2))
    return t1_str == t2_str

def get_today_log():
    repo = Repo(repo_path)
    today = datetime.date.today()
    today_timestamp = time.mktime(today.timetuple())
    log_list = list(repo.head.log())
    today_logs = list(filter(lambda log: is_same_day(float(log.time[0]), 1533902582) , log_list))
    my_logs = list(filter(lambda log: str(log.actor) == user_name, today_logs))
    messages = list(map(lambda log: log.message, my_logs))
    messge_list = []
    for index in range(len(messages)):
        msg = messages[index]
        index_str = str('%d. ' % (index + 1))
        modiy_mesage = msg.replace('commit:', index_str)
        messge_list.append(modiy_mesage)
    return messge_list

def write_log_to_file(path, logs):
    log_file = open(path, 'w')
    if(len(logs) > 0):
        for log in logs:
             log_file.write(log)
             log_file.write('\n')
        log_file.close()
   
def open_file(path):
    os.system('open %s' % (log_file_path))

if __name__ == '__main__':
    logs = get_today_log()
    if(len(logs) > 0):
        write_log_to_file(log_file_path, logs)
        open_file(log_file_path)
