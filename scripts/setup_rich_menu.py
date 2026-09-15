import os
from io import BytesIO
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    MessagingApiBlob,
    RichMenuRequest,
    RichMenuSize,
    RichMenuArea,
    RichMenuBounds,
    MessageAction
)

load_dotenv()

ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")

def create_rich_menu_image():
    """繪製 2500x1686 質感的四宮格 Rich Menu 圖片"""
    width = 2500
    height = 1686
    image = Image.new("RGB", (width, height), color="#0F172A")
    draw = ImageDraw.Draw(image)

    # 尋找中文字型
    font_candidates = [
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/STHeiti Light.ttc"
    ]
    font_path = None
    for p in font_candidates:
        if os.path.exists(p):
            font_path = p
            break

    title_font = ImageFont.truetype(font_path, 80) if font_path else ImageFont.load_default()
    subtitle_font = ImageFont.truetype(font_path, 46) if font_path else ImageFont.load_default()

    # 四個區域定義
    grid_configs = [
        {
            "rect": (20, 20, 1230, 823),
            "bg": "#1E293B",
            "border": "#38BDF8",
            "title": "使用指南",
            "subtitle": "查看所有功能與常用指令"
        },
        {
            "rect": (1270, 20, 2480, 823),
            "bg": "#0F766E",
            "border": "#2DD4BF",
            "title": "發起任務",
            "subtitle": "建立小組工作並讓大家認領"
        },
        {
            "rect": (20, 863, 1230, 1666),
            "bg": "#334155",
            "border": "#94A3B8",
            "title": "任務清單",
            "subtitle": "查看目前分工與認領現況"
        },
        {
            "rect": (1270, 863, 2480, 1666),
            "bg": "#0284C7",
            "border": "#38BDF8",
            "title": "🎲  抽籤分工",
            "subtitle": "沒人認領的工作直接抽籤"
        }
    ]

    for item in grid_configs:
        x1, y1, x2, y2 = item["rect"]
        # 繪製圓角卡片
        draw.rounded_rectangle([x1, y1, x2, y2], radius=32, fill=item["bg"], outline=item["border"], width=6)
        
        # 計算文字置中
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        # 標題
        t_bbox = draw.textbbox((0, 0), item["title"], font=title_font)
        tw = t_bbox[2] - t_bbox[0]
        th = t_bbox[3] - t_bbox[1]
        draw.text((cx - tw // 2, cy - th - 15), item["title"], fill="#FFFFFF", font=title_font)

        # 副標題
        s_bbox = draw.textbbox((0, 0), item["subtitle"], font=subtitle_font)
        sw = s_bbox[2] - s_bbox[0]
        draw.text((cx - sw // 2, cy + 20), item["subtitle"], fill="#E2E8F0", font=subtitle_font)

    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format="PNG")
    return img_byte_arr.getvalue()

def main():
    channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    if not channel_access_token:
        print("錯誤：找不到 LINE_CHANNEL_ACCESS_TOKEN，請檢查 .env 檔案！")
        return

    with ApiClient(Configuration(access_token=channel_access_token)) as api_client:
        messaging_api = MessagingApi(api_client)
        messaging_blob_api = MessagingApiBlob(api_client)

        print("正在清理舊的 Rich Menu...")
        try:
            menu_list = messaging_api.get_rich_menu_list()
            for m in menu_list.rich_menus:
                messaging_api.delete_rich_menu(m.rich_menu_id)
                print(f"已刪除舊選單：{m.rich_menu_id}")
        except Exception as e:
            print(f"清理舊選單時略過: {e}")

        print("正在產生 Rich Menu 圖片...")
        img_bytes = create_rich_menu_image()

        print("正在註冊新的 Rich Menu 設定...")
        rich_menu_req = RichMenuRequest(
            size=RichMenuSize(width=2500, height=1686),
            selected=True,
            name="LeaderGuard_Default_Menu",
            chat_bar_text="小組專案選單",
            areas=[
                # 左上：指令手冊 (/help)
                RichMenuArea(
                    bounds=RichMenuBounds(x=0, y=0, width=1250, height=843),
                    action=MessageAction(text="/help")
                ),
                # 右上：發起任務範本 (/task 範本)
                RichMenuArea(
                    bounds=RichMenuBounds(x=1250, y=0, width=1250, height=843),
                    action=MessageAction(text="/task 範本")
                ),
                # 左下：任務清單 (/task 清單)
                RichMenuArea(
                    bounds=RichMenuBounds(x=0, y=843, width=1250, height=843),
                    action=MessageAction(text="/task 清單")
                ),
                # 右下：死鬥輪盤 (/roulette)
                RichMenuArea(
                    bounds=RichMenuBounds(x=1250, y=843, width=1250, height=843),
                    action=MessageAction(text="/roulette")
                )
            ]
        )

        created_menu = messaging_api.create_rich_menu(rich_menu_req)
        rich_menu_id = created_menu.rich_menu_id
        print(f"Rich Menu 已建立，ID: {rich_menu_id}")

        print("正在上傳選單圖片...")
        messaging_blob_api.set_rich_menu_image(
            rich_menu_id=rich_menu_id,
            body=img_bytes,
            _headers={"Content-Type": "image/png"}
        )
        print("圖片上傳成功！")

        print("正在設為預設 Rich Menu（全體使用者可見）...")
        messaging_api.set_default_rich_menu(rich_menu_id)
        print("Rich Menu 圖文選單已成功設定完成並生效！")

if __name__ == "__main__":
    main()
