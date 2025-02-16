# device_bridge
flask sample project

<br>
Microservice Project Architect: 
<br>
run :
<br>
python project_architect.py
<br>
<br>
<br>

![device_bridge_0](https://github.com/user-attachments/assets/6c04ed31-320a-4dfc-89f3-23c9f1c60601)

<br>
add a project with CURL
<br>
curl -X POST http://localhost:5000/projects \
-H "Content-Type: application/json" \
-d '{"title": "Sample project", "description": "desctiption for project.", "user_id": 1}'
<br>
delete a project
<br>
curl -X DELETE http://localhost:5000/projects/1

<br>
----

sudo docker run -it -p 5000:5000 sdevbridge /bin/bash

<br>
----------

sudo docker build -t sdbidge .

<br>
------
<br>

sudo docker system prune

<br>

sudo docker system prune -a --volumes

<br>

sudo docker image prune -a

<br>

sudo docker builder prune

<br>

sudo docker builder prune --all

<br>

sudo docker container prune

<br>

sudo docker volume prune