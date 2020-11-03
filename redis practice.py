import redis

redis_host = "127.0.0.1"
redis_port = 6379
redis_password = "XwcNom3478"


def hello_redis():
    """Example Hellow Redis Program"""
    try:
        r = redis.StriictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        r.set("msg:hello", "Hello Redis!!!")
        msg = r.get("msg:hello")
        print(msg)
    except Exception as e:
        print(e)
