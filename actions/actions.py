from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecomendarFilme(Action):
    def name(self) -> Text:
        return "action_recomendar_filme"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Obtém o gênero do slot
        genero = tracker.get_slot("genero")

        # Chama a função para obter recomendações de filmes
        filmes = self.obter_recomendacoes(genero)

        # Verifica se há filmes para o gênero fornecido
        if filmes:
            # Envia a resposta com as recomendações de filmes
            dispatcher.utter_message(text=f"Para o gênero {genero}, recomendo: {', '.join(filmes)}.")
        else:
            # Envia uma mensagem caso não encontre filmes para o gênero
            dispatcher.utter_message(text=f"Desculpe, não encontrei recomendações para esse gênero.")

        return []

    def obter_recomendacoes(self, genero: Text) -> List[Text]:
        # Lista de filmes por gênero (pode ser expandida)
        filmes_por_genero = {
            "comédia": ["Esqueceram de Mim", "As Branquelas", "Se Beber, Não Case"],
            "ação": ["Mad Max: Estrada da Fúria", "John Wick", "Missão Impossível"],
            "drama": ["Um Sonho de Liberdade", "O Poderoso Chefão", "A Lista de Schindler"],
            "terror": ["IT: A Coisa", "O Exorcista", "Invocação do Mal"],
            "ficção científica": ["Interestelar", "Blade Runner 2049", "A Chegada"],
            "romance": ["Titanic", "Orgulho e Preconceito", "Simplesmente Acontece"],
            "animação": ["Toy Story", "Divertida Mente", "Procurando Nemo"],
            "documentário": ["A 13 Emenda", "Planeta Terra", "Free Solo"],
            "musical": ["La La Land: Cantando Estações", "Os Miseráveis", "Hamilton"],
            "faroeste": ["Era Uma Vez no Oeste", "Os Imperdoáveis", "Bravura Indômita"],
            "suspense": ["Ilha do Medo", "O Silêncio dos Inocentes", "Seven"]
            
        }

        # Retorna a lista de filmes para o gênero fornecido ou uma lista vazia se não houver recomendações
        return filmes_por_genero.get(genero.lower(), [])
