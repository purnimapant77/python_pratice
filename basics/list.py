tasks = ["data_cleanup", "user_auth", "image_processing"]

tasks.append("generate_report")
tasks.insert(0,"security_audit")
tasks.pop(2)
tasks.reverse()
print(tasks)

for iteam in tasks[::-1]:
    print(iteam)
