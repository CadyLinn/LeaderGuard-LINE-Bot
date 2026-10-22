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
        QuickReplyItem(action=MessageAction(label="隨機分配", text="/抽籤")),
        QuickReplyItem(action=MessageAction(label="開始會議", text="/開始會議")),
        QuickReplyItem(action=MessageAction(label="結束會議", text="/結束會議")),
        QuickReplyItem(action=MessageAction(label="方案說明", text="/升級方案")),
        QuickReplyItem(action=MessageAction(label="常用指令", text="/常用指令說明")),
    ])

def create_preset_tasks_carousel() -> FlexMessage:
    """常見小組專案工作範本輪播卡片（學院守護者風格 (Academy Tech Guardian)，遵循 Apple HIG 高對比按鈕）"""
    carousel_contents = [
        # 卡片 1：簡報製作
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#0F172A",
                "paddingAll": "16px",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                           
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
                "backgroundColor": "#1E293B",
                "borderColor": "#38BDF8",
                "borderWidth": "1px",
                "contents": [
                    {"type": "text", "text": "核心職責：", "weight": "bold", "size": "xs", "color": "#FBBF24"},
                    {"type": "text", "text": "• 統整組員文字與圖表\n• PPT / Canva 視覺專業美化\n• 彙整報告講稿備忘錄", "size": "xs", "color": "#E2E8F0", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#0F172A",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 簡報製作與美化 負責PPT視覺美編與排版"
                        },
                        "style": "primary",
                        "color": "#0284C7",
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
                "backgroundColor": "#0F172A",
                "paddingAll": "16px",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          
                            {"type": "text", "text": "FOCUS", "size": "xxs", "color": "#FBBF24", "align": "end", "weight": "bold"}
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
                "backgroundColor": "#1E293B",
                "borderColor": "#F43F5E",
                "borderWidth": "1px",
                "contents": [
                    {"type": "text", "text": "核心職責：", "weight": "bold", "size": "xs", "color": "#FBBF24"},
                    {"type": "text", "text": "• 掌握專案全脈絡\n• 代表小組自信發表\n• 現場教授提問沉著應對", "size": "xs", "color": "#E2E8F0", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#0F172A",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 上台口頭報告 負責掌握專案脈絡並代表口頭發表"
                        },
                        "style": "primary",
                        "color": "#0284C7",
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
                "backgroundColor": "#0F172A",
                "paddingAll": "16px",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          
                            {"type": "text", "text": "KEY", "size": "xxs", "color": "#38BDF8", "align": "end", "weight": "bold"}
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
                "backgroundColor": "#1E293B",
                "borderColor": "#38BDF8",
                "borderWidth": "1px",
                "contents": [
                    {"type": "text", "text": "核心職責：", "weight": "bold", "size": "xs", "color": "#FBBF24"},
                    {"type": "text", "text": "• 前期專案主題地毯式調研\n• 相關文獻與真實案例查證\n• 數據統整與來源佐證", "size": "xs", "color": "#E2E8F0", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#0F172A",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 文獻查證與資料蒐集 負責前期調研、文獻查證與數據整理"
                        },
                        "style": "primary",
                        "color": "#0284C7",
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
                "backgroundColor": "#0F172A",
                "paddingAll": "16px",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        
                            {"type": "text", "text": "CORE", "size": "xxs", "color": "#FBBF24", "align": "end", "weight": "bold"}
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
                "backgroundColor": "#1E293B",
                "borderColor": "#F43F5E",
                "borderWidth": "1px",
                "contents": [
                    {"type": "text", "text": "核心職責：", "weight": "bold", "size": "xs", "color": "#FBBF24"},
                    {"type": "text", "text": "• 彙整各章節文字與圖表\n• 校對格式排版與文獻引用\n• 產出完整清晰期末正式報告", "size": "xs", "color": "#E2E8F0", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#0F172A",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 書面報告撰寫統整 負責期末書面Word/PDF格式與內容校對"
                        },
                        "style": "primary",
                        "color": "#0284C7",
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
                "backgroundColor": "#1E293B",
                "borderColor": "#FBBF24",
                "borderWidth": "2px",
                "paddingAll": "16px",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {"type": "text", "text": "【快捷建立】", "size": "xxs", "color": "#FBBF24", "weight": "bold"},
                            {"type": "text", "text": "ALL IN ONE", "size": "xxs", "color": "#38BDF8", "align": "end", "weight": "bold"}
                        ]
                    },
                    {"type": "text", "text": "一鍵建立常見分工", "weight": "bold", "color": "#FBBF24", "size": "md", "margin": "xs"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#1E293B",
                "contents": [
                    {"type": "text", "text": "小組分工快速初始化", "weight": "bold", "size": "sm", "color": "#38BDF8"},
                    {"type": "text", "text": "一次建立 4 大標準工作項目（簡報、口頭、調研、書面），分工權責明確清楚。", "size": "xs", "color": "#E2E8F0", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#0F172A",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "一鍵建立常見分工",
                            "text": "/task 批次建立"
                        },
                        "style": "primary",
                        "color": "#0284C7",
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
                "backgroundColor": "#0F172A",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "自訂小組工作項目", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#1E293B",
                "borderColor": "#38BDF8",
                "borderWidth": "1px",
                "contents": [
                    {"type": "text", "text": "自訂專案工作", "weight": "bold", "size": "sm", "color": "#FBBF24"},
                    {"type": "text", "text": "點擊下方按鈕，對話框將自動帶入指令，即可自訂工作名稱與說明。", "size": "xs", "color": "#E2E8F0", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#0F172A",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "postback",
                            "label": "自訂新增工作",
                            "data": "action=prompt_custom_task",
                            "inputOption": "openKeyboard",
                            "fillInText": "/任務 新增 "
                        },
                        "style": "primary",
                        "color": "#0284C7",
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
        alt_text="小組專案常用分工範本",
        contents=FlexContainer.from_dict(carousel),
        quick_reply=get_main_quick_reply()
    )

def create_main_menu_flex() -> FlexMessage:
    """小組功能主選單卡片（簡潔現代風：高對比、鮮明按鈕、學院守護者專屬圖鑑）"""
    bubble = {
        "type": "bubble",
        "size": "giga",
        "hero": {
            "type": "image",
            "url": f"{BASE_URL}/assets/hero_menu_guardian.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
                "type": "message",
                "text": "/選單"
            }
        },
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "20px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "PRO 專業版", "weight": "bold", "color": "#38BDF8", "size": "xs", "align": "end"}
                    ]
                },
                {
                    "type": "text",
                    "text": "小組專案管理・功能選單",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "lg",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "小組任務分工與進度追蹤，即時掌握團隊協作成效。",
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
            "backgroundColor": "#0B132B",
            "paddingAll": "16px",
            "contents": [
                # 區塊 1：專案工作分工
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E293B",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#38BDF8",
                    "borderWidth": "1.5px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "工作分工管理",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#38BDF8"
                        },
                        {
                            "type": "text",
                            "text": "建立專案分工範本，記錄每位成員責任",
                            "size": "xs",
                            "color": "#E2E8F0",
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
                                    "color": "#0284C7",
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
                                    "color": "#0284C7",
                                    "height": "sm"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "sm",
                            "margin": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "postback",
                                        "label": "自訂工作",
                                        "data": "action=prompt_custom_task",
                                        "inputOption": "openKeyboard",
                                        "fillInText": "/任務 新增 "
                                    },
                                    "style": "primary",
                                    "color": "#0284C7",
                                    "height": "sm",
                                    "flex": 1
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "刪除工作",
                                        "text": "/task 刪除"
                                    },
                                    "style": "primary",
                                    "color": "#475569",
                                    "height": "sm",
                                    "flex": 1
                                }
                            ]
                        }
                    ]
                },
                # 區塊 2：隨機分配指派
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E293B",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#38BDF8",
                    "borderWidth": "1.5px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "隨機分配指派",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#38BDF8"
                        },
                        {
                            "type": "text",
                            "text": "未認領工作系統隨機指派，或登記小組名冊",
                            "size": "xs",
                            "color": "#E2E8F0",
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
                                        "label": "隨機分配",
                                        "text": "/抽籤"
                                    },
                                    "style": "primary",
                                    "color": "#0284C7",
                                    "height": "sm",
                                    "flex": 1
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "postback",
                                        "label": "登記組員",
                                        "data": "action=prompt_set_members",
                                        "inputOption": "openKeyboard",
                                        "fillInText": "/組員 "
                                    },
                                    "style": "primary",
                                    "color": "#0284C7",
                                    "height": "sm",
                                    "flex": 1
                                }
                            ]
                        }
                    ]
                },
                # 區塊 3：進度追蹤與期末結算
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E293B",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#FBBF24",
                    "borderWidth": "1.5px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "進度追蹤與存證",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#FBBF24"
                        },
                        {
                            "type": "text",
                            "text": "掌握小組分工進度，隨時產出完整存證報告",
                            "size": "xs",
                            "color": "#E2E8F0",
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
                                    "color": "#0284C7",
                                    "height": "sm"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "存證報告",
                                        "text": "/export"
                                    },
                                    "style": "primary",
                                    "color": "#6366F1",
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
                            "style": "primary",
                            "color": "#334155",
                            "height": "sm",
                            "margin": "sm"
                        }
                    ]
                },
                # 區塊 4：PRO 專業會議記錄統整
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E293B",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#38BDF8",
                    "borderWidth": "2px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "alignItems": "center",
                            "contents": [
                                {"type": "text", "text": "PRO 會議記錄統整", "weight": "bold", "size": "sm", "color": "#38BDF8", "flex": 1},
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "backgroundColor": "#0284C7",
                                    "paddingVertical": "2px",
                                    "paddingHorizontal": "6px",
                                    "cornerRadius": "4px",
                                    "contents": [
                                        {"type": "text", "text": "已開通", "size": "xxs", "color": "#FFFFFF", "weight": "bold"}
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "群組討論自動記錄，由 AI 提煉會議摘要與待辦工作。",
                            "size": "xs",
                            "color": "#E2E8F0",
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
                                        "label": "開始會議",
                                        "text": "/開始會議"
                                    },
                                    "style": "primary",
                                    "color": "#0284C7",
                                    "height": "sm",
                                    "flex": 1
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "結束會議",
                                        "text": "/結束會議"
                                    },
                                    "style": "primary",
                                    "color": "#D97706",
                                    "height": "sm",
                                    "flex": 1
                                }
                            ]
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "方案說明",
                                "text": "/升級方案"
                            },
                            "style": "primary",
                            "color": "#334155",
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
    """操作指南 Flex 卡片（學院守護者風格表格化速查表，清晰易讀）"""
    table_data = [
        ("挑選範本", "/任務 範本", "/task"),
        ("查看工作", "/任務 清單", "/tasks"),
        ("認領工作", "/認領 [編號]", "/claim"),
        ("自訂任務", "/任務 新增", "/task add"),
        ("開始會議", "/開始會議", "/start_meeting"),
        ("結束會議", "/結束會議", "/end_meeting"),
        ("隨機分配", "/抽籤 或 /抽籤 名單", "/roulette"),
        ("登記組員", "/組員 姓名1 姓名2", "/member"),
        ("專案進度", "/狀態", "/status"),
        ("解鎖專業", "/解鎖會議", "/upgrade")
    ]

    rows = []
    for idx, (func, cn, en) in enumerate(table_data):
        bg_color = "#1E293B" if idx % 2 == 0 else "#0F172A"
        rows.append({
            "type": "box",
            "layout": "horizontal",
            "backgroundColor": bg_color,
            "paddingVertical": "8px",
            "paddingHorizontal": "10px",
            "alignItems": "center",
            "contents": [
                {"type": "text", "text": func, "size": "xs", "weight": "bold", "color": "#FFFFFF", "flex": 3, "wrap": True},
                {"type": "text", "text": cn, "size": "xs", "weight": "bold", "color": "#38BDF8", "flex": 4, "wrap": True},
                {"type": "text", "text": en, "size": "xs", "color": "#FBBF24", "flex": 3, "wrap": True}
            ]
        })

    bubble = {
        "type": "bubble",
        "size": "giga",
        "hero": {
            "type": "image",
            "url": f"{BASE_URL}/assets/hero_command_guardian.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
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
                    "color": "#38BDF8",
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
            "backgroundColor": "#0B132B",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "backgroundColor": "#1E293B",
                    "borderColor": "#FBBF24",
                    "borderWidth": "1px",
                    "paddingVertical": "8px",
                    "paddingHorizontal": "10px",
                    "cornerRadius": "4px",
                    "contents": [
                        {"type": "text", "text": "發動行動", "weight": "bold", "size": "xs", "color": "#FBBF24", "flex": 3},
                        {"type": "text", "text": "中文指令", "weight": "bold", "size": "xs", "color": "#38BDF8", "flex": 4},
                        {"type": "text", "text": "英文指令", "weight": "bold", "size": "xs", "color": "#E2E8F0", "flex": 3}
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
                    "backgroundColor": "#1E293B",
                    "borderColor": "#38BDF8",
                    "borderWidth": "1px",
                    "cornerRadius": "6px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "• 認領示範：/認領 T001（或 /claim T001）\n• 登記組員：/成員 新增 小明 小華\n• 分配機制：系統將優先自尚未認領工作之成員中隨機指派",
                            "size": "xxs",
                            "color": "#E2E8F0",
                            "wrap": True
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "paddingAll": "12px",
            "backgroundColor": "#0F172A",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "立即把組長保險加入群組",
                        "text": "/如何加入群組"
                    },
                    "style": "primary",
                    "color": "#0284C7",
                    "height": "sm"
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
                    "style": "primary",
                    "color": "#D97706",
                    "height": "sm"
                }
            ]
        }
    }

    invite_bubble = create_invite_group_bubble()

    carousel = {
        "type": "carousel",
        "contents": [bubble, invite_bubble]
    }

    return FlexMessage(
        alt_text="組長保險・常用指令說明與加入群組指南",
        contents=FlexContainer.from_dict(carousel),
        quick_reply=get_main_quick_reply()
    )

