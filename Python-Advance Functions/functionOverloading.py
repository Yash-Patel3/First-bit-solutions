def calculate_sum(*numbers):
        total = 0
        for num in numbers:
            total += num
        print(f"Sum: {total}")

calculate_sum(1, 2)
calculate_sum(1, 2, 3, 4)