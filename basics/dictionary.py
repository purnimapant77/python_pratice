config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

config["port"]=9000
config["version"]="1.0.0"

timeout_setting=config.get("timeout",30)

for key,values in config.items():
    print(f" Key:{key} , value:{values} \n")
    