print ("Bem vindo ao assistente inteligente python! Aqui respondemos suas duvidas de programação")
print()

PERGUNTA = input("digite uma pergunta: (O que é Variável)/(O que é IA Generativa)/(O que é IA): ").lower().strip()

match PERGUNTA:
    case "o que é variável" | "o que é variavel" | "o que é variavel?" | "o que é variável?":
        print ("Variáveis são uma caixa vazia, elas armazenam informações definidas, que podem variar ao decorrer do código.")
    case "o que é ia generativa" | "o que é ia generativa?":
        print ("Ia generativa é um algoritmo que imita a inteligência humana através de dados, e pode criar (generar) novas informações a partir dos mesmos.")
    case "o que é ia" | "o que é ia?":
        print("IA é um algoritmo que imita a inteligencia humana a partir de dados, e serve para tomar decisões, resolver problemas, analisar possibilidades, através das estatisticas.")