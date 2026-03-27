import requests
import json

def test_telegram_send():
    bot_token = "8624261932:AAHUdfopde-6EVa5G0Df4WXMVSXS2STJccA"
    chat_id = "8792543569"
    message = "🚀 [Manus 테스트 메시지]\n\n이 메시지가 보인다면 봇 설정은 정상입니다."
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    
    print(f"Sending request to: {url}")
    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        
        if response.status_code == 200:
            print("\n✅ 메시지 전송 성공!")
        else:
            print("\n❌ 메시지 전송 실패!")
    except Exception as e:
        print(f"\n❌ 오류 발생: {str(e)}")

if __name__ == "__main__":
    test_telegram_send()
