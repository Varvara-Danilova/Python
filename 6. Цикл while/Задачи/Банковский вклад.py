start_sum = int(input())
percent = int(input())
target_sum = int(input())
mouth_count = 0
while start_sum <= target_sum:
    start_sum += start_sum/100*percent
    mouth_count += 1
    print(mouth_count, '-', start_sum)
print(f'Колличество месяцев: {mouth_count} \nИтоговая сумма: {target_sum}')

