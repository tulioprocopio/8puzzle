from agentes.abstrato import AgenteAbstrato
class AgentePrepostoESHumano(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        aux = ''
        elems_dipostos = percepcao_mundo.disposicao_elementos
        #guia_indices = '0 1 2'+'\n'+'\n'        
        #print(guia_indices)        
        i=0
        #print(elems_dipostos)
        #print('tamanho '+str(len(elems_dipostos)-1))
        for i in range(len(elems_dipostos)):
            aux = aux+' '+str(elems_dipostos[i])
            if ((i == 2) or (i == 5) or (i == (len(elems_dipostos)-1))):
                
                print(aux+'\n')
                aux = ''
                #print('\n')
            
            
        
    
    def escolherProximaAcao(self):
        from acoes import AcaoJogador
        i, j = (int(s) for s in input("Proxima troca (i,j)? ").split(',', 2))
        return AcaoJogador.permutar(i, j)