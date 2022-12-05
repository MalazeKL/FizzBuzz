hai_so = input("Nhập 2 số (cách nhau bằng dấu cách): ")
start = int(hai_so.split()[0])
end = int(hai_so.split()[1])
while start > end:
    print("số bắt đầu cần nhỏ hơn số kết thúc")
    hai_so = input("Nhập 2 số (cách nhau bằng dấu cách): ")
    start = int(hai_so.split()[0])
    end = int(hai_so.split()[1])
for num in range(start, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end = " " )
    elif num % 5 == 0:
        print("Buzz", end = " " )
    elif num % 3 == 0:
        print("Fizz", end = " " )
    else:
        print(num, end = " " )
