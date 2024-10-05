def qtdA(s: str):
    amin = 0
    amai = 0
    for i in s:
        if i == "a":
            amin = amin + 1
        elif i == "A":
            amai = amai + 1
    return f'A quantidade de letras "A" maiúscula é {amai}, e a quantidade de letras "a" Minúsculas é {amin}'

print(qtdA(input("Digite a palavra desejada: ")))