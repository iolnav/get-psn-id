#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PSN AccountID Tool — Bilingual (VI / EN)
# Chuyển đổi: From Base64 → Swap Endianness (Raw, 8 bytes) → To Hex
# https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)Swap_endianness('Raw',8,true)To_Hex('None',0)
# Credit: @iolna đã dùng AI để tạo ra cái này | Thành phố Bắc Bling kính chào quý khách! ;))

import sys

if sys.version_info < (3, 0, 0):
    print("ĐỪNG dùng Python 2. / DO NOT use Python 2.")
    sys.exit(1)

import platform
import base64
from urllib.parse import urlparse, parse_qs, quote
import pprint

current_lang = None

EXIT_MSG_BILINGUAL = (
    "@iolna đã dùng AI để tạo ra cái này! | @iolna built this with AI!\n"
    "Thành phố Bắc Bling | Bắc Bling City\n"
    "TẠM BIỆT, HẸN GẶP LẠI! | GOOD BYE SEE YOU AGAIN!"
)

# ── Giữ cửa sổ mở trên Windows khi thoát ────────────────────────────────────
_real_exit = sys.exit
def exit(code=0):
    if code == 0:
        print()
        if current_lang in UI:
            print(UI[current_lang]["exit_msg"])
        else:
            print(EXIT_MSG_BILINGUAL)
    if platform.system() == "Windows":
        input("\nNhấn Enter để thoát. / Press Enter to exit.")
    _real_exit(code)

# ── Hỗ trợ UTF-8 trên terminal ASCII ─────────────────────────────────────────
if sys.stdout.encoding.lower() == "ascii":
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer)

# ── Kiểm tra / cài requests ───────────────────────────────────────────────────
try:
    import requests
except ImportError as e:
    print(e)
    if platform.system() == "Windows":
        from distutils.util import strtobool
        a = input("requests chưa cài. Tự động cài qua pip? / Install via pip? [y/n] ")
        while True:
            try:
                a = strtobool(a)
                break
            except ValueError:
                a = input("y hoặc n / y or n: ")
        if a == 1:
            import subprocess
            subprocess.call([sys.executable, "-m", "pip", "install", "requests"])
            import requests
        else:
            exit(1)
    else:
        print("\"requests\" chưa được cài. Hãy cài bằng pip.")
        print("\"requests\" is not available. Install it with pip.")
        exit(1)

# ══════════════════════════════════════════════════════════════════════════════
# Hằng số
# ══════════════════════════════════════════════════════════════════════════════
CLIENT_ID     = "ba495a24-818c-472b-b12d-ff231c1b5745"
CLIENT_SECRET = "mvaiZkRsAsI1IBkY"
LOGIN_URL = (
    "https://auth.api.sonyentertainmentnetwork.com/2.0/oauth/authorize"
    "?service_entity=urn:service-entity:psn"
    "&response_type=code"
    "&client_id={}".format(CLIENT_ID) +
    "&redirect_uri=https://remoteplay.dl.playstation.net/remoteplay/redirect"
    "&scope=psn:clientapp"
    "&request_locale=en_US"
    "&ui=pr&service_logo=ps&layout_type=popup"
    "&smcid=remoteplay&prompt=always&PlatformPrivacyWs1=minimal&"
)
TOKEN_URL = "https://auth.api.sonyentertainmentnetwork.com/2.0/oauth/token"

