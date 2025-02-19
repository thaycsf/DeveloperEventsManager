class MinhaClasse:
  def __enter__(self):
    print("Entrou!")
    
  def __exit__(self, exc_type, exc_val, exc_tb):
    print("Saiu!")
      
with MinhaClasse() as mc:
  print("Dentro do bloco with")