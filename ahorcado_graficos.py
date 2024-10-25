# Función que dibuja el estado actual del ahorcado
def mostrar_ahorcado(intentos):
    etapas = [
        """
           +---+
           |   |
           |    
           |    
           |    
           |    
        =========
        """,
        """
           +---+
           |   |
           |   O 
           |    
           |    
           |    
        =========
        """,
        """
           +---+
           |   |
           |   O 
           |   | 
           |    
           |    
        =========
        """, 
        """
           +---+
           |   |
           |   O 
           |  /| 
           |    
           |    
        =========
        """, 
        """
           +---+
           |   |
           |   O 
           |  /|\ 
           |    
           |    
        =========
        """, 
        """
           +---+
           |   |
           |   O 
           |  /|\ 
           |  /  
           |    
        =========
        """,
        """
           +---+
           |   |
           |   O 
           |  /|\ 
           |  / \  
           |    
        =========
        """
    ]
    print(etapas[intentos])