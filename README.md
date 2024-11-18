# device_bridge
flask sample project

<br>
Microservice Project Architect: <br>
run :
<br>
python3 project_architect.py
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
curl -X DELETE http://127.0.0.1:5000/projects/1
