import redis

redis_db = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)

capitals = {}
capitals["Bahamas"] = "Nassau"
capitals["Croatia"] = "Zagreb"
print(capitals.get("Croatia"))

capitals.update(dict(Lebanon="Beirut", Norway="Oslo", France="Paris"))

print([capitals.get(k) for k in ["Lebanon", "Norway", "Bahamas"]])

print("Norway" in capitals)

data = {
    "realpython": {
        "url": "https://realpython.com/",
        "github": "realpython",
        "fullname": "Real Python",
    }
}

print(data)

