import os
import requests

# Busca as chaves configuradas nos Secrets do GitHub
APP_ID = os.environ.get("ONESIGNAL_APP_ID")
REST_API_KEY = os.environ.get("ONESIGNAL_REST_API_KEY")

def enviar_notificacao():
    url = "https://onesignal.com/api/v1/notifications"
    
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {REST_API_KEY}"
    }
    
    payload = {
        "app_id": APP_ID,
        "included_segments": ["Total Subscriptions"],
        "contents": {
            "pt": "Lembrete FinControl: Verifique suas movimentações e pendências do dia!",
            "en": "FinControl Reminder: Check your daily transactions and pending items!"
        },
        "headings": {
            "pt": "FinControl - Notificação",
            "en": "FinControl - Notification"
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("Notificação enviada com sucesso!")
    else:
        print(f"Erro ao enviar notificação: {response.status_code} - {response.text}")

if __name__ == "__main__":
    enviar_notificacao()
