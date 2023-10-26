random_list = [105, 3.1, "hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Data Float
data_float = tuple(filter(lambda x: isinstance(x, float), random_list))

# Data Int
data_int = list(
    map(
        lambda x: {"ratusan": x // 100, "Puluhan": (x % 100) // 10, "satuan": x % 10},
        filter(lambda x: isinstance(x, int), random_list),
    )
)

# Data String
data_string = list(
    map(
        lambda x: str(x).capitalize(), filter(lambda x: isinstance(x, str), random_list)
    )
)

print("Data Float:", data_float)
print("Data Int:")
for item in data_int:
    print(item)
print("Data String:", data_string)