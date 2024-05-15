iters: int = 0


# Сэкономил целую одну итерацию!!!!!
# На самом деле можно распаралелить и будет быстрее - но это можно сделать и по-другому
# А зачем я это написал так и не понял
# Ну я хотел реккурсию
def cool_sum(arr: list):
    global iters

    sum_list = []
    tmp = None
    if len(arr) % 2 == 1:
        tmp = arr.pop(-1)

    for i in range(0, len(arr), 2):
        iters += 1
        sum_list.append((arr[i] + arr[i + 1]))

    if tmp is not None:
        sum_list.append(tmp)

    if len(sum_list) == 1:
        return sum_list[0]
    else:
        return cool_sum(sum_list)


print(cool_sum(list(range(1000))))
print(iters)
