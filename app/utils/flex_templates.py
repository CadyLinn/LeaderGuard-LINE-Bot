import os
import json
from linebot.v3.messaging import (
    FlexMessage,
    FlexContainer,
    QuickReply,
    QuickReplyItem,
    MessageAction
)

BASE_URL = os.getenv("BASE_URL", "https://leaderguard-line-bot.onrender.com").rstrip("/")

def get_main_quick_reply() -> QuickReply:
    """聊天室底部的常駐快捷按鈕列"""
    return QuickReply(items=[
        QuickReplyItem(action=MessageAction(label="任務分工", text="/選單")),
        QuickReplyItem(action=MessageAction(label="任務清單", text="/task 清單")),
        QuickReplyItem(action=MessageAction(label="🎲 命運抽籤", text="/命運抽籤")),
        QuickReplyItem(action=MessageAction(label="專案進度", text="/status")),
        QuickReplyItem(action=MessageAction(label="指令說明", text="/常用指令說明")),
    ])

def create_preset_tasks_carousel() -> FlexMessage:
    """常見小組專案工作範本輪播卡片（JoJo 瘋狂鑽石波普風，遵循 Apple HIG 高對比按鈕）"""
    carousel_contents = [
        # 卡片 1：簡報製作
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#160F29",
                "paddingAll": "16px",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {"type": "text", "text": "【專業分工】", "size": "xxs", "color": "#06B6D4", "weight": "bold"},
                            {"type": "text", "text": "HOT", "size": "xxs", "color": "#F43F5E", "align": "end", "weight": "bold"}
                        ]
                    },
                    {"type": "text", "text": "簡報製作與美編", "weight": "bold", "color": "#FFFFFF", "size": "md", "margin": "xs"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#1E1636",
                "borderColor": "#06B6D4",
                "borderWidth": "1px",
                "contents": [
                    {"type": "text", "text": "核心職責：", "weight": "bold", "size": "xs", "color": "#FDE047"},
                    {"type": "text", "text": "• 統整組員文字與圖表\n• PPT / Canva 視覺專業美化\n• 彙整報告講稿備忘錄", "size": "xs", "color": "#F3E8FF", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#160F29",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "認領責任：建立任務",
                            "text": "/task 新增 簡報製作與美化 負責PPT視覺美編與排版"
                        },
                        "style": "primary",
                        "color": "#E11D48",
                        "height": "sm"
                    }
                ]
            }
        },
        # 卡片 2：口頭報告
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#160F29",
                "paddingAll": "16px",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {"type": "text", "text": "【專業分工】", "size": "xxs", "color": "#06B6D4", "weight": "bold"},
                            {"type": "text", "text": "FOCUS", "size": "xxs", "color": "#FDE047", "align": "end", "weight": "bold"}
                        ]
                    },
                    {"type": "text", "text": "上台口頭報告", "weight": "bold", "color": "#FFFFFF", "size": "md", "margin": "xs"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#1E1636",
                "borderColor": "#F43F5E",
                "borderWidth": "1px",
                "contents": [
                    {"type": "text", "text": "核心職責：", "weight": "bold", "size": "xs", "color": "#FDE047"},
                    {"type": "text", "text": "• 掌握專案全脈絡\n• 代表小組自信發表\n• 現場教授提問沉著應對", "size": "xs", "color": "#F3E8FF", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#160F29",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "認領責任：建立任務",
                            "text": "/task 新增 上台口頭報告 負責掌握專案脈絡並代表口頭發表"
                        },
                        "style": "primary",
                        "color": "#E11D48",
                        "height": "sm"
                    }
                ]
            }
        },
        # 卡片 3：文獻與資料蒐集
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#160F29",
                "paddingAll": "16px",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {"type": "text", "text": "【專業分工】", "size": "xxs", "color": "#06B6D4", "weight": "bold"},
                            {"type": "text", "text": "KEY", "size": "xxs", "color": "#06B6D4", "align": "end", "weight": "bold"}
                        ]
                    },
                    {"type": "text", "text": "文獻查證與資料蒐集", "weight": "bold", "color": "#FFFFFF", "size": "md", "margin": "xs"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#1E1636",
                "borderColor": "#06B6D4",
                "borderWidth": "1px",
                "contents": [
                    {"type": "text", "text": "核心職責：", "weight": "bold", "size": "xs", "color": "#FDE047"},
                    {"type": "text", "text": "• 前期專案主題地毯式調研\n• 相關文獻與真實案例查證\n• 數據統整與來源佐證", "size": "xs", "color": "#F3E8FF", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#160F29",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "認領責任：建立任務",
                            "text": "/task 新增 文獻查證與資料蒐集 負責前期調研、文獻查證與數據整理"
                        },
                        "style": "primary",
                        "color": "#E11D48",
                        "height": "sm"
                    }
                ]
            }
        },
        # 卡片 4：書面報告統整
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#160F29",
                "paddingAll": "16px",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {"type": "text", "text": "【專業分工】", "size": "xxs", "color": "#06B6D4", "weight": "bold"},
                            {"type": "text", "text": "CORE", "size": "xxs", "color": "#FDE047", "align": "end", "weight": "bold"}
                        ]
                    },
                    {"type": "text", "text": "書面報告撰寫統整", "weight": "bold", "color": "#FFFFFF", "size": "md", "margin": "xs"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#1E1636",
                "borderColor": "#F43F5E",
                "borderWidth": "1px",
                "contents": [
                    {"type": "text", "text": "核心職責：", "weight": "bold", "size": "xs", "color": "#FDE047"},
                    {"type": "text", "text": "• 彙整各章節文字與圖表\n• 校對格式排版與文獻引用\n• 產出完整清晰期末正式報告", "size": "xs", "color": "#F3E8FF", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#160F29",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "認領責任：建立任務",
                            "text": "/task 新增 書面報告撰寫統整 負責期末書面Word/PDF格式與內容校對"
                        },
                        "style": "primary",
                        "color": "#E11D48",
                        "height": "sm"
                    }
                ]
            }
        },
        # 卡片 5：一鍵批次建立全套（神級效率分工卡）
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#2A0845",
                "borderColor": "#FDE047",
                "borderWidth": "2px",
                "paddingAll": "16px",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {"type": "text", "text": "【效率神技】", "size": "xxs", "color": "#FDE047", "weight": "bold"},
                            {"type": "text", "text": "ALL IN ONE", "size": "xxs", "color": "#06B6D4", "align": "end", "weight": "bold"}
                        ]
                    },
                    {"type": "text", "text": "一鍵全套分工建立！", "weight": "bold", "color": "#FDE047", "size": "md", "margin": "xs"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#1E1636",
                "contents": [
                    {"type": "text", "text": "小組長必備效率神器", "weight": "bold", "size": "sm", "color": "#06B6D4"},
                    {"type": "text", "text": "一次建立 4 大標準分工（簡報、報告、調研、書面），責任清楚、拒絕摸魚！", "size": "xs", "color": "#F3E8FF", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#160F29",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "⚡️ 一鍵全套分工建立",
                            "text": "/task 批次建立"
                        },
                        "style": "primary",
                        "color": "#0891B2",
                        "height": "sm"
                    }
                ]
            }
        },
        # 卡片 6：自訂其他工作
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#160F29",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "➕ 自訂專屬小組任務", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#1E1636",
                "borderColor": "#06B6D4",
                "borderWidth": "1px",
                "contents": [
                    {"type": "text", "text": "拒絕摸魚！（自訂全新任務）", "weight": "bold", "size": "sm", "color": "#FDE047"},
                    {"type": "text", "text": "點擊下方按鈕，對話框會自動帶入指令，由你親手命名全新任務！", "size": "xs", "color": "#F3E8FF", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#160F29",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "postback",
                            "label": "點我自訂輸入工作",
                            "data": "action=prompt_custom_task",
                            "inputOption": "openKeyboard",
                            "fillInText": "/任務 新增 "
                        },
                        "style": "primary",
                        "color": "#E11D48",
                        "height": "sm"
                    }
                ]
            }
        }
    ]

    carousel = {
        "type": "carousel",
        "contents": carousel_contents
    }

    return FlexMessage(
        alt_text="小組專案常用分工範本（波普美漫版）",
        contents=FlexContainer.from_dict(carousel),
        quick_reply=get_main_quick_reply()
    )

