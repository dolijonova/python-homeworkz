txt=input()

vowels="aeuioAUEIO"

counter=0

ans=""

for i in range(len(txt)):
    counter+=1
    ans+=txt[i]
    if i!=len(txt)-1 and counter>=3 and txt[i] not in vowels:
        vowels+=txt[i]
        ans+="_"
        counter=0

print(ans)