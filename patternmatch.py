def search(input_pattern,input_text):
    M = len(input_pattern)
    N = len(input_text)

    for i in range(N - M + 1):
        for j in range(M):
            if input_text[i+j] != input_pattern[j]:
                break

        if j == M-1:
            print("Pattern found at index "+str(i))


print ("Enter the text: ")
input_text=input()
print("Enter the pattern: ")
input_pattern=input()
search(input_pattern,input_text)


