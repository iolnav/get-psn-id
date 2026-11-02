# 🎮 PSN AccountID Tool (Lấy & Chuyển Đổi Mã Tài Khoản PSN)

Công cụ Python song ngữ (Tiếng Việt / English) hỗ trợ:
1. **Lấy PSN-ID** (dạng Base64) từ tài khoản PlayStation Network và **tự động chuyển đổi sang AccountID HEX** (`0x...`).
2. **Chuyển đổi PSN-ID → AccountID HEX** độc lập dành cho những ai đã có sẵn mã PSN-ID.
3. **Lưu và xem lại thông tin:** Tự động lưu thông tin vào tệp `data.json` (thời gian lấy, PSN-ID Base64, AccountID HEX) để tiện tra cứu lại mà không cần đăng nhập nhiều lần.

Dùng cho các mục đích homebrew, kích hoạt tài khoản ngoại tuyến (Offline Activation) trên PS4/PS5.

> Tham khảo script gốc của tác giả **[grill2010](https://github.com/grill2010)** và công thức chuyển đổi từ **CyberChef**.

---

## ✨ Tính năng nổi bật

- 🌐 **Hỗ trợ 2 ngôn ngữ:** Tiếng Việt và English ngay khi khởi động tool.
- ⚡ **Tự động chuyển đổi:** Sau khi đăng nhập và lấy mã PSN-ID, tool tự động chuyển đổi sang định dạng `AccountID HEX` (16 ký tự kèm tiền tố `0x`) mà không cần làm thủ công.
- 💾 **Tự động lưu vào data.json:** Lưu lại thời gian lấy dữ liệu, PSN-ID (Base64) và AccountID HEX vào tệp `data.json` ngay cạnh script.
- 📂 **Xem lại mã đã lấy (Tùy chọn 3):** Dễ dàng xem lại thông tin đã lưu trước đó mà không phải thao tác đăng nhập lại từ đầu.
- 🔄 **Chế độ chuyển đổi nhanh:** Nhập trực tiếp mã PSN-ID có sẵn để nhận ngay AccountID HEX.
- 🧭 **Điều hướng linh hoạt:** Ở bất cứ bước nhập liệu nào, bạn có thể bấm `b` để quay lại menu chính hoặc `q` để thoát.
- 💬 **Thông báo chào tạm biệt cá nhân hoá:** Tự động hiển thị lời chào theo đúng ngôn ngữ bạn đang chọn.

---

## 📋 Yêu cầu hệ thống

- Python **3.6** trở lên
- Thư viện `requests`
- Kết nối Internet và tài khoản PSN hợp lệ (đối với chức năng 1)

---

## 🚀 Hướng dẫn cài đặt & chạy môi trường ảo (venv)

> ⚠️ **Khuyến nghị bắt buộc dùng Virtual Environment (venv)** để tránh lỗi quản lý gói hệ thống (như PEP 668 trên Homebrew/Debian/Ubuntu).

---

### 🍎 macOS

> Trên macOS với Python cài qua Homebrew, hệ thống sẽ chặn `pip install` trực tiếp. Cần tạo venv như sau:

**Bước 1 — Mở Terminal, di chuyển vào thư mục chứa mã nguồn vừa tải về:**

```bash
cd /duong/dan/den/thu-muc-chua-script
# Ví dụ: cd ~/Downloads/lay-tai-khoan-psn-id
```

**Bước 2 — Tạo và kích hoạt venv:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> 💡 **Lưu ý ổ cứng ngoài (exFAT/FAT32):** Nếu bạn đặt thư mục trên USB/ổ cứng ngoài định dạng exFAT hoặc FAT32 (không hỗ trợ symlink), hãy tạo venv tại thư mục home của máy:
> ```bash
> python3 -m venv ~/psn-venv
> source ~/psn-venv/bin/activate
> cd /duong/dan/den/thu-muc-chua-script
> ```

**Bước 3 — Cài đặt thư viện:**

```bash
python3 -m pip install requests
```

**Bước 4 — Khởi chạy công cụ:**

```bash
python3 lay-tai-khoan-psn-id.py
```

**Những lần sử dụng sau chỉ cần:**

```bash
cd /duong/dan/den/thu-muc-chua-script
source .venv/bin/activate  # (hoặc source ~/psn-venv/bin/activate)
python3 lay-tai-khoan-psn-id.py
```

Khi dùng xong, gõ `deactivate` để thoát môi trường ảo.

---

### 🪟 Windows

**Bước 1 — Mở Command Prompt hoặc PowerShell**, điều hướng đến thư mục chứa mã nguồn:

```cmd
cd C:\duong\dan\den\thu-muc-chua-script
:: Ví dụ: cd %USERPROFILE%\Downloads\lay-tai-khoan-psn-id
```

**Bước 2 — Tạo và kích hoạt venv:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

> 💡 Nếu PowerShell báo lỗi *“execution of scripts is disabled on this system”*, hãy mở PowerShell và chạy:
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**Bước 3 — Cài đặt thư viện:**

```cmd
python -m pip install requests
```

*(Trên Windows, nếu chưa cài requests thì script cũng có tính năng tự động hỏi và cài đặt giúp bạn).*

**Bước 4 — Khởi chạy công cụ:**

```cmd
python lay-tai-khoan-psn-id.py
```

**Những lần sau:**

```cmd
cd C:\duong\dan\den\thu-muc-chua-script
.venv\Scripts\activate
python lay-tai-khoan-psn-id.py
```

---

### 🐧 Linux (Ubuntu / Debian)

**Bước 1 — Cài đặt các gói cần thiết:**

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y
```

**Bước 2 — Di chuyển vào thư mục và kích hoạt venv:**

```bash
cd /duong/dan/den/thu-muc-chua-script
python3 -m venv .venv
source .venv/bin/activate
```

**Bước 3 — Cài đặt thư viện:**

```bash
python3 -m pip install requests
```

**Bước 4 — Khởi chạy:**

```bash
python3 lay-tai-khoan-psn-id.py
```

---

### 🤖 Android (Termux)

**Bước 1 — Cài Termux** từ [F-Droid](https://f-droid.org/packages/com.termux/) (không dùng bản Google Play vì đã cũ).

**Bước 2 — Cài Python và cấp quyền bộ nhớ:**

```bash
termux-setup-storage
pkg update && pkg upgrade -y
pkg install python -y
```

**Bước 3 — Di chuyển vào thư mục chứa script, tạo venv và cài thư viện:**

```bash
cd /duong/dan/den/thu-muc-chua-script
# Hoặc nếu lưu ở bộ nhớ máy: cd /storage/emulated/0/Download/lay-tai-khoan-psn-id
# Hoặc thư mục home Termux: cd ~/lay-tai-khoan-psn-id

python -m venv .venv
source .venv/bin/activate
pip install requests
```

**Bước 4 — Chạy tool:**

```bash
python lay-tai-khoan-psn-id.py
```

---

## 📖 Hướng dẫn sử dụng chi tiết

### 1. Màn hình chọn ngôn ngữ
Khi mở tool, màn hình lựa chọn sẽ hiện ra:
```text
╔══════════════════════════════════════════╗
║    PSN AccountID Tool  ·  by @iolna      ║
╠══════════════════════════════════════════╣
║   1.  Ngôn ngữ : Tiếng Việt              ║
║   2.  Language : English                 ║
║   q.  Thoát / Exit                       ║
╚══════════════════════════════════════════╝
```
- Nhập `1` để chọn Tiếng Việt.
- Nhập `2` để chọn English.
- Nhập `q` để thoát (in lời chào song ngữ).

---

### 2. Menu chính
Dựa trên ngôn ngữ đã chọn, giao diện sẽ hiển thị:
```text
════════════════
   MENU CHÍNH
════════════════

1. Lấy PSN-ID (yêu cầu đăng nhập vào trang web PSN)
2. Chuyển đổi PSN-ID → AccountID HEX
3. Xem PSN-ID đã lấy
4. Quay lại
q. Thoát
```

#### 👉 Chức năng 1: Lấy PSN-ID
1. Tool cung cấp một đường link đăng nhập chính thức của Sony.
2. Sao chép liên kết, mở trong trình duyệt và tiến hành đăng nhập tài khoản PSN của bạn.
3. Khi đăng nhập xong, trang chuyển hướng đến một trang trắng hiển thị chữ `"redirect"`.
4. Sao chép toàn bộ thanh địa chỉ URL trên trình duyệt và dán lại vào Terminal.
5. Tool sẽ tự động lấy thông tin tài khoản, lấy mã **PSN-ID** (Base64) và tự động chuyển đổi sang **AccountID HEX**, sau đó hiển thị bảng tổng kết:
   ```text
   +-------------------+----------------------+
   | PSN-ID (Base64)   | AccountID HEX        |
   +-------------------+----------------------+
   | DVD4MESCAwA=      | 0x0003824430f8500d   |
   +-------------------+----------------------+
   ```
6. Tool sẽ tự động lưu thông tin vào tệp `data.json` nằm cạnh script:
   ```json
   {
     "timestamp": "2026-11-02 22:00:00",
     "psn_id_base64": "DVD4MESCAwA=",
     "account_id_hex": "0x0003824430f8500d",
     "country_code": "vn",
     "expiration": "2026-11-02T15:56:03.874Z",
     "is_sub_account": false,
     "language_code": "vi",
     "online_id": "ten_online",
     "scopes": "psn:clientapp",
     "user_id": "123456789012345"
   }
   ```
7. Bấm **Enter** để quay về Menu chính.

#### 👉 Chức năng 2: Chuyển đổi PSN-ID → AccountID HEX
- Dành cho những ai đã có sẵn mã PSN-ID Base64.
- Nhập mã vào, tool sẽ lập tức tính toán và in bảng kết quả tương ứng.
- Có thể nhập `b` để quay lại menu chính hoặc `q` để thoát.

#### 👉 Chức năng 3: Xem PSN-ID đã lấy
- Đọc và hiển thị lại dữ liệu từ tệp `data.json` bao gồm thời gian lấy dữ liệu, bảng mã PSN-ID (Base64) & AccountID HEX, kèm theo thông tin tài khoản chi tiết (`online_id`, `user_id`, `country_code`, `language_code`, `is_sub_account`, `expiration`, `scopes`).
- Giúp bạn xem lại ngay mà không phải mở trình duyệt đăng nhập lại.
- Nếu chưa từng lấy dữ liệu hoặc tệp `data.json` bị mất/hỏng, tool sẽ hiển thị thông báo hướng dẫn sử dụng chức năng 1 trước.

---

## 🔒 An toàn & Bảo mật

- Script chỉ tương tác trực tiếp với máy chủ chính thức của Sony (`sonyentertainmentnetwork.com`) qua giao thức HTTPS.
- Không có bất kỳ máy chủ bên thứ ba nào can thiệp.
- Tệp `data.json` chỉ lưu trữ cục bộ trên máy của bạn (đã được cấu hình trong `.gitignore` để không bị đẩy lên GitHub).
- Không chia sẻ các URL hoặc mã Token nhạy cảm ra ngoài.

---

## 📁 Cấu trúc tệp

```text
PSN ID/
├── lay-tai-khoan-psn-id.py    # Script chính (tích hợp song ngữ & đa tính năng)
├── data.json                  # Tệp lưu thông tin tự động sinh ra sau khi lấy ID (tuỳ chọn)
├── README.md                  # Hướng dẫn sử dụng tiếng Việt (tệp này)
└── EN_README.md               # Hướng dẫn sử dụng tiếng Anh
```

---

## 💡 Credit & Lời cảm ơn

- Cảm ơn tác giả gốc **[grill2010](https://github.com/grill2010)** đã xây dựng luồng lấy token qua remoteplay client.
- Công thức chuyển đổi: Base64 → Đảo thứ tự bytes (8-byte word swap) → Hexadecimal.
- `@iolna đã dùng AI để tạo ra cái này! Thành phố Bắc Bling kính chào quý khách! ;))`