def create_main_menu_flex() -> FlexMessage:
    """小組功能主選單卡片（簡潔現代風：高對比、鮮明按鈕）"""
    bubble = {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#160F29",
            "paddingAll": "20px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "組長保險 LEADERGUARD", "weight": "bold", "color": "#FDE047", "size": "xs", "letterSpacing": "1px"},
                        {"type": "text", "text": "ACTIVE", "weight": "bold", "color": "#06B6D4", "size": "xs", "align": "end"}
                    ]
                },
                {
                    "type": "text",
                    "text": "小組協作・神隊友功能選單",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "lg",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "專案進度自動透明追蹤，輕鬆分工不當工具人",
                    "color": "#94A3B8",
                    "size": "xs",
                    "margin": "xs"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "backgroundColor": "#100B1E",
            "paddingAll": "16px",
            "contents": [
                # 區塊 1：專案工作分工
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E1636",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#06B6D4",
                    "borderWidth": "1.5px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "專案工作分工",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#06B6D4"
                        },
                        {
                            "type": "text",
                            "text": "標準工作範本一鍵發起，清楚記錄每位成員責任",
                            "size": "xs",
                            "color": "#F3E8FF",
                            "margin": "xs",
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "sm",
                            "margin": "md",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "分工範本",
                                        "text": "/task 範本"
                                    },
                                    "style": "primary",
                                    "color": "#E11D48",
                                    "height": "sm"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "任務清單",
                                        "text": "/task 清單"
                                    },
                                    "style": "primary",
                                    "color": "#0891B2",
                                    "height": "sm"
                                }
                            ]
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "自訂新增工作",
                                "data": "action=prompt_custom_task",
                                "inputOption": "openKeyboard",
                                "fillInText": "/任務 新增 "
                            },
                            "style": "secondary",
                            "color": "#2D224D",
                            "height": "sm",
                            "margin": "sm"
                        }
                    ]
                },
                # 區塊 2：命運抽籤輪盤
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E1636",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#F43F5E",
                    "borderWidth": "1.5px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "🎲 命運抽籤",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#F43F5E"
                        },
                        {
                            "type": "text",
                            "text": "工作沒人認領？交給命運抽籤，優先抽尚未負責之組員",
                            "size": "xs",
                            "color": "#F3E8FF",
                            "margin": "xs",
                            "wrap": True
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "🎲 啟動命運抽籤",
                                "text": "/命運抽籤"
                            },
                            "style": "primary",
                            "color": "#E11D48",
                            "margin": "md",
                            "height": "sm"
                        }
                    ]
                },
                # 區塊 3：進度追蹤與期末結算
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E1636",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#FDE047",
                    "borderWidth": "1.5px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "進度追蹤與結算",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#FDE047"
                        },
                        {
                            "type": "text",
                            "text": "即時掌握小組完成度，隨時產出完整專案紀錄",
                            "size": "xs",
                            "color": "#F3E8FF",
                            "margin": "xs",
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "sm",
                            "margin": "md",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "專案進度",
                                        "text": "/status"
                                    },
                                    "style": "primary",
                                    "color": "#0891B2",
                                    "height": "sm"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "匯出紀錄",
                                        "text": "/export"
                                    },
                                    "style": "primary",
                                    "color": "#9333EA",
                                    "height": "sm"
                                }
                            ]
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "指令手冊",
                                "text": "/常用指令說明"
                            },
                            "style": "secondary",
                            "color": "#2D224D",
                            "height": "sm",
                            "margin": "sm"
                        }
                    ]
                }
            ]
        }
    }
    return FlexMessage(
        alt_text="【組長保險】專案協作功能選單",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_help_flex() -> FlexMessage:
    """操作指南 Flex 卡片（JoJo 漫畫風格表格化速查表，清晰易讀）"""
    table_data = [
        ("挑選範本", "/任務 範本", "/task"),
        ("查看工作", "/任務 清單", "/tasks"),
        ("認領工作", "/認領 [編號]", "/claim"),
        ("自訂任務", "/任務 新增", "/task add"),
        ("🎲 命運抽籤", "/抽籤", "/roulette"),
        ("幽靈組員", "/成員 新增", "/member add"),
        ("組員名冊", "/成員", "/member"),
        ("專案進度", "/狀態", "/status")
    ]

    rows = []
    for idx, (func, cn, en) in enumerate(table_data):
        bg_color = "#1E1636" if idx % 2 == 0 else "#160F29"
        rows.append({
            "type": "box",
            "layout": "horizontal",
            "backgroundColor": bg_color,
            "paddingVertical": "8px",
            "paddingHorizontal": "10px",
            "alignItems": "center",
            "contents": [
                {"type": "text", "text": func, "size": "xs", "weight": "bold", "color": "#FFFFFF", "flex": 3, "wrap": True},
                {"type": "text", "text": cn, "size": "xs", "weight": "bold", "color": "#06B6D4", "flex": 4, "wrap": True},
                {"type": "text", "text": en, "size": "xs", "color": "#FDE047", "flex": 3, "wrap": True}
            ]
        })

    bubble = {
        "type": "bubble",
        "size": "giga",
        "hero": {
            "type": "image",
            "url": f"{BASE_URL}/assets/hero_command_v2026.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#160F29",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "【指令速查指南】", "size": "xs", "color": "#FDE047", "weight": "bold"},
                        {"type": "text", "text": "GUIDE", "size": "xs", "color": "#F43F5E", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": "常用指令說明・速查手冊",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "指令前加「/」，輸入中文或英文都可以發動！",
                    "color": "#06B6D4",
                    "size": "xs",
                    "margin": "xs",
                    "wrap": True
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "backgroundColor": "#100B1E",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "backgroundColor": "#2A0845",
                    "borderColor": "#FDE047",
                    "borderWidth": "1px",
                    "paddingVertical": "8px",
                    "paddingHorizontal": "10px",
                    "cornerRadius": "4px",
                    "contents": [
                        {"type": "text", "text": "發動行動", "weight": "bold", "size": "xs", "color": "#FDE047", "flex": 3},
                        {"type": "text", "text": "中文指令", "weight": "bold", "size": "xs", "color": "#06B6D4", "flex": 4},
                        {"type": "text", "text": "英文指令", "weight": "bold", "size": "xs", "color": "#F3E8FF", "flex": 3}
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xs",
                    "contents": rows
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "md",
                    "paddingAll": "10px",
                    "backgroundColor": "#1E1636",
                    "borderColor": "#06B6D4",
                    "borderWidth": "1px",
                    "cornerRadius": "6px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "• 認領示範：/認領 T001（或 /claim T001）\n• 幽靈組員：/成員 新增 小明 小華\n• 抽籤機制：🎲 命運之輪優先鎖定尚未認領任何工作的人！",
                            "size": "xxs",
                            "color": "#F3E8FF",
                            "wrap": True
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "backgroundColor": "#160F29",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "➕ 點此自訂新增工作",
                        "data": "action=prompt_custom_task",
                        "inputOption": "openKeyboard",
                        "fillInText": "/任務 新增 "
                    },
                    "style": "primary",
                    "color": "#E11D48",
                    "height": "sm"
                }
            ]
        }
    }
    return FlexMessage(
        alt_text="組長保險・常用指令說明",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_task_created_flex(task_id: str, title: str, description: str, creator_name: str) -> FlexMessage:
    """任務建立成功通知卡片（JoJo 漫畫戰鬥登場風格）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#160F29",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "【新任務建立】", "size": "xs", "color": "#06B6D4", "weight": "bold"},
                        {"type": "text", "text": "NEW", "size": "xs", "color": "#FDE047", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": "小組工作已正式指派！",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md",
                    "margin": "xs"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "paddingAll": "16px",
            "backgroundColor": "#1E1636",
            "contents": [
                {
                    "type": "text",
                    "text": f"【{task_id}】{title}",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FDE047",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": description if description else "（無補充說明）",
                    "size": "xs",
                    "color": "#F3E8FF",
                    "wrap": True
                },
                {"type": "separator", "color": "#4C1D95"},
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "任務發起人", "size": "xs", "color": "#06B6D4"},
                        {"type": "text", "text": creator_name, "size": "xs", "color": "#FFFFFF", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "當前狀態", "size": "xs", "color": "#06B6D4"},
                        {"type": "text", "text": "待認領（尚未認領）", "size": "xs", "color": "#F43F5E", "align": "end", "weight": "bold"}
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "backgroundColor": "#160F29",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "我來負責！認領此任務",
                        "text": f"/claim {task_id}"
                    },
                    "style": "primary",
                    "color": "#E11D48",
                    "height": "sm"
                }
            ]
        }
    }
    return FlexMessage(
        alt_text=f"新任務待認領：{title}",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_task_list_flex(tasks: list) -> FlexMessage:
    """任務清單卡片（JoJo 狂氣波普風格，按鈕鮮明高對比）"""
    if not tasks:
        item_boxes = [{
            "type": "text",
            "text": "目前沒有任何待辦任務！小組全員安全進入休假領域！",
            "size": "sm",
            "color": "#06B6D4",
            "align": "center",
            "margin": "lg"
        }]
        footer_box = {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "paddingAll": "12px",
            "backgroundColor": "#160F29",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "➕ 自訂新增工作",
                        "data": "action=prompt_custom_task",
                        "inputOption": "openKeyboard",
                        "fillInText": "/任務 新增 "
                    },
                    "style": "primary",
                    "color": "#E11D48",
                    "height": "sm"
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "瀏覽常用範本",
                        "text": "/task 範本"
                    },
                    "style": "primary",
                    "color": "#0891B2",
                    "height": "sm"
                }
            ]
        }
    else:
        item_boxes = []
        has_pending = False
        for t in tasks[:8]:
            is_pending = (t.get("status") == "pending")
            task_id = t.get("id", "T000")
            title = t.get("title", "")
            
            if is_pending:
                has_pending = True
                item_boxes.append({
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "md",
                    "alignItems": "center",
                    "backgroundColor": "#1E1636",
                    "borderColor": "#F43F5E",
                    "borderWidth": "1.5px",
                    "cornerRadius": "8px",
                    "paddingAll": "10px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 8,
                            "contents": [
                                {
                                    "type": "text",
                                    "text": f"[{task_id}] {title}",
                                    "size": "sm",
                                    "weight": "bold",
                                    "color": "#FFFFFF",
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "尚未認領（待認領）",
                                    "size": "xxs",
                                    "color": "#F43F5E",
                                    "weight": "bold"
                                }
                            ]
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "認領",
                                "text": f"/claim {task_id}"
                            },
                            "style": "primary",
                            "color": "#E11D48",
                            "height": "sm",
                            "flex": 3
                        }
                    ]
                })
            else:
                assignee_name = t.get("assignee_name", "組員")
                item_boxes.append({
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "md",
                    "alignItems": "center",
                    "backgroundColor": "#160F29",
                    "borderColor": "#4C1D95",
                    "borderWidth": "1px",
                    "cornerRadius": "8px",
                    "paddingAll": "10px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 8,
                            "contents": [
                                {
                                    "type": "text",
                                    "text": f"[{task_id}] {title}",
                                    "size": "sm",
                                    "color": "#A78BFA",
                                    "wrap": True
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 4,
                            "contents": [
                                {
                                    "type": "text",
                                    "text": f"👤 {assignee_name}",
                                    "size": "xs",
                                    "color": "#06B6D4",
                                    "align": "end",
                                    "weight": "bold",
                                    "wrap": True
                                }
                            ]
                        }
                    ]
                })

        footer_buttons = [
            {
                "type": "button",
                "action": {
                    "type": "postback",
                    "label": "➕ 自訂新增工作",
                    "data": "action=prompt_custom_task",
                    "inputOption": "openKeyboard",
                    "fillInText": "/任務 新增 "
                },
                "style": "secondary",
                "color": "#2D224D",
                "height": "sm"
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "常用分工範本",
                    "text": "/task 範本"
                },
                "style": "primary",
                "color": "#0891B2",
                "height": "sm"
            }
        ]
        if has_pending:
            footer_buttons.insert(0, {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "🎲 啟動命運抽籤未認領工作",
                    "text": "/命運抽籤"
                },
                "style": "primary",
                "color": "#E11D48",
                "height": "sm",
                "margin": "sm"
            })
            
        footer_box = {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "paddingAll": "12px",
            "backgroundColor": "#160F29",
            "contents": footer_buttons
        }

    bubble = {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#160F29",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "【工作存證現況】", "size": "xs", "color": "#06B6D4", "weight": "bold"},
                        {"type": "text", "text": "STATUS", "size": "xs", "color": "#F43F5E", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": "小組專案責任清單",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "分工進度透明公開，誰在付出全都清楚記錄！",
                    "color": "#FDE047",
                    "size": "xs",
                    "margin": "xs",
                    "wrap": True
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "16px",
            "backgroundColor": "#100B1E",
            "contents": item_boxes
        },
        "footer": footer_box
    }
    return FlexMessage(
        alt_text="小組專案任務清單",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_roulette_flex(task_id: str, task_title: str, victim_name: str) -> FlexMessage:
    """🎲 隨機抽籤結果卡片（命運輪盤風格）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#2A0845",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "🎲 命運抽籤", "size": "xs", "color": "#FDE047", "weight": "bold"},
                        {"type": "text", "text": "LUCKY", "size": "xs", "color": "#06B6D4", "align": "end", "weight": "bold"}
                    ]
                },
                {"type": "text", "text": "這就是命運的安排！", "weight": "bold", "color": "#FFFFFF", "size": "md", "align": "center", "margin": "xs"}
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "paddingAll": "16px",
            "backgroundColor": "#100B1E",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E1636",
                    "borderColor": "#E11D48",
                    "borderWidth": "2px",
                    "cornerRadius": "8px",
                    "paddingAll": "16px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "命運選中的天選隊友：",
                            "size": "xs",
                            "color": "#06B6D4",
                            "align": "center"
                        },
                        {
                            "type": "text",
                            "text": victim_name,
                            "weight": "bold",
                            "size": "xl",
                            "color": "#FDE047",
                            "align": "center",
                            "wrap": True,
                            "margin": "sm"
                        },
                        {"type": "separator", "color": "#4C1D95", "margin": "md"},
                        {
                            "type": "text",
                            "text": f"扛下重任：【{task_id}】{task_title}",
                            "size": "sm",
                            "color": "#FFFFFF",
                            "wrap": True,
                            "weight": "bold",
                            "margin": "md"
                        },
                        {
                            "type": "text",
                            "text": "天選之人！這項任務就交給你了，全組看好你！",
                            "size": "xs",
                            "color": "#F43F5E",
                            "align": "center",
                            "margin": "sm",
                            "weight": "bold"
                        }
                    ]
                }
            ]
        }
    }
    return FlexMessage(
        alt_text=f"🎲 抽籤結果：由 {victim_name} 負責 {task_title}",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_welcome_guide_flex() -> FlexMessage:
    """加入好友時發送的 4 步驟使用手冊 Flex 卡片（JoJo 瘋狂鑽石波普風）"""
    manual_url = os.getenv("MANUAL_URL", "")
    group_invite_url = os.getenv("GROUP_INVITE_URL", "https://line.me/R/nv/recommendOA/@805yffpw")

    manual_action = (
        {"type": "uri", "label": "查看完整秘笈手冊", "uri": manual_url}
        if manual_url
        else {"type": "message", "label": "查看完整秘笈手冊", "text": "/常用指令說明"}
    )

    bubble = {
        "type": "bubble",
        "size": "mega",
        "hero": {
            "type": "image",
            "url": f"{BASE_URL}/assets/hero_guide_v2026.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#160F29",
            "paddingAll": "20px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "【新手入門指引】", "size": "xs", "weight": "bold", "color": "#FDE047"},
                        {"type": "text", "text": "START", "size": "xs", "weight": "bold", "color": "#06B6D4", "align": "end"}
                    ]
                },
                {
                    "type": "text",
                    "text": "4 步驟告別組長噩夢！",
                    "size": "xl",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "margin": "sm"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#100B1E",
            "paddingAll": "20px",
            "spacing": "md",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E1435",
                    "cornerRadius": "10px",
                    "borderColor": "#06B6D4",
                    "borderWidth": "2px",
                    "paddingAll": "12px",
                    "spacing": "xs",
                    "contents": [
                        # Step 1
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "md",
                            "alignItems": "center",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "width": "26px",
                                    "height": "26px",
                                    "cornerRadius": "13px",
                                    "backgroundColor": "#FDE047",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                    "contents": [
                                        { "type": "text", "text": "1", "size": "xs", "weight": "bold", "color": "#160F29", "align": "center" }
                                    ]
                                },
                                {
                                    "type": "text",
                                    "text": "把我加進「群組」",
                                    "size": "sm",
                                    "color": "#FDE047",
                                    "weight": "bold",
                                    "flex": 1
                                }
                            ]
                        },
                        { "type": "separator", "color": "#2A1B4E" },
                        # Step 2
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "md",
                            "alignItems": "center",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "width": "26px",
                                    "height": "26px",
                                    "cornerRadius": "13px",
                                    "backgroundColor": "#0891B2",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                    "contents": [
                                        { "type": "text", "text": "2", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center" }
                                    ]
                                },
                                {
                                    "type": "text",
                                    "text": "輸入 /assign 發起分工",
                                    "size": "sm",
                                    "color": "#FFFFFF",
                                    "weight": "bold",
                                    "flex": 1
                                }
                            ]
                        },
                        { "type": "separator", "color": "#2A1B4E" },
                        # Step 3
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "md",
                            "alignItems": "center",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "width": "26px",
                                    "height": "26px",
                                    "cornerRadius": "13px",
                                    "backgroundColor": "#E11D48",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                    "contents": [
                                        { "type": "text", "text": "3", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center" }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "spacing": "sm",
                                    "alignItems": "center",
                                    "flex": 1,
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "沈靜30分鐘自動標註",
                                            "size": "sm",
                                            "color": "#FFFFFF",
                                            "weight": "bold",
                                            "flex": 0
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "flex": 0,
                                            "backgroundColor": "#E11D48",
                                            "cornerRadius": "3px",
                                            "paddingStart": "5px",
                                            "paddingEnd": "5px",
                                            "paddingTop": "1px",
                                            "paddingBottom": "1px",
                                            "contents": [
                                                {"type": "text", "text": "PRO", "size": "xxs", "color": "#FFFFFF", "weight": "bold"}
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        { "type": "separator", "color": "#2A1B4E" },
                        # Step 4
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "md",
                            "alignItems": "center",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "width": "26px",
                                    "height": "26px",
                                    "cornerRadius": "13px",
                                    "backgroundColor": "#9333EA",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                    "contents": [
                                        { "type": "text", "text": "4", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center" }
                                    ]
                                },
                                {
                                    "type": "text",
                                    "text": "輸入 /export 匯出鐵證",
                                    "size": "sm",
                                    "color": "#FFFFFF",
                                    "weight": "bold",
                                    "flex": 1
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "backgroundColor": "#160F29",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "color": "#E11D48",
                    "action": {
                        "type": "message",
                        "label": "了解 PRO 專案",
                        "text": "/升級方案"
                    }
                }
            ],
            "flex": 0
        }
    }

    return FlexMessage(
        alt_text="組長保險 LeaderGuard - 4 步驟使用手冊",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_upgrade_plan_flex() -> FlexMessage:
    """升級方案卡片（JoJo 狂氣波普風格：高對比、鮮明按鈕）"""
    bubble = {
        "type": "bubble",
        "size": "giga",
        "hero": {
            "type": "image",
            "url": f"{BASE_URL}/assets/hero_upgrade_v2026.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#160F29",
            "paddingAll": "20px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "組長保險 LEADERGUARD", "size": "xs", "color": "#FDE047", "weight": "bold", "letterSpacing": "1px"},
                        {"type": "text", "text": "PRO PLAN", "size": "xs", "color": "#06B6D4", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": "組長保險・升級方案",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md",
                    "margin": "xs"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "16px",
            "spacing": "md",
            "backgroundColor": "#100B1E",
            "contents": [
                # 方案 1：基礎免費版
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E1636",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#4C1D95",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "alignItems": "center",
                            "contents": [
                                {"type": "text", "text": "基礎免費版", "weight": "bold", "size": "sm", "color": "#FFFFFF", "flex": 1},
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "backgroundColor": "#2D224D",
                                    "paddingVertical": "2px",
                                    "paddingHorizontal": "6px",
                                    "cornerRadius": "4px",
                                    "contents": [
                                        {"type": "text", "text": "使用中", "size": "xxs", "color": "#06B6D4", "weight": "bold"}
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "• 基礎任務建立與自訂項目\n• 溫和版超時提醒通知\n• 🎲 基礎隨機抽籤分配\n• 單一群組上限 1 個專案",
                            "size": "xs",
                            "color": "#F3E8FF",
                            "margin": "sm",
                            "wrap": True
                        }
                    ]
                },
                # 方案 2：專案保險單次包 (PRO)
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#2A0845",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#FDE047",
                    "borderWidth": "2px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "alignItems": "center",
                            "contents": [
                                {"type": "text", "text": "保險單次包", "weight": "bold", "size": "sm", "color": "#FDE047", "flex": 1},
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "backgroundColor": "#E11D48",
                                    "paddingVertical": "2px",
                                    "paddingHorizontal": "6px",
                                    "cornerRadius": "4px",
                                    "contents": [
                                        {"type": "text", "text": "NT$ 49 / 專案", "size": "xxs", "color": "#FFFFFF", "weight": "bold"}
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "• 僅限單一專案群組使用（有效 120 天）\n• 匯出完整《小組貢獻度分析 PDF 報告》\n• 30 分鐘沉寂偵測與自動標註催繳\n• 🎲 命運抽籤（超時未認領自動強制指派）\n• LIFF 任務點擊查閱時間戳記紀錄（已讀精準追蹤）",
                            "size": "xs",
                            "color": "#FFFFFF",
                            "margin": "sm",
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "backgroundColor": "#06C755",
                            "cornerRadius": "6px",
                            "paddingVertical": "8px",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "margin": "md",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "LINE Pay 立即升級 NT$ 49",
                                    "size": "xs",
                                    "color": "#FFFFFF",
                                    "weight": "bold"
                                }
                            ]
                        }
                    ]
                },
                # 方案 3：全學期組長躺平 Pass
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E1636",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#0891B2",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "alignItems": "center",
                            "contents": [
                                {"type": "text", "text": "組長躺平pass", "weight": "bold", "size": "sm", "color": "#38BDF8", "flex": 1},
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "backgroundColor": "#0C4A6E",
                                    "paddingVertical": "2px",
                                    "paddingHorizontal": "6px",
                                    "cornerRadius": "4px",
                                    "contents": [
                                        {"type": "text", "text": "NT$ 99 / 學期", "size": "xxs", "color": "#38BDF8", "weight": "bold"}
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "• 可4個群組使用（有效 180 天）\n• 一個便當錢，全學期多群組無限暢用\n• 解鎖「毒舌嘴替／嚴格教授」AI 人格包\n• 適合修多門專案課、同時身兼多組組長的同學",
                            "size": "xs",
                            "color": "#F3E8FF",
                            "margin": "sm",
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "backgroundColor": "#06C755",
                            "cornerRadius": "6px",
                            "paddingVertical": "8px",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "margin": "md",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "LINE Pay 立即升級 NT$ 99",
                                    "size": "xs",
                                    "color": "#FFFFFF",
                                    "weight": "bold"
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "10px",
            "backgroundColor": "#160F29",
            "contents": [
                {
                    "type": "text",
                    "text": "LINE Pay 線上支付建置中，暫未開放點擊付費",
                    "size": "xxs",
                    "color": "#94A3B8",
                    "align": "center"
                }
            ]
        }
    }
    return FlexMessage(
        alt_text="組長保險・升級方案",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )
