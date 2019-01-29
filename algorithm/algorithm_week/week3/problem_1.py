import sys
sys.stdin = open("problem_1.txt", "r")
T = int(input())
for tc in range(1, T+1):
    check_word = input()
    sentence = input()
    len_check = len(check_word)
    len_sentence = len(sentence)
    cnt_check, cnt_sentence = 0, 0
    result = 0
    # print(check_word, sentence)
    for i in range(len_sentence):
        if sentence[cnt_sentence] != check_word[cnt_check]:
            cnt_sentence += 1
        else:
            cnt_sentence += 1
            cnt_check += 1
            if cnt_check == len_check:
                result = 1
                break               # 이거 안쓰고 range 조정해서 풀어볼것. !
    print(f'#{tc} {result}')


