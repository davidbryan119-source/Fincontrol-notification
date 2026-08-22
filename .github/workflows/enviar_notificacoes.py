import os
import requests

ONESIGNAL_APP_ID = "fbe16faa-197b-400d-95d1-f790aa261f2f"
ONESIGNAL_REST_API_KEY = os.getenv("ONESIGNAL_REST_API_KEY")

def enviar_notificacao():
    if not ONESIGNAL_REST_API_KEY:
        print("Erro: Chave ONESIGNAL_REST_API_KEY nao foi configurada nos Secrets!")
        return

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {ONESIGNAL_REST_API_KEY}"
    }

    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "headings": {"pt": "Lembrete FinControl Pro 🔔"},
        "contents": {"pt": "Acesse o sistema para conferir suas faturas e lancamentos do dia!"},
        "included_segments": ["Total Subscriptions"],
        "url": "https://fincontrol.netlify.app"
    }

    response = requests.post("https://onesignal.com/api/v1/notifications", headers=headers, json=payload)
    print(f"Status: {response.status_code}")
    print(f"Resposta: {response.text}")

if __name__ == "__main__":
    enviar_notificacao()
