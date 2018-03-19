
def test(x):
    x = x + 5
    print("Inside func:")
    print(x)
    return x


# class mathtest():






if __name__ == "__main__":
    x = 0
    print("Before func:")
    print(str(x))
    y=test(x)
    print("After func:")
    print(str(x))
    print("y:")
    print(str(y))