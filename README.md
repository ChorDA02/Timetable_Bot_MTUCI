# Timetable Bot MTUCI
VK Timetable Python Bot
# Requirements
- Python3
- vk_api
- PyMySQL
# How to launch
Insert your VK Group Token into bot.py

Create MySQL DB and import bot.sql

Insert your MySQL DB login details into mysql_connect.py

Upload bot.py, mysql_connect.py, checkbot, startbot on your server

Make CronTab tasks:
```bash
*/1 * * * * *path*/checkbot
0 * * * * *path*/startbot
```
Invite your group into conference

Insert your timetable into the database
# Presentation
![1](https://user-images.githubusercontent.com/79046421/177777011-48ee67ba-7dfc-45c8-9615-9135c192df20.png)
# License
GNU GPL v3