def create_invite_group_bubble() -> dict:
    """立即把組長保險加入群組 Bubble 卡片字典（科技學院學院風，步驟附精美圖解、色彩鮮明）"""
    return {
        "type": "bubble",
        "size": "giga",
        "hero": {
            "type": "image",
            "url": f"{BASE_URL}/assets/hero_invite_guardian.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
                "type": "message",
                "text": "/如何加入群組"
            }
        },
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "INVITE GUIDE", "size": "xs", "color": "#38BDF8", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": "立即把組長保險加入群組",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "進駐小組專案聊天室，全體裝置連線・杜絕擺爛！",
                    "color": "#38BDF8",
                    "size": "xs",
                    "margin": "xs",
                    "wrap": True
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "14px",
            "backgroundColor": "#0B132B",
            "spacing": "md",
            "contents": [
                # 步驟 1
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
                    "alignItems": "center",
                    "backgroundColor": "#162032",
                    "borderColor": "#0284C7",
                    "borderWidth": "1px",
                    "paddingAll": "10px",
                    "cornerRadius": "8px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "width": "26px",
                            "height": "26px",
                            "cornerRadius": "13px",
                            "backgroundColor": "#0284C7",
                            "justifyContent": "center",
                            "alignItems": "center",
                            "contents": [
                                {"type": "text", "text": "1", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center"}
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 1,
                            "contents": [
                                {"type": "text", "text": "開啟專案小組聊天室", "size": "sm", "weight": "bold", "color": "#FFFFFF"},
                                {"type": "text", "text": "進入您的大學報告或專案分工群組", "size": "xxs", "color": "#94A3B8", "margin": "xs"}
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "width": "50px",
                            "height": "50px",
                            "cornerRadius": "8px",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": f"{BASE_URL}/assets/step1_group.jpg",
                                    "size": "full",
                                    "aspectRatio": "1:1",
                                    "aspectMode": "cover"
                                }
                            ]
                        }
                    ]
                },
                # 步驟 2
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
                    "alignItems": "center",
                    "backgroundColor": "#162032",
                    "borderColor": "#D97706",
                    "borderWidth": "1px",
                    "paddingAll": "10px",
                    "cornerRadius": "8px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "width": "26px",
                            "height": "26px",
                            "cornerRadius": "13px",
                            "backgroundColor": "#D97706",
                            "justifyContent": "center",
                            "alignItems": "center",
                            "contents": [
                                {"type": "text", "text": "2", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center"}
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 1,
                            "contents": [
                                {"type": "text", "text": "點選右上角選單（≡）>「邀請」", "size": "sm", "weight": "bold", "color": "#FFFFFF"},
                                {"type": "text", "text": "進入群組設定功能頁，點擊「邀請」圖示", "size": "xxs", "color": "#94A3B8", "margin": "xs"}
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "width": "50px",
                            "height": "50px",
                            "cornerRadius": "8px",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": f"{BASE_URL}/assets/step2_invite.jpg",
                                    "size": "full",
                                    "aspectRatio": "1:1",
                                    "aspectMode": "cover"
                                }
                            ]
                        }
                    ]
                },
                # 步驟 3
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
                    "alignItems": "center",
                    "backgroundColor": "#162032",
                    "borderColor": "#38BDF8",
                    "borderWidth": "1px",
                    "paddingAll": "10px",
                    "cornerRadius": "8px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "width": "26px",
                            "height": "26px",
                            "cornerRadius": "13px",
                            "backgroundColor": "#38BDF8",
                            "justifyContent": "center",
                            "alignItems": "center",
                            "contents": [
                                {"type": "text", "text": "3", "size": "xs", "weight": "bold", "color": "#0B132B", "align": "center"}
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 1,
                            "contents": [
                                {"type": "text", "text": "搜尋「組長保險」並勾選加入", "size": "sm", "weight": "bold", "color": "#FFFFFF"},
                                {"type": "text", "text": "勾選機器人並點擊邀請，立即進駐群組！", "size": "xxs", "color": "#94A3B8", "margin": "xs"}
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "width": "50px",
                            "height": "50px",
                            "cornerRadius": "8px",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": f"{BASE_URL}/assets/step3_bot.jpg",
                                    "size": "full",
                                    "aspectRatio": "1:1",
                                    "aspectMode": "cover"
                                }
                            ]
                        }
                    ]
                },
                # 底部小提醒（簡潔清爽）
                {
                    "type": "box",
                    "layout": "vertical",
                    "paddingAll": "10px",
                    "backgroundColor": "#0F172A",
                    "borderColor": "#1E293B",
                    "borderWidth": "1px",
                    "cornerRadius": "6px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "• 推薦分享：點擊下方「一鍵推薦給朋友」直接挑選好友或群組\n• 啟用指令：進群後輸入「/選單」即可開始小組協作管理\n• 常用指令說明：點擊下方「常用指令手冊」查看完整說明",
                            "size": "xxs",
                            "color": "#94A3B8",
                            "wrap": True
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "paddingAll": "12px",
            "backgroundColor": "#0F172A",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "一鍵推薦給朋友／邀請入群",
                        "uri": "https://line.me/R/nv/recommendOA/@805yffpw"
                    },
                    "style": "primary",
                    "color": "#0284C7",
                    "height": "sm"
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "常用指令說明・速查手冊",
                        "text": "/常用指令說明"
                    },
                    "style": "primary",
                    "color": "#D97706",
                    "height": "sm"
                }
            ]
        }
    }

