from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionBuscarLivroTitulo(Action):
    def name(self) -> Text:
        return "action_buscar_livro_titulo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        titulo = tracker.get_slot("titulo_livro")
        url = f"https://openlibrary.org/search.json?title={titulo}"
        response = requests.get(url).json()
        
        if response['docs']:
            livro = response['docs'][0]
            dispatcher.utter_message(text=f"Encontrei: {livro.get('title')} de {', '.join(livro.get('author_name', []))}")
        else:
            dispatcher.utter_message(text="Desculpe, não encontrei esse livro.")
        
        return []

class ActionBuscarLivroAutor(Action):
    def name(self) -> Text:
        return "action_buscar_livro_autor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        autor = tracker.get_slot("nome_autor")
        url = f"https://openlibrary.org/search.json?author={autor}"
        response = requests.get(url).json()
        
        if response['docs']:
            titulos = [livro.get('title') for livro in response['docs'][:3]]
            dispatcher.utter_message(text=f"Alguns livros de {autor}: {', '.join(titulos)}")
        else:
            dispatcher.utter_message(text="Não encontrei livros desse autor.")
        
        return []

class ActionBuscarLivroAssunto(Action):
    def name(self) -> Text:
        return "action_buscar_livro_assunto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        assunto = tracker.get_slot("assunto_livro")
        url = f"https://openlibrary.org/search.json?subject={assunto}"
        response = requests.get(url).json()
        
        if response['docs']:
            livros = [livro.get('title') for livro in response['docs'][:3]]
            dispatcher.utter_message(text=f"Livros sobre {assunto}: {', '.join(livros)}")
        else:
            dispatcher.utter_message(text="Não encontrei livros sobre esse assunto.")
        
        return []
