from django.http import HttpResponse
from django.utils import timezone
from users.models import Vcode
from requests.sessions import Session
from requests.adapters import HTTPAdapter
import json

#
# Cron functions
#


def update_dmd_cookie(request):
    with Session() as session:
        session.mount("https://", HTTPAdapter(max_retries=3))
        response = session.get("https://util.dgufilm.link/get-dmd-cookie")
        cookie = response.text.rstrip()

    if "WMONID" in cookie:
        with open("secrets.json", "r+") as f:
            data = json.load(f)
            data["DMD_COOKIE"] = cookie
            f.seek(0)
            f.write(json.dumps(data, indent=4))
            f.truncate()

    return HttpResponse(f"dmd-cookie: {cookie}")


def delete_expired_vcodes(request):
    expired_vcodes = Vcode.objects.filter(will_expire_on__lt=timezone.now())
    count = expired_vcodes.count()
    if count > 0:
        expired_vcodes.delete()
    return HttpResponse(f"Number of deleted verification codes: {count}")