# ── Chuỗi giao diện song ngữ ──────────────────────────────────────────────────
UI = {
    "vi": {
        "credit"      : "@iolna đã dùng AI để tạo ra cái này!\nThành phố Bắc Bling kính chào quý khách! ;))",
        "main_title"  : "MENU CHÍNH",
        "o1_label"    : "1. Lấy PSN-ID (yêu cầu đăng nhập vào trang web PSN)",
        "o2_label"    : "2. Chuyển đổi PSN-ID → AccountID HEX",
        "o3_label"    : "3. Quay lại",
        "oq_label"    : "q. Thoát",
        "prompt"      : "Lựa chọn của bạn: ",
        "invalid"     : "⚠️  Lựa chọn không hợp lệ. Vui lòng thử lại.",
        "nav_hint"    : "    (b = Quay lại  |  q = Thoát)",
        # Màn hình 1
        "s1_title"    : "LẤY PSN-ID",
        "s1_open"     : "➡️  Mở đường link sau trong trình duyệt và đăng nhập vào tài khoản PSN:",
        "s1_paste"    : "➡️  Sau khi trang hiện chữ \"redirect\", sao chép URL và dán vào đây:",
        "s1_no_code"  : "☠️  URL không chứa tham số code.",
        "s1_tok_req"  : "🌏 Đang yêu cầu OAuth Token...",
        "s1_warning"  : "⚠️  CẢNH BÁO: Từ đây trở đi có thể chứa thông tin nhạy cảm!",
        "s1_info_req" : "🌏 Đang lấy thông tin tài khoản...",
        "s1_info_got" : "🥦 Đã nhận thông tin tài khoản:",
        "s1_no_uid"   : "☠️  Không tìm thấy \"user_id\" trong phản hồi.",
        "s1_req_fail" : "☠️  Yêu cầu thất bại (mã lỗi {}):\n{}",
        "s1_no_tok"   : "☠️  Không tìm thấy \"access_token\" trong phản hồi:\n{}",
        "s1_psn_id"   : "🍙 PSN-ID (Base64) của bạn:",
        "s1_hex_id"   : "🔑 AccountID HEX của bạn:",
        # Màn hình 2
        "s2_title"    : "CHUYỂN ĐỔI PSN-ID → AccountID HEX",
        "s2_enter"    : "➡️  Nhập PSN-ID (Base64) của bạn:",
        "s2_empty"    : "❌  Chưa nhập PSN-ID.",
        "s2_fail"     : "❌  Chuyển đổi thất bại: {}",
        # Bảng kết quả & điều hướng
        "col1"        : "PSN-ID (Base64)",
        "col2"        : "AccountID HEX",
        "back_enter"  : "↩️  Nhấn Enter để quay lại menu chính...",
        "exit_msg"    : (
            "@iolna đã dùng AI để tạo ra cái này!\n"
            "Thành phố Bắc Bling\n"
            "TẠM BIỆT, HẸN GẶP LẠI!"
        ),
    },
    "en": {
        "credit"      : "@iolna built this with AI!\nWelcome to Bắc Bling City! ;))",
        "main_title"  : "MAIN MENU",
        "o1_label"    : "1. Get PSN-ID (requires logging into the PSN website)",
        "o2_label"    : "2. Convert PSN-ID → AccountID HEX",
        "o3_label"    : "3. Back",
        "oq_label"    : "q. Exit",
        "prompt"      : "Your choice: ",
        "invalid"     : "⚠️  Invalid choice. Please try again.",
        "nav_hint"    : "    (b = Back  |  q = Exit)",
        # Screen 1
        "s1_title"    : "GET PSN-ID",
        "s1_open"     : "➡️  Open the following URL in your browser and log in to your PSN account:",
        "s1_paste"    : "➡️  After the page shows \"redirect\", copy the URL and paste it here:",
        "s1_no_code"  : "☠️  URL did not contain a code parameter.",
        "s1_tok_req"  : "🌏 Requesting OAuth Token...",
        "s1_warning"  : "⚠️  WARNING: From this point on, output might contain sensitive information!",
        "s1_info_req" : "🌏 Requesting Account Info...",
        "s1_info_got" : "🥦 Received Account Info:",
        "s1_no_uid"   : "☠️  \"user_id\" is missing in response.",
        "s1_req_fail" : "☠️  Request failed (code {}):\n{}",
        "s1_no_tok"   : "☠️  \"access_token\" is missing in response:\n{}",
        "s1_psn_id"   : "🍙 Your PSN-ID (Base64):",
        "s1_hex_id"   : "🔑 Your AccountID HEX:",
        # Screen 2
        "s2_title"    : "CONVERT PSN-ID → AccountID HEX",
        "s2_enter"    : "➡️  Enter your PSN-ID (Base64):",
        "s2_empty"    : "❌  No PSN-ID entered.",
        "s2_fail"     : "❌  Conversion failed: {}",
        # Table & navigation
        "col1"        : "PSN-ID (Base64)",
        "col2"        : "AccountID HEX",
        "back_enter"  : "↩️  Press Enter to return to the main menu...",
        "exit_msg"    : (
            "@iolna built this with AI!\n"
            "Bắc Bling City\n"
            "GOOD BYE SEE YOU AGAIN!"
        ),
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# Hàm tiện ích
# ══════════════════════════════════════════════════════════════════════════════

def convert_to_hex(b64: str) -> str:
    """PSN AccountID (Base64) → AccountID HEX
    Pipeline: From Base64 → Swap Endianness (Raw, 8 bytes, pad) → To Hex"""
    b64 = b64.strip()
    b64 += '=' * ((4 - len(b64) % 4) % 4)
    raw = base64.b64decode(b64)
    rem = len(raw) % 8
    if rem:
        raw += b'\x00' * (8 - rem)
    swapped = b''.join(raw[i:i+8][::-1] for i in range(0, len(raw), 8))
    return "0x" + swapped.hex()


def print_header(title: str):
    line = "═" * (len(title) + 6)
    print()
    print(line)
    print("   " + title)
    print(line)
    print()


def print_table(psn_id: str, hex_id: str, s: dict):
    h1, h2 = s["col1"], s["col2"]
    w1 = max(len(h1), len(psn_id)) + 4
    w2 = max(len(h2), len(hex_id)) + 4
    sep = "+" + "-" * w1 + "+" + "-" * w2 + "+"
    fmt = "| {:<{w1}} | {:<{w2}} |"
    print(sep)
    print(fmt.format(h1, h2, w1=w1-2, w2=w2-2))
    print(sep)
    print(fmt.format(psn_id, hex_id, w1=w1-2, w2=w2-2))
    print(sep)


def ask(prompt_text: str, nav_hint: str) -> str:
    """Hiển thị gợi ý điều hướng rồi đọc input."""
    print(prompt_text)
    print(nav_hint)
    return input("> ").strip()


def handle_nav(val: str) -> str:
    """Trả về 'back' / 'quit' / 'ok' tuỳ giá trị nhập."""
    v = val.lower()
    if v == 'q':
        print()
        exit(0)
    if v == 'b':
        return 'back'
    return 'ok'

# ══════════════════════════════════════════════════════════════════════════════
# Màn hình 1: Lấy PSN-ID rồi tự động chuyển đổi sang HEX
# ══════════════════════════════════════════════════════════════════════════════

def screen_get_psn(s: dict):
    print_header(s["s1_title"])
    print(s["s1_open"])
    print()
    print(LOGIN_URL)
    print()

    raw_url = ask(s["s1_paste"], s["nav_hint"])
    if handle_nav(raw_url) == 'back':
        return

    # Parse code từ URL
    code_url = urlparse(raw_url)
    query    = parse_qs(code_url.query)
    if "code" not in query or not query["code"] or not query["code"][0]:
        print()
        print(s["s1_no_code"])
        input("\n" + s["back_enter"])
        return
    code = query["code"][0]

    print()
    print(s["s1_tok_req"])

    # Xin Token
    api_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    body = (
        "grant_type=authorization_code"
        "&code={}".format(code) +
        "&redirect_uri=https://remoteplay.dl.playstation.net/remoteplay/redirect&"
    )
    tok_req = requests.post(
        TOKEN_URL,
        auth    = api_auth,
        headers = {"Content-Type": "application/x-www-form-urlencoded"},
        data    = body.encode("ascii"),
    )
    print(s["s1_warning"])

    if tok_req.status_code != 200:
        print(s["s1_req_fail"].format(tok_req.status_code, tok_req.text))
        input("\n" + s["back_enter"])
        return

    tok_json = tok_req.json()
    if "access_token" not in tok_json:
        print(s["s1_no_tok"].format(tok_req.text))
        input("\n" + s["back_enter"])
        return
    token = tok_json["access_token"]

    # Lấy thông tin tài khoản
    print(s["s1_info_req"])
    acc_req = requests.get(TOKEN_URL + "/" + quote(token), auth=api_auth)

    if acc_req.status_code != 200:
        print(s["s1_req_fail"].format(acc_req.status_code, acc_req.text))
        input("\n" + s["back_enter"])
        return

    acc_info = acc_req.json()
    print(s["s1_info_got"])
    pprint.pprint(acc_info)
    print()

    if "user_id" not in acc_info:
        print(s["s1_no_uid"])
        input("\n" + s["back_enter"])
        return

    user_id    = int(acc_info["user_id"])
    psn_id_b64 = base64.b64encode(user_id.to_bytes(8, "little")).decode()

    print(s["s1_psn_id"])
    print(psn_id_b64)
    print()

    # Tự động chuyển đổi (không hỏi)
    hex_id = convert_to_hex(psn_id_b64)
    print(s["s1_hex_id"])
    print(hex_id)
    print()
    print_table(psn_id_b64, hex_id, s)
    print()
    print(s["credit"])

    input("\n" + s["back_enter"])

# ══════════════════════════════════════════════════════════════════════════════
# Màn hình 2: Tự nhập PSN-ID để chuyển đổi
# ══════════════════════════════════════════════════════════════════════════════

def screen_convert(s: dict):
    print_header(s["s2_title"])

    psn_id = ask(s["s2_enter"], s["nav_hint"])
    if handle_nav(psn_id) == 'back':
        return

    if not psn_id:
        print(s["s2_empty"])
        input("\n" + s["back_enter"])
        return

    try:
        hex_id = convert_to_hex(psn_id)
    except Exception as e:
        print(s["s2_fail"].format(e))
        input("\n" + s["back_enter"])
        return

    print()
    print_table(psn_id, hex_id, s)
    print()
    print(s["credit"])

    input("\n" + s["back_enter"])

# ══════════════════════════════════════════════════════════════════════════════
# Menu chính
# ══════════════════════════════════════════════════════════════════════════════

def screen_main(lang: str):
    global current_lang
    current_lang = lang
    s = UI[lang]
    try:
        while True:
            print_header(s["main_title"])
            print(s["o1_label"])
            print(s["o2_label"])
            print(s["o3_label"])
            print(s["oq_label"])
            print()
            choice = input(s["prompt"]).strip().lower()
            print()

            if choice == '1':
                screen_get_psn(s)
            elif choice == '2':
                screen_convert(s)
            elif choice == '3':
                return  # quay lại chọn ngôn ngữ
            elif choice == 'q':
                exit(0)
            else:
                print(s["invalid"])
    finally:
        current_lang = None

# ══════════════════════════════════════════════════════════════════════════════
# Màn hình chọn ngôn ngữ
# ══════════════════════════════════════════════════════════════════════════════

def screen_language():
    while True:
        print()
        print("╔══════════════════════════════════════════╗")
        print("║    PSN AccountID Tool  ·  by @iolna      ║")
        print("╠══════════════════════════════════════════╣")
        print("║   1.  Ngôn ngữ : Tiếng Việt              ║")
        print("║   2.  Language : English                  ║")
        print("║   q.  Thoát / Exit                       ║")
        print("╚══════════════════════════════════════════╝")
        print()
        choice = input("Chọn / Select: ").strip().lower()

        if choice == '1':
            screen_main("vi")
        elif choice == '2':
            screen_main("en")
        elif choice == 'q':
            exit(0)
        else:
            print("⚠️  Vui lòng chọn 1, 2 hoặc q.  /  Please choose 1, 2 or q.")

# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    screen_language()
