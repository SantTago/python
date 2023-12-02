"""
Esta é uma implementação Python do Markdown 
de John Gruber. É quase totalmente compatível 
com a implementação de referência, embora existam 
alguns problemas conhecidos. Consulte Recursos 
para obter informações sobre o que exatamente é 
suportado e o que não é. Recursos adicionais são 
suportados pelas extensões disponíveis.

"""
# pip install markdown

import markdown
html = markdown.markdown(your_text_string)

# Markdown (3.0.0+) - Suporte Markdown para a API navegável.