def create_invite_group_flex() -> FlexMessage:
    """立即把組長保險加入群組 Flex 獨立卡片"""
    return FlexMessage(
        alt_text="立即把組長保險加入群組教學",
        contents=FlexContainer.from_dict(create_invite_group_bubble()),
        quick_reply=get_main_quick_reply()
    )

def create_task_created_flex(task_id: str, title: str, description: str, creator_name: str) -> FlexMessage:
    """任務建立成功通知卡片（學院守護者登場風格，指派圖像存證）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "hero": {
            "type": "image",
            "url": f"{BASE_URL}/assets/hero_task_assigned_v2026.jpg",
            "size": "full",
            "aspectRatio": "16:9",
            "aspectMode": "cover",
            "backgroundColor": "#0B132B",
            "action": {
                "type": "message",
                "text": "/task 清單"
            }
        },
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      
                        {"type": "text", "text": "NEW", "size": "xs", "color": "#FBBF24", "align": "end", "weight": "bold"}
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
            "backgroundColor": "#1E293B",
            "contents": [
                {
                    "type": "text",
                    "text": f"【{task_id}】{title}",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FBBF24",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": description if description else "（無補充說明）",
                    "size": "xs",
                    "color": "#E2E8F0",
                    "wrap": True
                },
                {"type": "separator", "color": "#0284C7"},
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "任務發起人", "size": "xs", "color": "#38BDF8"},
                        {"type": "text", "text": creator_name, "size": "xs", "color": "#FFFFFF", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "當前狀態", "size": "xs", "color": "#38BDF8"},
                        {"type": "text", "text": "待認領（尚未認領）", "size": "xs", "color": "#F43F5E", "align": "end", "weight": "bold"}
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "backgroundColor": "#0F172A",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "我來負責！認領此任務",
                        "text": f"/claim {task_id}"
                    },
                    "style": "primary",
                    "color": "#0284C7",
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
    """任務清單卡片（學院守護者風格，按鈕鮮明高對比）"""
    if not tasks:
        item_boxes = [{
            "type": "text",
            "text": "目前沒有任何待辦任務！小組全員安全進入休假領域！",
            "size": "sm",
            "color": "#38BDF8",
            "align": "center",
            "margin": "lg"
        }]
        footer_box = {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "paddingAll": "12px",
            "backgroundColor": "#0F172A",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "自訂新增工作",
                        "data": "action=prompt_custom_task",
                        "inputOption": "openKeyboard",
                        "fillInText": "/任務 新增 "
                    },
                    "style": "primary",
                    "color": "#D97706",
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
                    "color": "#0284C7",
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
                    "backgroundColor": "#1E293B",
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
                            "color": "#0284C7",
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
                    "backgroundColor": "#0F172A",
                    "borderColor": "#0284C7",
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
                                    "color": "#E2E8F0",
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
                                    "text": f"{assignee_name}",
                                    "size": "xs",
                                    "color": "#38BDF8",
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
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "postback",
                            "label": "自訂新增工作",
                            "data": "action=prompt_custom_task",
                            "inputOption": "openKeyboard",
                            "fillInText": "/任務 新增 "
                        },
                        "style": "primary",
                        "color": "#0284C7",
                        "height": "sm",
                        "flex": 1
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "刪除工作",
                            "text": "/task 刪除"
                        },
                        "style": "primary",
                        "color": "#475569",
                        "height": "sm",
                        "flex": 1
                    }
                ]
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "常用分工範本",
                    "text": "/task 範本"
                },
                "style": "primary",
                "color": "#0284C7",
                "height": "sm"
            }
        ]
        if has_pending:
            footer_buttons.insert(0, {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "隨機分配未認領工作",
                    "text": "/抽籤"
                },
                "style": "primary",
                "color": "#D97706",
                "height": "sm",
                "margin": "sm"
            })
            
        footer_box = {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "paddingAll": "12px",
            "backgroundColor": "#0F172A",
            "contents": footer_buttons
        }

    bubble = {
        "type": "bubble",
        "size": "giga",
        "hero": {
            "type": "image",
            "url": f"{BASE_URL}/assets/hero_tasklist_guardian.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
                "type": "message",
                "text": "/task 清單"
            }
        },
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "STATUS", "size": "xs", "color": "#38BDF8", "align": "end", "weight": "bold"}
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
                    "color": "#FBBF24",
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
            "backgroundColor": "#0B132B",
            "contents": item_boxes
        },
        "footer": footer_box
    }
    return FlexMessage(
        alt_text="小組專案任務清單",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_task_delete_flex(tasks: list) -> FlexMessage:
    """工作刪除管理卡片（列出所有工作，點選紅色刪除按鈕即可刪除該項目）"""
    if not tasks:
        bubble = {
            "type": "bubble",
            "size": "giga",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#0F172A",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "【小組工作管理】", "size": "xs", "color": "#F43F5E", "weight": "bold"},
                    {"type": "text", "text": "目前沒有任何工作可刪除", "weight": "bold", "color": "#FFFFFF", "size": "md", "margin": "xs"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "16px",
                "backgroundColor": "#0B132B",
                "contents": [
                    {"type": "text", "text": "目前小組清單中尚無任何專案工作。", "size": "sm", "color": "#94A3B8", "align": "center"}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#0F172A",
                "contents": [
                    {
                        "type": "button",
                        "action": {"type": "message", "label": "返回任務清單", "text": "/task 清單"},
                        "style": "primary",
                        "color": "#0284C7",
                        "height": "sm"
                    }
                ]
            }
        }
        return FlexMessage(
            alt_text="小組工作管理・刪除工作",
            contents=FlexContainer.from_dict(bubble),
            quick_reply=get_main_quick_reply()
        )

    item_boxes = []
    for t in tasks[:10]:
        task_id = t.get("id", "T000")
        title = t.get("title", "")
        is_pending = (t.get("status") == "pending")
        status_text = "尚未認領" if is_pending else f"負責人：{t.get('assignee_name', '組員')}"
        status_color = "#F43F5E" if is_pending else "#38BDF8"

        item_boxes.append({
            "type": "box",
            "layout": "horizontal",
            "margin": "md",
            "alignItems": "center",
            "backgroundColor": "#1E293B",
            "borderColor": "#0284C7",
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
                            "weight": "bold",
                            "color": "#FFFFFF",
                            "wrap": True
                        },
                        {
                            "type": "text",
                            "text": status_text,
                            "size": "xxs",
                            "color": status_color,
                            "weight": "bold",
                            "margin": "xs"
                        }
                    ]
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "刪除",
                        "text": f"/task 刪除 {task_id}"
                    },
                    "style": "primary",
                    "color": "#DC2626",
                    "height": "sm",
                    "flex": 3
                }
            ]
        })

    bubble = {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "【小組工作管理】", "size": "xs", "color": "#F43F5E", "weight": "bold"},
                        {"type": "text", "text": f"共 {len(tasks)} 項", "size": "xs", "color": "#38BDF8", "align": "end", "weight": "bold"}
                    ]
                },
                {"type": "text", "text": "點選「刪除」即可移除工作", "weight": "bold", "color": "#FFFFFF", "size": "md", "margin": "xs"}
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "xs",
            "paddingAll": "12px",
            "backgroundColor": "#0B132B",
            "contents": item_boxes
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "backgroundColor": "#0F172A",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "返回任務清單",
                        "text": "/task 清單"
                    },
                    "style": "primary",
                    "color": "#0284C7",
                    "height": "sm"
                }
            ]
        }
    }

    return FlexMessage(
        alt_text="小組工作管理・刪除工作",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_roulette_flex(task_id: str, task_title: str, victim_name: str) -> FlexMessage:
    """隨機抽籤結果卡片（專業簡潔風格）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#1E293B",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "TASK ASSIGNMENT", "size": "xs", "color": "#38BDF8", "align": "end", "weight": "bold"}
                    ]
                },
                {"type": "text", "text": "系統隨機指派結果", "weight": "bold", "color": "#FFFFFF", "size": "md", "align": "center", "margin": "xs"}
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "paddingAll": "16px",
            "backgroundColor": "#0B132B",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E293B",
                    "borderColor": "#38BDF8",
                    "borderWidth": "2px",
                    "cornerRadius": "8px",
                    "paddingAll": "16px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "本次指派負責成員：",
                            "size": "xs",
                            "color": "#94A3B8",
                            "align": "center"
                        },
                        {
                            "type": "text",
                            "text": victim_name,
                            "weight": "bold",
                            "size": "xl",
                            "color": "#FBBF24",
                            "align": "center",
                            "wrap": True,
                            "margin": "sm"
                        },
                        {"type": "separator", "color": "#0284C7", "margin": "md"},
                        {
                            "type": "text",
                            "text": f"負責項目：【{task_id}】{task_title}",
                            "size": "sm",
                            "color": "#FFFFFF",
                            "wrap": True,
                            "weight": "bold",
                            "margin": "md",
                            "align": "center"
                        },
                        {
                            "type": "text",
                            "text": "系統已記錄指派資訊，請確認工作內容並推進進度。",
                            "size": "xs",
                            "color": "#38BDF8",
                            "align": "center",
                            "margin": "sm",
                            "wrap": True
                        }
                    ]
                }
            ]
        }
    }
    return FlexMessage(
        alt_text=f"隨機分配結果：由 {victim_name} 負責 {task_title}",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_welcome_guide_flex() -> FlexMessage:
    """加入好友時發送的 4 步驟使用手冊 Flex 卡片（學院守護者風格 (Academy Tech Guardian)）"""
    manual_url = os.getenv("MANUAL_URL", "")
    group_invite_url = os.getenv("GROUP_INVITE_URL", "https://line.me/R/nv/recommendOA/@805yffpw")

    manual_action = (
        {"type": "uri", "label": "查看完整操作說明", "uri": manual_url}
        if manual_url
        else {"type": "message", "label": "查看完整操作說明", "text": "/常用指令說明"}
    )

    bubble = {
        "type": "bubble",
        "size": "mega",
        "hero": {
            "type": "image",
            "url": f"{BASE_URL}/assets/hero_guide_guardian.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "20px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    
                        {"type": "text", "text": "START", "size": "xs", "weight": "bold", "color": "#38BDF8", "align": "end"}
                    ]
                },
                {
                    "type": "text",
                    "text": "4 步驟快速上手指南",
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
            "backgroundColor": "#0B132B",
            "paddingAll": "20px",
            "spacing": "md",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E293B",
                    "cornerRadius": "10px",
                    "borderColor": "#38BDF8",
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
                            "action": {
                                "type": "message",
                                "text": "/如何加入群組"
                            },
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "width": "26px",
                                    "height": "26px",
                                    "cornerRadius": "13px",
                                    "backgroundColor": "#FBBF24",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                    "contents": [
                                        { "type": "text", "text": "1", "size": "xs", "weight": "bold", "color": "#0F172A", "align": "center" }
                                    ]
                                },
                                {
                                    "type": "text",
                                    "text": "把我加進「群組」",
                                    "size": "sm",
                                    "color": "#FFFFFF",
                                    "weight": "bold",
                                    "flex": 1
                                }
                            ]
                        },
                        { "type": "separator", "color": "#334155" },
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
                                    "backgroundColor": "#0284C7",
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
                                    "color": "#38BDF8",
                                    "weight": "bold",
                                    "flex": 1
                                }
                            ]
                        },
                        { "type": "separator", "color": "#334155" },
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
                                            "text": "閒置30分鐘自動提醒",
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
                        { "type": "separator", "color": "#334155" },
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
                                    "backgroundColor": "#38BDF8",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                    "contents": [
                                        { "type": "text", "text": "4", "size": "xs", "weight": "bold", "color": "#0F172A", "align": "center" }
                                    ]
                                },
                                {
                                    "type": "text",
                                    "text": "輸入 /export 匯出成果存證",
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
            "spacing": "sm",
            "paddingAll": "12px",
            "backgroundColor": "#0F172A",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "color": "#0284C7",
                    "action": {
                        "type": "message",
                        "label": "常用指令說明",
                        "text": "/常用指令說明"
                    }
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "color": "#D97706",
                    "action": {
                        "type": "message",
                        "label": "查看方案說明",
                        "text": "/升級方案"
                    }
                }
            ],
            "flex": 0
        }
    }

    return FlexMessage(
        alt_text="組長保險 LeaderGuard - 4 步驟上手指南",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_upgrade_plan_flex() -> FlexMessage:
    """升級方案卡片（簡約現代、聚焦會議記錄統整與解鎖）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "LEADERGUARD", "size": "xs", "color": "#38BDF8", "weight": "bold"},
                        {"type": "text", "text": "PRO 專業版", "size": "xs", "color": "#94A3B8", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": "PRO 會議記錄方案",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "自動記錄群組討論，AI 統整會議重點與待辦清單",
                    "size": "xs",
                    "color": "#94A3B8",
                    "margin": "xs",
                    "wrap": True
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "16px",
            "spacing": "md",
            "backgroundColor": "#0B132B",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E293B",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#38BDF8",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "alignItems": "center",
                            "contents": [
                                {"type": "text", "text": "PRO 會議統整核心功能", "weight": "bold", "size": "sm", "color": "#38BDF8", "flex": 1},
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "backgroundColor": "#059669",
                                    "paddingVertical": "2px",
                                    "paddingHorizontal": "6px",
                                    "cornerRadius": "4px",
                                    "contents": [
                                        {"type": "text", "text": "即將開放", "size": "xxs", "color": "#FFFFFF", "weight": "bold"}
                                    ]
                                }
                            ]
                        },
                        {"type": "separator", "color": "#334155", "margin": "sm"},
                        {
                            "type": "text",
                            "text": "• 輸入 /開始會議 自動記錄群組討論發言\n• 輸入 /結束會議 AI 提煉重點與待辦清單\n• 小組分工與期末成果存證報告（/export）\n• 支援多專案與多群組管理",
                            "size": "xs",
                            "color": "#FFFFFF",
                            "margin": "sm",
                            "wrap": True
                        },
                        {"type": "separator", "color": "#334155", "margin": "sm"},
                        {
                            "type": "text",
                            "text": "PRO 方案目前尚未開放申請，敬請期待。",
                            "size": "xs",
                            "color": "#94A3B8",
                            "margin": "sm",
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
            "backgroundColor": "#0F172A",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "付款解鎖會議記錄功能",
                        "text": "/解鎖會議"
                    },
                    "style": "primary",
                    "color": "#0284C7",
                    "height": "sm"
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "前往專案選單",
                        "text": "/選單"
                    },
                    "style": "primary",
                    "color": "#334155",
                    "height": "sm"
                }
            ]
        }
    }
    return FlexMessage(
        alt_text="組長保險・方案說明",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_upgrade_success_flex() -> FlexMessage:
    """PRO 專業版啟用與快捷操作卡片（簡約洗鍊、聚焦會議記錄功能）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "LEADERGUARD PRO", "size": "xs", "color": "#38BDF8", "weight": "bold"},
                        {"type": "text", "text": "已解鎖", "size": "xs", "color": "#10B981", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": "PRO 會議記錄功能已解鎖",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "已開通群組對話記錄與 AI 智能統整權限，可直接點擊操作：",
                    "size": "xs",
                    "color": "#94A3B8",
                    "margin": "xs",
                    "wrap": True
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "16px",
            "spacing": "sm",
            "backgroundColor": "#0B132B",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E293B",
                    "paddingAll": "12px",
                    "cornerRadius": "8px",
                    "borderColor": "#38BDF8",
                    "borderWidth": "1px",
                    "contents": [
                        # 項目 1：開始會議
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "alignItems": "center",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "flex": 7,
                                    "contents": [
                                        {"type": "text", "text": "開始會議記錄", "weight": "bold", "size": "sm", "color": "#FFFFFF"},
                                        {"type": "text", "text": "啟動群組發言自動記錄", "size": "xs", "color": "#94A3B8", "margin": "xs", "wrap": True}
                                    ]
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "開始",
                                        "text": "/開始會議"
                                    },
                                    "style": "primary",
                                    "color": "#0284C7",
                                    "height": "sm",
                                    "flex": 3
                                }
                            ]
                        },
                        {"type": "separator", "color": "#334155", "margin": "md"},
                        # 項目 2：結束會議
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "alignItems": "center",
                            "margin": "md",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "flex": 7,
                                    "contents": [
                                        {"type": "text", "text": "結束會議統整", "weight": "bold", "size": "sm", "color": "#FFFFFF"},
                                        {"type": "text", "text": "AI 提煉重點與待辦清單", "size": "xs", "color": "#94A3B8", "margin": "xs", "wrap": True}
                                    ]
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "結束",
                                        "text": "/結束會議"
                                    },
                                    "style": "primary",
                                    "color": "#D97706",
                                    "height": "sm",
                                    "flex": 3
                                }
                            ]
                        },
                        {"type": "separator", "color": "#334155", "margin": "md"},
                        # 項目 3：成果存證
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "alignItems": "center",
                            "margin": "md",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "flex": 7,
                                    "contents": [
                                        {"type": "text", "text": "成果存證報告", "weight": "bold", "size": "sm", "color": "#FFFFFF"},
                                        {"type": "text", "text": "產出分工紀錄與時間戳記", "size": "xs", "color": "#94A3B8", "margin": "xs", "wrap": True}
                                    ]
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "匯出",
                                        "text": "/export"
                                    },
                                    "style": "primary",
                                    "color": "#0284C7",
                                    "height": "sm",
                                    "flex": 3
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
            "backgroundColor": "#0F172A",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "前往專案主選單",
                        "text": "/選單"
                    },
                    "style": "primary",
                    "color": "#334155",
                    "height": "sm"
                }
            ]
        }
    }
    return FlexMessage(
        alt_text="PRO 會議記錄功能已解鎖",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_meeting_active_flex(meeting_info: dict) -> FlexMessage:
    """會議記錄進行中提示卡片（簡約洗鍊風格）"""
    starter_name = meeting_info.get("starter_name", "組員")
    start_time = meeting_info.get("start_time", "")

    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "LEADERGUARD PRO", "size": "xs", "color": "#38BDF8", "weight": "bold"},
                        {"type": "text", "text": "記錄中", "size": "xs", "color": "#10B981", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": "小組會議記錄中",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "群組成員發言已啟動自動記錄",
                    "size": "xs",
                    "color": "#94A3B8",
                    "margin": "xs",
                    "wrap": True
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "16px",
            "backgroundColor": "#0B132B",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E293B",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#38BDF8",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "text",
                            "text": f"發起成員：{starter_name}",
                            "size": "xs",
                            "color": "#E2E8F0",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": f"開始時間：{start_time}",
                            "size": "xs",
                            "color": "#94A3B8",
                            "margin": "xs"
                        },
                        {"type": "separator", "color": "#334155", "margin": "sm"},
                        {
                            "type": "text",
                            "text": "提示：接下來群組成員之討論發言將自動記錄。討論完畢後，請點選下方按鈕或輸入「/結束會議」，系統將由 AI 提煉會議重點與待辦清單。",
                            "size": "xs",
                            "color": "#FFFFFF",
                            "margin": "sm",
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
            "backgroundColor": "#0F172A",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "結束會議並由 AI 統整",
                        "text": "/結束會議"
                    },
                    "style": "primary",
                    "color": "#0284C7",
                    "height": "sm"
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "前往專案選單",
                        "text": "/選單"
                    },
                    "style": "primary",
                    "color": "#334155",
                    "height": "sm"
                }
            ]
        }
    }
    return FlexMessage(
        alt_text="小組會議記錄中",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_meeting_summary_flex(summary_data: dict) -> FlexMessage:
    """AI 會議記錄統整成果卡片（簡約洗鍊、資訊直觀清楚）"""
    title = summary_data.get("title", "小組專案會議")
    start_time = summary_data.get("start_time", "")
    end_time = summary_data.get("end_time", "")
    time_str = f"{start_time} ~ {end_time[-5:] if end_time else ''}"

    summary_points = summary_data.get("summary_points", [])
    decisions = summary_data.get("decisions", [])
    action_items = summary_data.get("action_items", [])

    body_contents = []

    # 1. 討論重點
    point_lines = "\n".join([f"• {p}" for p in summary_points]) if summary_points else "• 討論專案進度與工作規劃"
    body_contents.append({
        "type": "box",
        "layout": "vertical",
        "backgroundColor": "#1E293B",
        "paddingAll": "12px",
        "cornerRadius": "8px",
        "borderColor": "#38BDF8",
        "borderWidth": "1px",
        "contents": [
            {"type": "text", "text": "討論重點摘要", "weight": "bold", "size": "sm", "color": "#38BDF8"},
            {"type": "separator", "color": "#334155", "margin": "xs"},
            {"type": "text", "text": point_lines, "size": "xs", "color": "#FFFFFF", "margin": "sm", "wrap": True}
        ]
    })

    # 2. 決議事項
    if decisions:
        decision_lines = "\n".join([f"• {d}" for d in decisions])
        body_contents.append({
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#1E293B",
            "paddingAll": "12px",
            "cornerRadius": "8px",
            "borderColor": "#10B981",
            "borderWidth": "1px",
            "contents": [
                {"type": "text", "text": "小組決議事項", "weight": "bold", "size": "sm", "color": "#10B981"},
                {"type": "separator", "color": "#334155", "margin": "xs"},
                {"type": "text", "text": decision_lines, "size": "xs", "color": "#FFFFFF", "margin": "sm", "wrap": True}
            ]
        })

    # 3. 待辦工作與指派
    if action_items:
        action_lines = "\n".join([f"• {item.get('task', '')}（負責人：{item.get('assignee', '待認領')}）" for item in action_items])
        body_contents.append({
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#1E293B",
            "paddingAll": "12px",
            "cornerRadius": "8px",
            "borderColor": "#FBBF24",
            "borderWidth": "1px",
            "contents": [
                {"type": "text", "text": "待辦事項與指派", "weight": "bold", "size": "sm", "color": "#FBBF24"},
                {"type": "separator", "color": "#334155", "margin": "xs"},
                {"type": "text", "text": action_lines, "size": "xs", "color": "#FFFFFF", "margin": "sm", "wrap": True}
            ]
        })

    bubble = {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "LEADERGUARD PRO", "size": "xs", "color": "#38BDF8", "weight": "bold"},
                        {"type": "text", "text": "AI 統整完成", "size": "xs", "color": "#10B981", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": title,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md",
                    "margin": "xs",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": f"會議時間：{time_str}",
                    "size": "xs",
                    "color": "#94A3B8",
                    "margin": "xs"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "16px",
            "spacing": "md",
            "backgroundColor": "#0B132B",
            "contents": body_contents
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "backgroundColor": "#0F172A",
            "spacing": "sm",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "任務清單",
                                "text": "/task 清單"
                            },
                            "style": "primary",
                            "color": "#0284C7",
                            "height": "sm",
                            "flex": 1
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "存證報告",
                                "text": "/export"
                            },
                            "style": "primary",
                            "color": "#0284C7",
                            "height": "sm",
                            "flex": 1
                        }
                    ]
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "前往專案主選單",
                        "text": "/選單"
                    },
                    "style": "primary",
                    "color": "#334155",
                    "height": "sm"
                }
            ]
        }
    }
    return FlexMessage(
        alt_text=f"AI 會議記錄統整・{title}",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )

