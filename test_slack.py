import requests
import json

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

def test_slack():
    payload = {
        "text": "🚀 Manus 테스트 메시지: 슬랙 웹훅이 정상적으로 작동하고 있습니다!"
    }
    
    try:
        print(f"Sending test message to Slack...")
        response = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
        
        if response.status_code == 200:
            print("✅ Success! Slack response: OK")
        else:
            print(f"❌ Failed! Slack response: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    test_slack()
