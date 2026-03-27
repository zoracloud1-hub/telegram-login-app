import requests
import json

webhook_url = "https://discord.com/api/webhooks/1487076733583622217/PdN7RzEQ3_FbbfYYSvus3eldxNvIM_m5PViWm8h9BNqbrpcv5mcE-LzsGhTHLt6YTvPZ"

payload = {
    "content": "🚀 **Manus 테스트 메시지**\n디스코드 웹훅 연동 테스트 중입니다. 이 메시지가 보인다면 연동이 정상입니다!"
}

try:
    response = requests.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
    if response.status_code == 204:
        print("✅ 테스트 메시지 전송 성공!")
    else:
        print(f"❌ 전송 실패 (상태 코드: {response.status_code})")
        print(f"응답 내용: {response.text}")
except Exception as e:
    print(f"⚠️ 에러 발생: {str(e)}")
