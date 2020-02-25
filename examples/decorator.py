def deco(func: callable):
    print(f"start {deco.__name__} call")

    def inner_deco(callable_obj, *args, **kwargs):
        print(f"start {inner_deco.__name__} call")
        ret = func(callable_obj, *args, **kwargs)
        return ret

    print(f"end {deco.__name__} call")
    return inner_deco


print("start define add")


@deco
def add(x: int, y: int):
    return x + y


print(add(3, 5))
print(add.__name__)
