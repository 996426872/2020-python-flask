def log(func):
    def wrapper(*args, **kwargs):
        print("{} be called".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


@log
def now():
    print("2020-11-16")


f = now
print(now.__name__)
print(f.__name__)
now()
# now() log(now)

