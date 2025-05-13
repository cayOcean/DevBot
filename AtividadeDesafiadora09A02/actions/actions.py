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

        if not titulo:
            dispatcher.utter_message(text="Você pode me dizer o título do livro?")
            return []

        try:
            url = f"https://openlibrary.org/search.json?title={titulo}"
            response = requests.get(url).json()

            if response.get('docs'):
                livro = response['docs'][0]
                nome = livro.get('title', 'Título desconhecido')
                autores = ', '.join(livro.get('author_name', ['Autor desconhecido']))
                dispatcher.utter_message(text=f"Encontrei: *{nome}* de {autores}.")
            else:
                dispatcher.utter_message(text="Desculpe, não encontrei esse livro.")
        except Exception as e:
            dispatcher.utter_message(text="Ocorreu um erro ao buscar o livro. Tente novamente mais tarde.")
            print(f"Erro ao buscar livro por título: {e}")

        return []


class ActionBuscarLivroAutor(Action):
    def name(self) -> Text:
        return "action_buscar_livro_autor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        autor = tracker.get_slot("nome_autor")

        if not autor:
            dispatcher.utter_message(text="Qual o nome do autor?")
            return []

        try:
            url = f"https://openlibrary.org/search.json?author={autor}"
            response = requests.get(url).json()

            if response.get('docs'):
                titulos = [livro.get('title', 'Sem título') for livro in response['docs'][:3]]
                dispatcher.utter_message(text=f"Alguns livros de *{autor}*: {', '.join(titulos)}.")
            else:
                dispatcher.utter_message(text="Não encontrei livros desse autor.")
        except Exception as e:
            dispatcher.utter_message(text="Houve um problema ao buscar os livros do autor.")
            print(f"Erro ao buscar livro por autor: {e}")

        return []


class ActionBuscarLivroAssunto(Action):
    def name(self) -> Text:
        return "action_buscar_livro_assunto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        assunto = tracker.get_slot("assunto_livro")

        if not assunto:
            dispatcher.utter_message(text="Sobre qual assunto você gostaria de ver livros?")
            return []

        try:
            url = f"https://openlibrary.org/search.json?subject={assunto}"
            response = requests.get(url).json()

            if response.get('docs'):
                livros = [livro.get('title', 'Sem título') for livro in response['docs'][:3]]
                dispatcher.utter_message(text=f"Livros sobre *{assunto}*: {', '.join(livros)}.")
            else:
                dispatcher.utter_message(text="Nenhum livro encontrado com esse assunto.")
        except Exception as e:
            dispatcher.utter_message(text="Erro ao buscar livros por assunto.")
            print(f"Erro ao buscar livro por assunto: {e}")

        return []
