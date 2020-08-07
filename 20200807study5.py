# 게시판 페이징. 게시물의총건수와 한페이지에 보여줄 게시물수 입력. 총페이지수 출력.

def total_page(m, n):
    if m % n == 0:
        return m // n
    else:
        return (m // n) + 1

print(total_page(15, 10))
print(total_page(30, 10))