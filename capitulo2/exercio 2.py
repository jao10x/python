precoCapaLivro = 24.95
precoCapaLivroDesconto = precoCapaLivro - (precoCapaLivro * 0.40)
custoFretePrimeiroExemplar = precoCapaLivroDesconto + 3.00
custoFreteRestanteExemplares = precoCapaLivroDesconto + 0.75
custoTotalAtacado = custoFretePrimeiroExemplar + (custoFreteRestanteExemplares * 59)

print("O preco total de atacado para 60 exemplares é de: ", custoTotalAtacado)