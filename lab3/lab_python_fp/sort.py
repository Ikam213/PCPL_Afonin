data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == "__main__":
    result = []
    temp = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if (abs(data[i]) > abs(data[j])):
                temp = data[j]
                data[j] = data[i]
                data[i] = temp
    result = data.copy()          
    print(result)

    result_with_lambda = sorted(data, key = lambda x: abs(x), reverse = True)
    print(result_with_lambda)