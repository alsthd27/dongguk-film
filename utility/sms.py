from django.conf import settings
from .hangul import handle_hangul
import time, hmac, hashlib, base64, requests, json

NCP_ACCESS_KEY_ID = getattr(settings, "NCP_ACCESS_KEY_ID", "NCP_ACCESS_KEY_ID")

NCP_SECRET_KEY = getattr(settings, "NCP_SECRET_KEY", "NCP_SECRET_KEY")

NCP_SENS_SMS_SERVICE_ID = getattr(
    settings, "NCP_SENS_SMS_SERVICE_ID", "NCP_SENS_SMS_SERVICE_ID"
)

MGT_PHONE = getattr(settings, "MGT_PHONE", "MGT_PHONE")

#
# Sun functions
#


def init_service():
    sid = NCP_SENS_SMS_SERVICE_ID
    sms_uri = f"/sms/v2/services/{sid}/messages"
    sms_url = f"https://sens.apigw.ntruss.com{sms_uri}"
    acc_key_id = NCP_ACCESS_KEY_ID
    acc_sec_key = bytes(NCP_SECRET_KEY, "utf-8")
    stime = int(float(time.time()) * 1000)
    hash_str = f"POST {sms_uri}\n{stime}\n{acc_key_id}"
    digest = hmac.new(
        acc_sec_key, msg=hash_str.encode("utf-8"), digestmod=hashlib.sha256
    ).digest()
    d_hash = base64.b64encode(digest).decode()
    service = {
        "sms_url": sms_url,
        "stime": str(stime),
        "acc_key_id": acc_key_id,
        "d_hash": d_hash,
    }
    return service


#
# Main functions
#


def send_sms(data):
    """
    type: "SNP"

    SNP: Sign up
    """

    # type: "SNP"
    type = data["type"]

    if type == "SNP":
        phone_vcode = data["content"]["phone_vcode"]
        raw_content = (
            f'[디닷에프] 휴대전화 번호 인증번호는 {handle_hangul(phone_vcode, "이에요예요", True)}!'
        )

    service = init_service()
    from_no = MGT_PHONE
    to_no = "".join(filter(str.isalnum, data["phone"]))
    content = raw_content
    msg_data = {
        "type": "SMS",
        "countryCode": "82",
        "from": from_no,
        "contentType": "COMM",
        "content": content,
        "messages": [{"to": to_no}],
    }
    response = requests.post(
        service["sms_url"],
        data=json.dumps(msg_data),
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "x-ncp-apigw-timestamp": service["stime"],
            "x-ncp-iam-access-key": service["acc_key_id"],
            "x-ncp-apigw-signature-v2": service["d_hash"],
        },
    )

    return response.text
