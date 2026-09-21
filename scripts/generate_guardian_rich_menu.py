import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_circular_mask(size, feather_start=0.75):
    """建立平滑羽化的圓形 / 圓角透明遮罩，消除圖片邊界方框感"""
    w, h = size
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    
    cx, cy = w / 2, h / 2
    rx, ry = w / 2, h / 2
    
    # 建立距離場
    for y in range(h):
        for x in range(w):
            dx = (x - cx) / rx
            dy = (y - cy) / ry
            dist = math.sqrt(dx*dx + dy*dy)
            if dist <= feather_start:
                alpha = 255
            elif dist < 1.0:
                # 平滑餘弦衰減
                factor = (dist - feather_start) / (1.0 - feather_start)
                alpha = int(255 * (0.5 + 0.5 * math.cos(factor * math.pi)))
            else:
                alpha = 0
            mask.putpixel((x, y), alpha)
    return mask

def create_guardian_rich_menu():
    width = 2500
    height = 1686
    
    # 學院深邃暗夜藍底 (Deep Academy Navy: #0A0F1D)
    base = Image.new("RGBA", (width, height), (10, 15, 29, 255))
    
    # 繪製深邃背景微光與雷電星空
    bg_overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    bg_draw = ImageDraw.Draw(bg_overlay)
    
    # 中欄高科技藍色光暈發散
    bg_draw.ellipse([800, 300, 1700, 1400], fill=(2, 132, 199, 45))
    # 左欄溫潤琥珀微光
    bg_draw.ellipse([50, 400, 780, 1100], fill=(245, 158, 11, 25))
    # 右欄青藍神盾微光
    bg_draw.ellipse([1720, 400, 2450, 1100], fill=(6, 182, 212, 30))
    
    bg_overlay = bg_overlay.filter(ImageFilter.GaussianBlur(100))
    base = Image.alpha_composite(base, bg_overlay)

    # 字型配置
    font_path = "/System/Library/Fonts/Hiragino Sans GB.ttc"
    if not os.path.exists(font_path):
        font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
    
    font_title = ImageFont.truetype(font_path, 118)
    font_sub = ImageFont.truetype(font_path, 54)

    col1_cx = 416
    col2_cx = 1250
    col3_cx = 2083

    # 圖示檔案
    brain_dir = "/Users/linyuting/.gemini/antigravity/brain/a92565cb-3865-4f7c-b880-318168d8a557"
    icon_guide_path = os.path.join(brain_dir, "icon_guide_book_1789990607661.jpg")
    icon_crystal_path = os.path.join(brain_dir, "icon_command_crystal_1789990631196.jpg")
    icon_shield_path = os.path.join(brain_dir, "icon_upgrade_shield_1789990651399.jpg")

    # --- 中間直欄：發光卡片容器 ---
    frame_box = [870, 48, 1630, height - 48]
    
    # 外發光霓虹光暈
    glow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow_layer)
    for offset in range(24, 0, -3):
        alpha = int(35 * (1 - offset / 24))
        g_draw.rounded_rectangle(
            [frame_box[0] - offset, frame_box[1] - offset, frame_box[2] + offset, frame_box[3] + offset],
            radius=45, outline=(0, 216, 246, alpha), width=4
        )
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(12))
    base = Image.alpha_composite(base, glow_layer)

    # 卡片實體背景
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(frame_box, radius=42, fill=(15, 23, 42, 240), outline=(56, 189, 248, 255), width=8)

    # --- 載入與羽化貼合圖示 ---
    # 1. 左欄圖示
    if os.path.exists(icon_guide_path):
        img_guide = Image.open(icon_guide_path).convert("RGBA").resize((760, 760), Image.Resampling.LANCZOS)
        mask_guide = create_circular_mask((760, 760), feather_start=0.72)
        base.paste(img_guide, (col1_cx - 380, 230), mask_guide)

    # 2. 中欄圖示
    if os.path.exists(icon_crystal_path):
        img_crystal = Image.open(icon_crystal_path).convert("RGBA").resize((740, 740), Image.Resampling.LANCZOS)
        mask_crystal = create_circular_mask((740, 740), feather_start=0.70)
        base.paste(img_crystal, (col2_cx - 370, 520), mask_crystal)

    # 3. 右欄圖示
    if os.path.exists(icon_shield_path):
        img_shield = Image.open(icon_shield_path).convert("RGBA").resize((780, 780), Image.Resampling.LANCZOS)
        mask_shield = create_circular_mask((780, 780), feather_start=0.72)
        base.paste(img_shield, (col3_cx - 390, 220), mask_shield)

    draw = ImageDraw.Draw(base)

    # --- 繪製文字與裝飾條 ---

    # 左欄文字（下方）
    t_text = "使用手冊"
    s_text = "4步驟快速入門"
    tb = draw.textbbox((0, 0), t_text, font=font_title)
    tw = tb[2] - tb[0]
    draw.text((col1_cx - tw // 2, 1180), t_text, fill="#FFFFFF", font=font_title)
    
    sb = draw.textbbox((0, 0), s_text, font=font_sub)
    sw = sb[2] - sb[0]
    draw.text((col1_cx - sw // 2, 1340), s_text, fill="#94A3B8", font=font_sub)

    # 中欄文字（上方）
    t_mid = "指令總覽"
    s_mid = "快捷指令與詳細對照"
    tb_m = draw.textbbox((0, 0), t_mid, font=font_title)
    tw_m = tb_m[2] - tb_m[0]
    # 雙層立體青藍文字
    draw.text((col2_cx - tw_m // 2, 142), t_mid, fill=(2, 132, 199, 255), font=font_title)
    draw.text((col2_cx - tw_m // 2, 138), t_mid, fill="#FFFFFF", font=font_title)

    sb_m = draw.textbbox((0, 0), s_mid, font=font_sub)
    sw_m = sb_m[2] - sb_m[0]
    draw.text((col2_cx - sw_m // 2, 290), s_mid, fill="#38BDF8", font=font_sub)

    # 右欄文字（下方）
    t_right = "升級方案"
    s_right = "進階催繳與專案管理"
    tb_r = draw.textbbox((0, 0), t_right, font=font_title)
    tw_r = tb_r[2] - tb_r[0]
    draw.text((col3_cx - tw_r // 2, 1180), t_right, fill="#FFFFFF", font=font_title)

    sb_r = draw.textbbox((0, 0), s_right, font=font_sub)
    sw_r = sb_r[2] - sb_r[0]
    draw.text((col3_cx - sw_r // 2, 1340), s_right, fill="#94A3B8", font=font_sub)

    # 輸出至 assets/rich_menu_2500x1686.jpg
    final_img = base.convert("RGB")
    out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "rich_menu_2500x1686.jpg")
    final_img.save(out_path, quality=95)
    print(f"Rich Menu 圖片已無縫羽化輸出至: {out_path}")

if __name__ == "__main__":
    create_guardian_rich_menu()
