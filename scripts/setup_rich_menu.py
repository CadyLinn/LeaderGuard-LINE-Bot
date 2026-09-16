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
    """繪製 2500x1686 質感的莫蘭迪黑白灰三格 Rich Menu 圖片"""
    width = 2500
    height = 1686
    image = Image.new("RGB", (width, height), color="#18181B")
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

    title_font = ImageFont.truetype(font_path, 88) if font_path else ImageFont.load_default()
    subtitle_font = ImageFont.truetype(font_path, 42) if font_path else ImageFont.load_default()

    # 三個直欄區域定義（莫蘭迪黑白灰質感）
    col_w = (width - 40 * 4) // 3  # (2500 - 160) // 3 = 780
    grid_configs = [
        {
            "rect": (40, 40, 40 + col_w, height - 40),
            "bg": "#27272A",
            "border": "#3F3F46",
            "title": "指令說明",
            "subtitle": "常用指令與速查表"
        },
        {
            "rect": (40 * 2 + col_w, 40, 40 * 2 + col_w * 2, height - 40),
            "bg": "#3F3F46",
            "border": "#71717A",
            "title": "任務分工",
            "subtitle": "工作發起、認領與抽籤"
        },
        {
            "rect": (40 * 3 + col_w * 2, 40, width - 40, height - 40),
            "bg": "#27272A",
            "border": "#3F3F46",
            "title": "升級方案",
            "subtitle": "進階催繳與專案管理"
        }
    ]

    for item in grid_configs:
        x1, y1, x2, y2 = item["rect"]
        # 繪製圓角卡片
        draw.rounded_rectangle([x1, y1, x2, y2], radius=40, fill=item["bg"], outline=item["border"], width=6)
        
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        # 標題
        t_bbox = draw.textbbox((0, 0), item["title"], font=title_font)
        tw = t_bbox[2] - t_bbox[0]
        th = t_bbox[3] - t_bbox[1]
        draw.text((cx - tw // 2, cy - th - 30), item["title"], fill="#FFFFFF", font=title_font)

        # 副標題
        s_bbox = draw.textbbox((0, 0), item["subtitle"], font=subtitle_font)
        sw = s_bbox[2] - s_bbox[0]
        draw.text((cx - sw // 2, cy + 30), item["subtitle"], fill="#D4D4D8", font=subtitle_font)

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
            menu_list_resp = messaging_api.get_rich_menu_list()
            menus = getattr(menu_list_resp, "rich_menus", None) or getattr(menu_list_resp, "items", None) or []
            for m in menus:
                m_id = getattr(m, "rich_menu_id", None)
                if m_id:
                    try:
                        messaging_api.delete_rich_menu(m_id)
                        print(f"已刪除舊選單：{m_id}")
                    except Exception:
                        pass
        except Exception as e:
            print(f"清理舊選單時略過: {e}")

        print("正在產生莫蘭迪黑白灰三格 Rich Menu 圖片...")
        img_bytes = create_rich_menu_image()

        print("正在註冊新的三格 Rich Menu 設定...")
        rich_menu_req = RichMenuRequest(
            size=RichMenuSize(width=2500, height=1686),
            selected=True,
            name="LeaderGuard_Morandi_3Grid_Menu",
            chat_bar_text="小組功能選單",
            areas=[
                # 左 1：指令說明 (/常用指令說明)
                RichMenuArea(
                    bounds=RichMenuBounds(x=0, y=0, width=833, height=1686),
                    action=MessageAction(text="/常用指令說明")
                ),
                # 中 2：任務分工 (/選單)
                RichMenuArea(
                    bounds=RichMenuBounds(x=833, y=0, width=834, height=1686),
                    action=MessageAction(text="/選單")
                ),
                # 右 3：升級方案 (/升級方案)
                RichMenuArea(
                    bounds=RichMenuBounds(x=1667, y=0, width=833, height=1686),
                    action=MessageAction(text="/升級方案")
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
        print("三格莫蘭迪 Rich Menu 圖文選單已成功設定完成並生效！")

if __name__ == "__main__":
    main()
