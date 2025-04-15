from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionFornecerSuporte(Action):

    def name(self) -> Text:
        return "action_fornecer_suporte"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        problema = tracker.get_slot("problema")

        if not problema:
            dispatcher.utter_message(text="Você poderia me dar mais detalhes sobre o problema?")
            return []

        if "acessar" in problema or "login" in problema:
            dispatcher.utter_message(text="Tente redefinir sua senha clicando em 'Esqueci minha senha' na tela de login.")
        elif "mudar meu plano" in problema or "trocar de plano" in problema:
            dispatcher.utter_message(text="Você pode mudar de plano acessando o menu 'Conta > Planos' no aplicativo.")
        elif "aplicativo não funciona" in problema or "app" in problema:
            dispatcher.utter_message(text="Tente reinstalar o aplicativo ou verificar se há atualizações disponíveis.")
            dispatcher.utter_message(text="Se o problema persistir, vou te encaminhar para um atendente humano.")
            return [{"event": "followup", "name": "utter_encaminhar_atendente"}]
        else:
            dispatcher.utter_message(text="Esse problema parece mais técnico. Vou te encaminhar para um atendente humano.")
            return [{"event": "followup", "name": "utter_encaminhar_atendente"}]

        return []
