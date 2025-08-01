class Agronomia:

    def __init__(self, fruta, preco_kg, kg_hec, hectares):

        self.fruta = fruta
        self.preco_kg = preco_kg
        self.kg_hec = kg_hec 
        self.hectares = hectares


        self.arrendamento = 550
        self.mudas = 200
        self.insumo = 600
        self.mao_de_obra = 400
        self.energia = 145

    def valorGasto(self):
        GastoTotal = (self.arrendamento +
         self.mudas +
         self.mudas +
         self.insumo +
         self.mao_de_obra +
         self.energia
         )
        return GastoTotal * self.hectares
    
    def valorBruto(self):
        valorBruto = self.kg_hec * self.hectares
        return valorBruto * self.preco_kg
    
    def lucroTotal(self):
        return self.valorBruto() - self.valorGasto()
         
    
    def mostrar_produtividade(self, fruta):
        gasto = self.valorGasto()
        bruto = self.valorBruto()
        lucro = self.lucroTotal()
        print("\n RESULTADO DA PRODUÇÃO ")
        print(f"Fruta escolhida: {fruta}")
        print(f"O gasto total foi: R${gasto}")
        print(f"O valor bruto é: R${bruto}")
        print(f"O líquido obtido foi: R$ {lucro}") 
