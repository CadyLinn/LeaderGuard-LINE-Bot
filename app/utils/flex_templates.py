import os
import json
from linebot.v3.messaging import (
    FlexMessage,
    FlexContainer,
    QuickReply,
    QuickReplyItem,
    MessageAction
)

def get_main_quick_reply() -> QuickReply:
    """聊天室底部的常駐快捷按鈕列（JoJo 狂氣波普風）"""
    return QuickReply(items=[
        QuickReplyItem(action=MessageAction(label="任務分工", text="/選單")),
        QuickReplyItem(action=MessageAction(label="任務清單", text="/task 清單")),
        QuickReplyItem(action=MessageAction(label="🎲 死鬥輪盤", text="/roulette")),
        QuickReplyItem(action=MessageAction(label="升級方案", text="/升級方案")),
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
                            {"type": "text", "text": "【替身能力】", "size": "xxs", "color": "#06B6D4", "weight": "bold"},
                            {"type": "text", "text": "ゴゴゴ", "size": "xxs", "color": "#F43F5E", "align": "end", "weight": "bold"}
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
                    {"type": "text", "text": "使命覺悟：", "weight": "bold", "size": "xs", "color": "#FDE047"},
                    {"type": "text", "text": "• 統整組員文字與圖表\n• PPT / Canva 視覺暴擊美化\n• 彙整報告講稿備忘錄", "size": "xs", "color": "#F3E8FF", "wrap": True}
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
                            "label": "發動替身：建立任務",
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
                            {"type": "text", "text": "【替身能力】", "size": "xxs", "color": "#06B6D4", "weight": "bold"},
                            {"type": "text", "text": "ドドド", "size": "xxs", "color": "#FDE047", "align": "end", "weight": "bold"}
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
                    {"type": "text", "text": "使命覺悟：", "weight": "bold", "size": "xs", "color": "#FDE047"},
                    {"type": "text", "text": "• 掌握專案全脈絡\n• 代表小組霸氣發表\n• 現場教授提問強勢應對", "size": "xs", "color": "#F3E8FF", "wrap": True}
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
                            "label": "發動替身：建立任務",
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
                            {"type": "text", "text": "【替身能力】", "size": "xxs", "color": "#06B6D4", "weight": "bold"},
                            {"type": "text", "text": "ズキューン", "size": "xxs", "color": "#06B6D4", "align": "end", "weight": "bold"}
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
                    {"type": "text", "text": "使命覺悟：", "weight": "bold", "size": "xs", "color": "#FDE047"},
                    {"type": "text", "text": "• 前期專案主題地毯式調研\n• 相關文獻與真實案例查證\n• 數據統整與來源鐵證", "size": "xs", "color": "#F3E8FF", "wrap": True}
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
                            "label": "發動替身：建立任務",
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
                            {"type": "text", "text": "【替身能力】", "size": "xxs", "color": "#06B6D4", "weight": "bold"},
                            {"type": "text", "text": "WRYYYY", "size": "xxs", "color": "#FDE047", "align": "end", "weight": "bold"}
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
                    {"type": "text", "text": "使命覺悟：", "weight": "bold", "size": "xs", "color": "#FDE047"},
                    {"type": "text", "text": "• 彙整各章節文字與圖表\n• 校對格式排版與文獻引用\n• 產出完美無瑕期末正式報告", "size": "xs", "color": "#F3E8FF", "wrap": True}
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
                            "label": "發動替身：建立任務",
                            "text": "/task 新增 書面報告撰寫統整 負責期末書面Word/PDF格式與內容校對"
                        },
                        "style": "primary",
                        "color": "#E11D48",
                        "height": "sm"
                    }
                ]
            }
        },
        # 卡片 5：一鍵批次建立全套（黃金精神狂暴卡）
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
                            {"type": "text", "text": "【黃金之風】", "size": "xxs", "color": "#FDE047", "weight": "bold"},
                            {"type": "text", "text": "オラオラ！", "size": "xxs", "color": "#06B6D4", "align": "end", "weight": "bold"}
                        ]
                    },
                    {"type": "text", "text": "一鍵全套分工連擊！", "weight": "bold", "color": "#FDE047", "size": "md", "margin": "xs"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#1E1636",
                "contents": [
                    {"type": "text", "text": "組長無想轉生首選", "weight": "bold", "size": "sm", "color": "#06B6D4"},
                    {"type": "text", "text": "一次召喚 4 大標準分工（簡報、報告、調研、書面），誰敢已讀不回？直接認領！", "size": "xs", "color": "#F3E8FF", "wrap": True}
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
                    {"type": "text", "text": "➕ 自訂專屬替身工作", "weight": "bold", "color": "#FFFFFF", "size": "md"}
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
                    {"type": "text", "text": "だが断る！（但是我拒絕侷限）", "weight": "bold", "size": "sm", "color": "#FDE047"},
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
        alt_text="小組專案常用分工範本（JoJo 波普版）",
        contents=FlexContainer.from_dict(carousel),
        quick_reply=get_main_quick_reply()
    )

def create_main_menu_flex() -> FlexMessage:
    """小組功能主選單卡片（JoJo 波普風：高對比、鮮明按鈕、Apple HIG 清晰規範）"""
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
                        {"type": "text", "text": "【組長保險・已讀不回審判庭】", "weight": "bold", "color": "#FDE047", "size": "sm"},
                        {"type": "text", "text": "ゴゴゴ", "weight": "bold", "color": "#F43F5E", "size": "sm", "align": "end"}
                    ]
                },
                {
                    "type": "text",
                    "text": "小組協作・替身使者功能選單",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "lg",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "組長不必親自追殺進度，這就是命運的裁判！",
                    "color": "#06B6D4",
                    "size": "xs",
                    "margin": "sm",
                    "wrap": True
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
                            "text": "💥 專案工作分工（連擊召喚）",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#06B6D4"
                        },
                        {
                            "type": "text",
                            "text": "簡報、報告、文獻調研全套範本，點選一鍵發起，立刻認領責任！",
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
                                "label": "➕ 自訂新增工作",
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
                # 區塊 2：死鬥輪盤抽籤
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#1E1636",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#F43F5E",
                    "borderWidth": "2px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "🎲 死鬥輪盤・命運抽籤",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#F43F5E"
                        },
                        {
                            "type": "text",
                            "text": "沒人認領的工作？這就是替身使者的命運！系統優先抽尚未負責者！",
                            "size": "xs",
                            "color": "#F3E8FF",
                            "margin": "xs",
                            "wrap": True
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "🎲 啟動命運死鬥輪盤",
                                "text": "/roulette"
                            },
                            "style": "primary",
                            "color": "#E11D48",
                            "margin": "md",
                            "height": "sm"
                        }
                    ]
                },
                # 區塊 3：進度狀態與指南
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
                            "text": "📜 專案審判現況與指令秘笈",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#FDE047"
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
                                        "label": "指令手冊",
                                        "text": "/常用指令說明"
                                    },
                                    "style": "primary",
                                    "color": "#E11D48",
                                    "height": "sm"
                                }
                            ]
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
                        {"type": "text", "text": "【替身指令全集中】", "size": "xs", "color": "#FDE047", "weight": "bold"},
                        {"type": "text", "text": "ドドド…", "size": "xs", "color": "#F43F5E", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": "常用指令說明・秘笈",
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
                        {"type": "text", "text": "【新任務登場】", "size": "xs", "color": "#06B6D4", "weight": "bold"},
                        {"type": "text", "text": "ズキューン", "size": "xs", "color": "#FDE047", "align": "end", "weight": "bold"}
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
                        {"type": "text", "text": "指派召喚者", "size": "xs", "color": "#06B6D4"},
                        {"type": "text", "text": creator_name, "size": "xs", "color": "#FFFFFF", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "當前狀態", "size": "xs", "color": "#06B6D4"},
                        {"type": "text", "text": "待認領（命運等待中）", "size": "xs", "color": "#F43F5E", "align": "end", "weight": "bold"}
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
                                    "text": "尚未認領（ゴゴゴ…）",
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
                    "label": "🎲 啟動輪盤抽籤未認領工作",
                    "text": "/roulette"
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
                        {"type": "text", "text": "ゴゴゴ", "size": "xs", "color": "#F43F5E", "align": "end", "weight": "bold"}
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
                    "text": "誰在做事、誰在摸魚，全都逃不過替身之眼！",
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
    """🎲 隨機抽籤結果卡片（JoJo 命運死鬥輪盤風格）"""
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
                        {"type": "text", "text": "🎲 死鬥輪盤裁決", "size": "xs", "color": "#FDE047", "weight": "bold"},
                        {"type": "text", "text": "オラオラ！", "size": "xs", "color": "#06B6D4", "align": "end", "weight": "bold"}
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
                            "text": "命運選中的替身使者：",
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
                            "text": "覺悟吧！逃避是沒有用的，全組都在看著你！",
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
                        {"type": "text", "text": "【組長保險指南】", "size": "xs", "weight": "bold", "color": "#FDE047"},
                        {"type": "text", "text": "ドドド…", "size": "xs", "weight": "bold", "color": "#06B6D4", "align": "end"}
                    ]
                },
                {
                    "type": "text",
                    "text": "4 步驟開啟替身審判！",
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
                    "layout": "horizontal",
                    "spacing": "md",
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
                                { "type": "text", "text": "1", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center" }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "把我召喚進小組群組！",
                            "size": "sm",
                            "color": "#FFFFFF",
                            "gravity": "center",
                            "wrap": True,
                            "flex": 1,
                            "weight": "bold"
                        }
                    ]
                },
                { "type": "separator", "color": "#2A1B4E" },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
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
                            "text": "輸入 /assign 發起連擊分工",
                            "size": "sm",
                            "color": "#FFFFFF",
                            "gravity": "center",
                            "wrap": True,
                            "flex": 1,
                            "weight": "bold"
                        }
                    ]
                },
                { "type": "separator", "color": "#2A1B4E" },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
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
                                { "type": "text", "text": "3", "size": "xs", "weight": "bold", "color": "#160F29", "align": "center" }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 1,
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "沉寂 30 分鐘自動替身催繳",
                                    "size": "sm",
                                    "color": "#FFFFFF",
                                    "weight": "bold",
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "無人認領將公告並發動死鬥輪盤隨機指派！",
                                    "size": "xxs",
                                    "color": "#06B6D4",
                                    "wrap": True,
                                    "margin": "xs"
                                }
                            ]
                        }
                    ]
                },
                { "type": "separator", "color": "#2A1B4E" },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
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
                                { "type": "text", "text": "4", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center" }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "期末輸入 /export 產出互評鐵證",
                            "size": "sm",
                            "color": "#FFFFFF",
                            "gravity": "center",
                            "wrap": True,
                            "flex": 1,
                            "weight": "bold"
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
            "backgroundColor": "#160F29",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "color": "#E11D48",
                    "action": manual_action
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "color": "#0891B2",
                    "action": {
                        "type": "uri",
                        "label": "立即召喚進群組",
                        "uri": group_invite_url
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
                        {"type": "text", "text": "【黃金覺悟】", "size": "xs", "color": "#FDE047", "weight": "bold"},
                        {"type": "text", "text": "WRYYYY", "size": "xs", "color": "#06B6D4", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "text",
                    "text": "組長保險・尊榮 Pro 升級方案",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "全面解鎖進階替身催繳能力與期末互評防護罩",
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
                            "text": "• 4 大標準分工範本與自訂任務\n• 🎲 死鬥輪盤隨機抽籤（優先鎖定無任務者）\n• 本地資料存證與小組成員名冊",
                            "size": "xs",
                            "color": "#F3E8FF",
                            "margin": "sm",
                            "wrap": True
                        }
                    ]
                },
                # 方案 2：尊榮組長保險 Pro (高能特色卡)
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
                                {"type": "text", "text": "🔥 尊榮組長保險 Pro", "weight": "bold", "size": "sm", "color": "#FDE047", "flex": 1},
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "backgroundColor": "#E11D48",
                                    "paddingVertical": "2px",
                                    "paddingHorizontal": "6px",
                                    "cornerRadius": "4px",
                                    "contents": [
                                        {"type": "text", "text": "PRO", "size": "xxs", "color": "#FFFFFF", "weight": "bold"}
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "• 30 分鐘沉寂自動催繳與 LINE 警示彈幕通知\n• 小組期末專案互評與個人貢獻度 PDF 鐵證報表\n• Google Docs / Notion 雲端即時同步\n• 無上限多組專案與跨群協作支援",
                            "size": "xs",
                            "color": "#FFFFFF",
                            "margin": "sm",
                            "wrap": True
                        }
                    ]
                },
                {
                    "type": "text",
                    "text": "不想再當組長冤大頭？升級 Pro 讓替身自動幫你主持公道！",
                    "size": "xxs",
                    "color": "#F43F5E",
                    "align": "center",
                    "wrap": True,
                    "weight": "bold"
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
                    "color": "#E11D48",
                    "height": "sm",
                    "action": {
                        "type": "message",
                        "label": "了解方案 / 諮詢升級",
                        "text": "/諮詢升級"
                    }
                }
            ]
        }
    }
    return FlexMessage(
        alt_text="組長保險・升級方案",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )
