class Jornalistas:

    def __init__(self, id, nome, imagem, biografia):
        self.id = id
        self.nome = nome
        self.imagem = imagem
        self.biografia = biografia
       
    
    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_imagem(self):
        return self.imagem
    def get_biografia(self):
        return self.biografia
    


class Noticias:
    def __init__(self, id, titulo, resumo, data, descricao, categoria, jornalista, conteudo, imagem, idJornalista):
        self.id = id
        self.titulo = titulo
        self.resumo = resumo
        self.data = data
        self.descricao = descricao
        self.categoria = categoria
        self.jornalista = jornalista
        self.conteudo = conteudo
        self.imagem = imagem
        self.idJornalista = idJornalista
    

    def get_id(self):
        return self.id
    def get_titulo(self):
        return self.titulo
    def get_resumo(self):
        return self.resumo
    def get_data(self):
        return self.data
    def get_descricao(self):
        return self.descricao
    def get_categoria(self):
        return self.categoria
    def get_jornalista(self):
        return self.jornalista
    def get_conteudo(self):
        return self.conteudo
    def get_imagem(self):
        return self.imagem
    def get_idJornalista(self):
        return self.idJornalista



