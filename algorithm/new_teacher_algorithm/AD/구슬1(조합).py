def dfs(no,cnt):
    # if cnt==1:
    #     print(cnt, ':', end='  ')
    #     print(*b);return
    if no>=N:
        print(cnt, ':', end='  ')
        print(*b);return

    b[no] = a[no] #담기   앞 no를 cnt로 바꾸면 앞에서부터 차곡차곡 담긴다.
    dfs(no+1,cnt+1)

    b[no]=0 # 담지않기     앞 no를 cnt로 바꾸면 앞에서부터 차곡차곡 담긴다.
    dfs(no+1,cnt)

a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3
cnt = 0
dfs(0,cnt)
# print(cnt)
