def func():
    print("function a.py")
# print(f'a의 __name__은 {__name__}.')
print('top-level a.py')

if __name__ == "__main__":
    print('a.py가 직접 실행')
else:
    print('a.py가 import되어 사용됨')
