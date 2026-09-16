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
    """聊天室底部的常駐快捷按鈕列（莫蘭迪極簡風）"""
    return QuickReply(items=[
        QuickReplyItem(action=MessageAction(label="任務分工", text="/選單")),
        QuickReplyItem(action=MessageAction(label="任務清單", text="/task 清單")),
        QuickReplyItem(action=MessageAction(label="🎲 抽籤分工", text="/roulette")),
        QuickReplyItem(action=MessageAction(label="升級方案", text="/升級方案")),
        QuickReplyItem(action=MessageAction(label="指令說明", text="/常用指令說明")),
    ])

def create_preset_tasks_carousel() -> FlexMessage:
    """常見小組專案工作範本輪播卡片（莫蘭迪黑白灰配色，mega 尺寸）"""
    carousel_contents = [
        # 卡片 1：簡報製作
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#27272A",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "簡報製作與美編", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#FFFFFF",
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#18181B"},
                    {"type": "text", "text": "• 統整組員文字與圖表\n• PPT / Canva 視覺美化\n• 彙整報告講稿備忘錄", "size": "xs", "color": "#71717A", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#F4F4F5",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 簡報製作與美化 負責PPT視覺美編與排版"
                        },
                        "style": "primary",
                        "color": "#27272A",
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
                "backgroundColor": "#3F3F46",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "上台口頭報告", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#FFFFFF",
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#18181B"},
                    {"type": "text", "text": "• 掌握專案架構脈絡\n• 代表小組上台發表\n• 現場提問 Q&A 應對", "size": "xs", "color": "#71717A", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#F4F4F5",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 上台口頭報告 負責掌握專案脈絡並代表口頭發表"
                        },
                        "style": "primary",
                        "color": "#3F3F46",
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
                "backgroundColor": "#52525B",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "文獻查證與資料蒐集", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#FFFFFF",
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#18181B"},
                    {"type": "text", "text": "• 前期專案主題調研\n• 相關文獻與案例查證\n• 數據統整與來源驗證", "size": "xs", "color": "#71717A", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#F4F4F5",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 文獻查證與資料蒐集 負責前期調研、文獻查證與數據整理"
                        },
                        "style": "primary",
                        "color": "#52525B",
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
                "backgroundColor": "#27272A",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "書面報告撰寫統整", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#FFFFFF",
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#18181B"},
                    {"type": "text", "text": "• 彙整各章節文字與圖表\n• 校對格式、目錄與文獻\n• 產出期末正式完整報告", "size": "xs", "color": "#71717A", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#F4F4F5",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 書面報告撰寫統整 負責期末書面Word/PDF格式與內容校對"
                        },
                        "style": "primary",
                        "color": "#27272A",
                        "height": "sm"
                    }
                ]
            }
        },
        # 卡片 5：一鍵批次建立全套
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#18181B",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "一鍵全套分工", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#FFFFFF",
                "contents": [
                    {"type": "text", "text": "組長省時首選", "weight": "bold", "size": "sm", "color": "#18181B"},
                    {"type": "text", "text": "一次建立以上 4 項小組標準分工（簡報、報告、資料、書面），全組立刻認領。", "size": "xs", "color": "#71717A", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#F4F4F5",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "一鍵建立全部",
                            "text": "/task 批次建立"
                        },
                        "style": "primary",
                        "color": "#18181B",
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
                "backgroundColor": "#3F3F46",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "➕ 自訂其他工作", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "backgroundColor": "#FFFFFF",
                "contents": [
                    {"type": "text", "text": "不限於現有範本", "weight": "bold", "size": "sm", "color": "#18181B"},
                    {"type": "text", "text": "點選下方按鈕，對話框會自動帶入指令，直接輸入工作名稱即可！", "size": "xs", "color": "#71717A", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "backgroundColor": "#F4F4F5",
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
                        "color": "#3F3F46",
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
    """小組功能主選單卡片（莫蘭迪黑白灰風格）"""
    bubble = {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#18181B",
            "paddingAll": "20px",
            "contents": [
                {
                    "type": "text",
                    "text": "【組長保險】專案協作功能選單",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md"
                },
                {
                    "type": "text",
                    "text": "組長不用自己催進度，分工與數據交給機器人處理",
                    "color": "#A1A1AA",
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
            "backgroundColor": "#F4F4F5",
            "paddingAll": "16px",
            "contents": [
                # 區塊 1：工作發起與認領
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FFFFFF",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#E4E4E7",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "專案工作分工",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#18181B"
                        },
                        {
                            "type": "text",
                            "text": "內建簡報、上台報告、資料調研等範本，點擊即可一鍵建立發起。",
                            "size": "xs",
                            "color": "#71717A",
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
                                    "color": "#27272A",
                                    "height": "sm"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "任務清單",
                                        "text": "/task 清單"
                                    },
                                    "style": "secondary",
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
                            "height": "sm",
                            "margin": "sm"
                        }
                    ]
                },
                # 區塊 2：隨機抽籤
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FFFFFF",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#E4E4E7",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "🎲 隨機抽籤分工",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#18181B"
                        },
                        {
                            "type": "text",
                            "text": "卡關沒人認領的工作？直接交給系統隨機抽籤，公平省事。",
                            "size": "xs",
                            "color": "#71717A",
                            "margin": "xs",
                            "wrap": True
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "🎲 隨機抽籤",
                                "text": "/roulette"
                            },
                            "style": "primary",
                            "color": "#3F3F46",
                            "margin": "md",
                            "height": "sm"
                        }
                    ]
                },
                # 區塊 3：進度狀態與指南
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FFFFFF",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#E4E4E7",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "專案狀況與說明",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#18181B"
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
                                    "style": "secondary",
                                    "height": "sm"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "常用指令說明",
                                        "text": "/常用指令說明"
                                    },
                                    "style": "secondary",
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
    """操作指南 Flex 卡片（莫蘭迪黑白灰表格化設計，尺寸設為 giga）"""
    table_data = [
        ("挑選範本", "/任務 範本", "/task"),
        ("查看工作", "/任務 清單", "/tasks"),
        ("認領工作", "/認領 [編號]", "/claim"),
        ("自訂任務", "/任務 新增", "/task add"),
        ("🎲 抽籤分工", "/抽籤", "/roulette"),
        ("加幽靈組員", "/成員 新增", "/member add"),
        ("組員名冊", "/成員", "/member"),
        ("專案進度", "/狀態", "/status")
    ]

    rows = []
    for idx, (func, cn, en) in enumerate(table_data):
        bg_color = "#FFFFFF" if idx % 2 == 0 else "#F4F4F5"
        rows.append({
            "type": "box",
            "layout": "horizontal",
            "backgroundColor": bg_color,
            "paddingVertical": "8px",
            "paddingHorizontal": "10px",
            "alignItems": "center",
            "contents": [
                {"type": "text", "text": func, "size": "xs", "weight": "bold", "color": "#18181B", "flex": 3, "wrap": True},
                {"type": "text", "text": cn, "size": "xs", "weight": "bold", "color": "#27272A", "flex": 4, "wrap": True},
                {"type": "text", "text": en, "size": "xs", "color": "#71717A", "flex": 3, "wrap": True}
            ]
        })

    bubble = {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#18181B",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "text",
                    "text": "常用指令說明",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md"
                },
                {
                    "type": "text",
                    "text": "指令前加「/」，輸入中文或英文都可以！",
                    "color": "#A1A1AA",
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
            "backgroundColor": "#F4F4F5",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "backgroundColor": "#27272A",
                    "paddingVertical": "8px",
                    "paddingHorizontal": "10px",
                    "cornerRadius": "4px",
                    "contents": [
                        {"type": "text", "text": "你想做的事", "weight": "bold", "size": "xs", "color": "#FFFFFF", "flex": 3},
                        {"type": "text", "text": "中文指令", "weight": "bold", "size": "xs", "color": "#D4D4D8", "flex": 4},
                        {"type": "text", "text": "英文指令", "weight": "bold", "size": "xs", "color": "#A1A1AA", "flex": 3}
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
                    "backgroundColor": "#E4E4E7",
                    "cornerRadius": "6px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "• 認領範例：/認領 T001（或 /claim T001）\n• 幽靈組員：/成員 新增 小明 小華\n• 抽籤機制：🎲 系統優先抽尚未分配任務的人",
                            "size": "xxs",
                            "color": "#52525B",
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
            "backgroundColor": "#F4F4F5",
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
                    "color": "#27272A",
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
    """任務建立成功通知卡片（莫蘭迪黑白灰風格）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#27272A",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "text",
                    "text": "新增小組任務",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "paddingAll": "16px",
            "backgroundColor": "#FFFFFF",
            "contents": [
                {
                    "type": "text",
                    "text": f"【{task_id}】{title}",
                    "weight": "bold",
                    "size": "md",
                    "color": "#18181B",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": description if description else "（無補充說明）",
                    "size": "xs",
                    "color": "#71717A",
                    "wrap": True
                },
                {"type": "separator", "color": "#E4E4E7"},
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "建立者", "size": "xs", "color": "#A1A1AA"},
                        {"type": "text", "text": creator_name, "size": "xs", "color": "#18181B", "align": "end", "weight": "bold"}
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "狀態", "size": "xs", "color": "#A1A1AA"},
                        {"type": "text", "text": "待認領", "size": "xs", "color": "#52525B", "align": "end", "weight": "bold"}
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "backgroundColor": "#F4F4F5",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "認領任務",
                        "text": f"/claim {task_id}"
                    },
                    "style": "primary",
                    "color": "#27272A",
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
    """任務清單卡片（莫蘭迪黑白灰風格，giga 寬版尺寸）"""
    if not tasks:
        item_boxes = [{
            "type": "text",
            "text": "目前這組還沒有任何待辦任務，大家可以輕鬆一下！",
            "size": "sm",
            "color": "#71717A",
            "align": "center",
            "margin": "lg"
        }]
        footer_box = {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "paddingAll": "12px",
            "backgroundColor": "#F4F4F5",
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
                    "color": "#27272A",
                    "height": "sm"
                },
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "瀏覽常用範本",
                        "text": "/task 範本"
                    },
                    "style": "secondary",
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
                                    "color": "#18181B",
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "尚未認領",
                                    "size": "xxs",
                                    "color": "#71717A"
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
                            "color": "#27272A",
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
                                    "color": "#71717A",
                                    "wrap": True
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 3,
                            "contents": [
                                {
                                    "type": "text",
                                    "text": assignee_name,
                                    "size": "xs",
                                    "color": "#18181B",
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
                "height": "sm"
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "常用分工範本",
                    "text": "/task 範本"
                },
                "style": "secondary",
                "height": "sm"
            }
        ]
        if has_pending:
            footer_buttons.insert(0, {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "🎲 抽籤未認領工作",
                    "text": "/roulette"
                },
                "style": "primary",
                "color": "#3F3F46",
                "height": "sm",
                "margin": "sm"
            })
            
        footer_box = {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "paddingAll": "12px",
            "backgroundColor": "#F4F4F5",
            "contents": footer_buttons
        }

    bubble = {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#18181B",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "text",
                    "text": "小組工作清單",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md"
                },
                {
                    "type": "text",
                    "text": "即時掌握每項工作負責進度",
                    "color": "#A1A1AA",
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
            "backgroundColor": "#FFFFFF",
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
    """🎲 隨機抽籤結果卡片（莫蘭迪黑白灰極簡風格）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#18181B",
            "paddingAll": "16px",
            "contents": [
                {"type": "text", "text": "🎲 抽籤分工結果", "weight": "bold", "color": "#FFFFFF", "size": "md", "align": "center"}
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "paddingAll": "16px",
            "backgroundColor": "#FFFFFF",
            "contents": [
                {
                    "type": "text",
                    "text": "由你負責：",
                    "size": "xs",
                    "color": "#71717A",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": victim_name,
                    "weight": "bold",
                    "size": "xl",
                    "color": "#18181B",
                    "align": "center",
                    "wrap": True
                },
                {"type": "separator", "color": "#E4E4E7"},
                {
                    "type": "text",
                    "text": f"抽籤任務：【{task_id}】{task_title}",
                    "size": "sm",
                    "color": "#27272A",
                    "wrap": True,
                    "weight": "bold"
                },
                {
                    "type": "text",
                    "text": "辛苦了！有問題隨時在群組討論。",
                    "size": "xs",
                    "color": "#71717A",
                    "align": "center"
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
    """加入好友時發送的 4 步驟使用手冊 Flex 卡片（莫蘭迪黑白灰高質感配色）"""
    manual_url = os.getenv("MANUAL_URL", "")
    group_invite_url = os.getenv("GROUP_INVITE_URL", "https://line.me/R/nv/recommendOA/@805yffpw")

    manual_action = (
        {"type": "uri", "label": "查看完整教學", "uri": manual_url}
        if manual_url
        else {"type": "message", "label": "查看完整教學", "text": "/常用指令說明"}
    )

    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#18181B",
            "paddingAll": "20px",
            "contents": [
                {
                    "type": "text",
                    "text": "使用手冊",
                    "size": "sm",
                    "weight": "bold",
                    "color": "#A1A1AA"
                },
                {
                    "type": "text",
                    "text": "4 步驟開始使用",
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
            "backgroundColor": "#F4F4F5",
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
                            "width": "24px",
                            "height": "24px",
                            "cornerRadius": "12px",
                            "backgroundColor": "#27272A",
                            "justifyContent": "center",
                            "alignItems": "center",
                            "contents": [
                                { "type": "text", "text": "1", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center" }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "把我拉進小組群組",
                            "size": "sm",
                            "color": "#18181B",
                            "gravity": "center",
                            "wrap": True,
                            "flex": 1
                        }
                    ]
                },
                { "type": "separator", "color": "#E4E4E7" },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "width": "24px",
                            "height": "24px",
                            "cornerRadius": "12px",
                            "backgroundColor": "#27272A",
                            "justifyContent": "center",
                            "alignItems": "center",
                            "contents": [
                                { "type": "text", "text": "2", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center" }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "輸入 /assign 指派任務",
                            "size": "sm",
                            "color": "#18181B",
                            "gravity": "center",
                            "wrap": True,
                            "flex": 1
                        }
                    ]
                },
                { "type": "separator", "color": "#E4E4E7" },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "width": "24px",
                            "height": "24px",
                            "cornerRadius": "12px",
                            "backgroundColor": "#52525B",
                            "justifyContent": "center",
                            "alignItems": "center",
                            "contents": [
                                { "type": "text", "text": "3", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center" }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 1,
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "沉寂 30 分鐘自動提醒",
                                    "size": "sm",
                                    "color": "#18181B",
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "無人認領將公告並隨機指派",
                                    "size": "xxs",
                                    "color": "#71717A",
                                    "wrap": True,
                                    "margin": "xs"
                                }
                            ]
                        }
                    ]
                },
                { "type": "separator", "color": "#E4E4E7" },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "width": "24px",
                            "height": "24px",
                            "cornerRadius": "12px",
                            "backgroundColor": "#27272A",
                            "justifyContent": "center",
                            "alignItems": "center",
                            "contents": [
                                { "type": "text", "text": "4", "size": "xs", "weight": "bold", "color": "#FFFFFF", "align": "center" }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "期末輸入 /export 匯出報告",
                            "size": "sm",
                            "color": "#18181B",
                            "gravity": "center",
                            "wrap": True,
                            "flex": 1
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
            "backgroundColor": "#F4F4F5",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "color": "#18181B",
                    "action": manual_action
                },
                {
                    "type": "button",
                    "style": "secondary",
                    "height": "sm",
                    "color": "#52525B",
                    "action": {
                        "type": "uri",
                        "label": "立即拉我進群組",
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
    """升級方案卡片（莫蘭迪黑白灰質感設計）"""
    bubble = {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#18181B",
            "paddingAll": "20px",
            "contents": [
                {
                    "type": "text",
                    "text": "組長保險・升級方案",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "size": "md"
                },
                {
                    "type": "text",
                    "text": "全面解鎖進階小組專案協作與催繳保障",
                    "color": "#A1A1AA",
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
            "backgroundColor": "#F4F4F5",
            "contents": [
                # 方案 1：免費版
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FFFFFF",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#E4E4E7",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "alignItems": "center",
                            "contents": [
                                {"type": "text", "text": "基礎免費版", "weight": "bold", "size": "sm", "color": "#18181B", "flex": 1},
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "backgroundColor": "#E4E4E7",
                                    "paddingVertical": "2px",
                                    "paddingHorizontal": "6px",
                                    "cornerRadius": "4px",
                                    "contents": [
                                        {"type": "text", "text": "使用中", "size": "xxs", "color": "#52525B", "weight": "bold"}
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "text",
                            "text": "• 4 大標準工作範本與自訂任務\n• 🎲 隨機抽籤（優先指派無任務者）\n• 本地資料永續保存與成員名冊",
                            "size": "xs",
                            "color": "#71717A",
                            "margin": "sm",
                            "wrap": True
                        }
                    ]
                },
                # 方案 2：專業版 Pro
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FFFFFF",
                    "paddingAll": "14px",
                    "cornerRadius": "8px",
                    "borderColor": "#27272A",
                    "borderWidth": "2px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "alignItems": "center",
                            "contents": [
                                {"type": "text", "text": "尊榮組長保險 Pro", "weight": "bold", "size": "sm", "color": "#18181B", "flex": 1},
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "backgroundColor": "#18181B",
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
                            "text": "• 30 分鐘沉寂自動催繳與 LINE 警示通知\n• 小組期末專案互評與個人貢獻度 PDF 報表\n• Google Docs / Notion 雲端即時同步\n• 無上限多組專案與跨群協作支援",
                            "size": "xs",
                            "color": "#27272A",
                            "margin": "sm",
                            "wrap": True
                        }
                    ]
                },
                {
                    "type": "text",
                    "text": "專案組員不想再當冤大頭？升級 Pro 讓全自動保險為您護航！",
                    "size": "xxs",
                    "color": "#71717A",
                    "align": "center",
                    "wrap": True
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "backgroundColor": "#F4F4F5",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "color": "#18181B",
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
