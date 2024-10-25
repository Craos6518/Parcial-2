# Función que dibuja el estado actual del ahorcado
def mostrar_ahorcado(intentos): # Recibe el número de intentos restantes
    etapas = [
        # Etapa 0
        """ 
           +---+
           |   |
           |    
           |    
           |    
           |    
        =========
        """,# Etapa 1
        """
           +---+
           |   |
           |   O 
           |    
           |    
           |    
        =========
        """,# Etapa 2
        """
           +---+
           |   |
           |   O 
           |   | 
           |    
           |    
        =========
        """, # Etapa 3
        """
           +---+
           |   |
           |   O 
           |  /| 
           |    
           |    
        =========
        """, # Etapa 4
        """
           +---+
           |   |
           |   O 
           |  /|\ 
           |    
           |    
        =========
        """, # Etapa 5
        """
           +---+
           |   |
           |   O 
           |  /|\ 
           |  /  
           |    
        =========
        """,# Etapa 6
        """
           +---+
           |   |
           |   O 
           |  /|\ 
           |  / \  
           |    
        =========
        """# 6 intentos
    ]
    print(etapas[intentos])# Mostrar etapa correspondiente