def create_ai_reminder_flex(pending_tasks: list = None, mode: str = "friendly") -> FlexMessage:
    """進度提醒卡片（簡約洗鍊、資訊直觀清楚）"""
    if pending_tasks is None:
        pending_tasks = []

    if mode in ["formal", "professor"]:
        title_text = "專案里程碑通報"
        sub_text = "進度核定通知"
        if pending_tasks:
            preview = "、".join([f"「{t.get('title', '待辦工作')}」" for t in pending_tasks[:3]])
            speech = f"目前尚有 {len(pending_tasks)} 項工作待認領（{preview}）。請相關成員儘速完成認領與進度回報。"
        else:
            speech = "目前所有工作均已完成指派，請各成員依時程推進交付成果。"
    else:
        title_text = "專案進度提醒"
        sub_text = "小組協作通知"
        if pending_tasks:
            preview = "、".join([f"「{t.get('title', '待辦工作')}」" for t in pending_tasks[:3]])
            speech = f"目前尚有 {len(pending_tasks)} 項待認領工作（{preview}）。請成員點選下方按鈕認領或進行隨機分配。"
        else:
            speech = "目前所有工作皆已認領完畢，請各成員持續推進專案進度。"

    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F172A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": title_text, "weight": "bold", "size": "md", "color": "#38BDF8"},
                        {"type": "text", "text": sub_text, "size": "xs", "color": "#94A3B8", "align": "end"}
                    ]
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "16px",
            "backgroundColor": "#0B132B",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E293B",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#38BDF8",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "text",
                            "text": speech,
                            "size": "sm",
                            "color": "#FFFFFF",
                            "wrap": True
                        }
                    ]
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
                                "label": "認領工作",
                                "text": "/task 清單"
                            },
                            "style": "primary",
                            "color": "#0284C7",
                            "height": "sm",
                            "flex": 1
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "隨機分配",
                                "text": "/抽籤"
                            },
                            "style": "primary",
                            "color": "#D97706",
                            "height": "sm",
                            "flex": 1
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "10px",
            "backgroundColor": "#0F172A",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "查看存證報告",
                        "text": "/export"
                    },
                    "style": "primary",
                    "color": "#334155",
                    "height": "sm"
                }
            ]
        }
    }
    return FlexMessage(
        alt_text=title_text,
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )


