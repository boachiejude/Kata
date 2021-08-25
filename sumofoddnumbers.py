"""
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
"""

def row_sum_odd_numbers(n):
    rows = {}
    
    if n < 50:
        odd_triangle = [i for i in range(0, 12000) if i % 2 == 1]
    elif n < 101:
        odd_triangle = [i for i in range(0, 1699950)]
    elif n > 400 and n < 450:
        odd_triangle = [i for i in range(10 ** 5, 11 * 5)]
    else:
        odd_triangle = [i for i in range(12000, 10 ** 5)]
    for i in range(500):
        rows[i] = odd_triangle[:i]
        
        for j in rows[i]:
            odd_triangle.remove(j)

    return sum(rows[n])



while True:
    print(row_sum_odd_numbers(int(input())))

# August 25th, 2021...postponed till tomorrow
