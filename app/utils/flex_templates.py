import json
from linebot.v3.messaging import (
    FlexMessage,
    FlexContainer,
    QuickReply,
    QuickReplyItem,
    MessageAction
)

def get_main_quick_reply() -> QuickReply:
    """聊天室底部的常駐快捷按鈕列"""
    return QuickReply(items=[
        QuickReplyItem(action=MessageAction(label="常用分工範本", text="/task 範本")),
        QuickReplyItem(action=MessageAction(label="任務清單", text="/task 清單")),
        QuickReplyItem(action=MessageAction(label="🎲 抽籤分工", text="/roulette")),
        QuickReplyItem(action=MessageAction(label="專案進度", text="/status")),
        QuickReplyItem(action=MessageAction(label="常用指令說明", text="/常用指令說明")),
    ])

def create_preset_tasks_carousel() -> FlexMessage:
    """常見小組專案工作範本輪播卡片（卡片尺寸設為 mega，文字精簡不截斷）"""
    carousel_contents = [
        # 卡片 1：簡報製作
        {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#0F766E",
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
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#0F172A"},
                    {"type": "text", "text": "• 統整組員文字與圖表\n• PPT / Canva 視覺美化\n• 彙整報告講稿備忘錄", "size": "xs", "color": "#64748B", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 簡報製作與美化 負責PPT視覺美編與排版"
                        },
                        "style": "primary",
                        "color": "#0F766E",
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
                "backgroundColor": "#0284C7",
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
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#0F172A"},
                    {"type": "text", "text": "• 掌握專案架構脈絡\n• 代表小組上台發表\n• 現場提問 Q&A 應對", "size": "xs", "color": "#64748B", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
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
                "backgroundColor": "#7C3AED",
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
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#0F172A"},
                    {"type": "text", "text": "• 前期專案主題調研\n• 相關文獻與案例查證\n• 數據統整與來源驗證", "size": "xs", "color": "#64748B", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 文獻查證與資料蒐集 負責前期調研、文獻查證與數據整理"
                        },
                        "style": "primary",
                        "color": "#7C3AED",
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
                "backgroundColor": "#D97706",
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
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#0F172A"},
                    {"type": "text", "text": "• 彙整各章節文字與圖表\n• 校對格式、目錄與文獻\n• 產出期末正式完整報告", "size": "xs", "color": "#64748B", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "建立任務",
                            "text": "/task 新增 書面報告撰寫統整 負責期末書面Word/PDF格式與內容校對"
                        },
                        "style": "primary",
                        "color": "#D97706",
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
                "backgroundColor": "#1E293B",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "一鍵全套分工", "weight": "bold", "color": "#38BDF8", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "組長省時首選", "weight": "bold", "size": "sm", "color": "#0F172A"},
                    {"type": "text", "text": "一次建立以上 4 項小組標準分工（簡報、報告、資料、書面），全組立刻認領。", "size": "xs", "color": "#64748B", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "12px",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "一鍵建立全部",
                            "text": "/task 批次建立"
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
    """小組功能主選單卡片（含一鍵點擊範本按鈕）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#1E293B",
            "paddingAll": "20px",
            "contents": [
                {
                    "type": "text",
                    "text": "【組長保險】專案協作功能選單",
                    "weight": "bold",
                    "color": "#F8FAFC",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": "組長不用自己催進度，分工與數據交給機器人處理",
                    "color": "#94A3B8",
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
            "contents": [
                # 區塊 1：常用分工範本
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#F8FAFC",
                    "paddingAll": "14px",
                    "cornerRadius": "10px",
                    "borderColor": "#E2E8F0",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "專案工作分工（不用手打字）",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#0F172A"
                        },
                        {
                            "type": "text",
                            "text": "內建簡報、上台報告、資料調研、書面統整等常見範本，點擊即可一鍵建立發起。",
                            "size": "xs",
                            "color": "#64748B",
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
                                    "color": "#0F766E",
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
                        }
                    ]
                },
                # 區塊 2：隨機抽籤
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FEF2F2",
                    "paddingAll": "14px",
                    "cornerRadius": "10px",
                    "borderColor": "#FECACA",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "🎲 隨機抽籤分工",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#991B1B"
                        },
                        {
                            "type": "text",
                            "text": "卡關沒人認領的工作？直接交給系統隨機抽籤，公平省事。",
                            "size": "xs",
                            "color": "#B91C1C",
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
                            "color": "#DC2626",
                            "margin": "md",
                            "height": "sm"
                        }
                    ]
                },
                # 區塊 3：進度狀態與指南
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#F1F5F9",
                    "paddingAll": "14px",
                    "cornerRadius": "10px",
                    "borderColor": "#CBD5E1",
                    "borderWidth": "1px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "專案狀況與說明",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#334155"
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
    """操作指南 Flex 卡片（文字精簡不截斷，尺寸設為 giga）"""
    bubble = {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#1E293B",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "text",
                    "text": "組長保險・常用指令說明",
                    "weight": "bold",
                    "color": "#F8FAFC",
                    "size": "md"
                },
                {
                    "type": "text",
                    "text": "專案分工與進度追蹤指南",
                    "color": "#94A3B8",
                    "size": "xs",
                    "margin": "xs",
                    "wrap": True
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "paddingAll": "16px",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#F8FAFC",
                    "paddingAll": "12px",
                    "cornerRadius": "8px",
                    "contents": [
                        {"type": "text", "text": "任務建立與認領（中英文皆可）", "weight": "bold", "size": "sm", "color": "#0F172A"},
                        {"type": "text", "text": "• /task 範本 或 /任務 範本：快速建立範本", "size": "xs", "color": "#0284C7", "weight": "bold", "margin": "xs", "wrap": True},
                        {"type": "text", "text": "• /task 新增 或 /任務 新增 [名稱]：自訂任務", "size": "xs", "color": "#475569", "margin": "xs", "wrap": True},
                        {"type": "text", "text": "• /task 清單 或 /任務 清單：查看進度與認領", "size": "xs", "color": "#475569", "margin": "xs", "wrap": True},
                        {"type": "text", "text": "• /claim 或 /認領 [編號]：認領指定任務", "size": "xs", "color": "#475569", "margin": "xs", "wrap": True}
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FEF2F2",
                    "paddingAll": "12px",
                    "cornerRadius": "8px",
                    "contents": [
                        {"type": "text", "text": "🎲 抽籤分工與名冊", "weight": "bold", "size": "sm", "color": "#991B1B"},
                        {"type": "text", "text": "• /roulette 或 /抽籤：優先抽無任務組員", "size": "xs", "color": "#B91C1C", "margin": "xs", "wrap": True},
                        {"type": "text", "text": "• /member 新增 或 /成員 新增 [名字]：手動加入組員", "size": "xs", "color": "#B91C1C", "margin": "xs", "wrap": True},
                        {"type": "text", "text": "• /member 或 /成員：查看成員分工現況", "size": "xs", "color": "#B91C1C", "margin": "xs", "wrap": True}
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#ECFDF5",
                    "paddingAll": "12px",
                    "cornerRadius": "8px",
                    "contents": [
                        {"type": "text", "text": "進度狀態與指南", "weight": "bold", "size": "sm", "color": "#065F46"},
                        {"type": "text", "text": "• /status 或 /狀態：查看各項任務認領狀況", "size": "xs", "color": "#047857", "margin": "xs", "wrap": True},
                        {"type": "text", "text": "• /常用指令說明 或 /help：隨時查看本說明", "size": "xs", "color": "#047857", "margin": "xs", "wrap": True}
                    ]
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
    """任務建立成功通知卡片（精簡標籤與版面）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F766E",
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
            "contents": [
                {
                    "type": "text",
                    "text": f"【{task_id}】{title}",
                    "weight": "bold",
                    "size": "md",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": description if description else "（無補充說明）",
                    "size": "xs",
                    "color": "#64748B",
                    "wrap": True
                },
                {"type": "separator"},
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "發起人", "size": "xs", "color": "#94A3B8"},
                        {"type": "text", "text": creator_name, "size": "xs", "color": "#334155", "align": "end", "wrap": True}
                    ]
                },
                {
                    "type": "text",
                    "text": "請組員主動認領，若無人認領可點選抽籤隨機分工。",
                    "size": "xs",
                    "color": "#EA580C",
                    "wrap": True
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "認領任務",
                        "text": f"/claim {task_id}"
                    },
                    "style": "primary",
                    "color": "#0F766E",
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
    """任務清單卡片（使用 giga 寬版尺寸與簡潔按鈕，確保字體絕不截斷）"""
    if not tasks:
        item_boxes = [{
            "type": "text",
            "text": "目前這組還沒有任何待辦任務，大家可以輕鬆一下！",
            "size": "sm",
            "color": "#64748B",
            "align": "center",
            "margin": "lg"
        }]
        footer_box = {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "12px",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "瀏覽分工範本",
                        "text": "/task 範本"
                    },
                    "style": "primary",
                    "color": "#0F766E",
                    "height": "sm"
                }
            ]
        }
    else:
        item_boxes = []
        has_pending = False
        for t in tasks[:8]:  # 最多顯示 8 筆完整條目
            is_pending = (t.get("status") == "pending")
            task_id = t.get("id", "T000")
            title = t.get("title", "")
            
            if is_pending:
                has_pending = True
                # 待認領：提供 2 字「認領」按鈕，左邊 flex 8，右邊 flex 3，絕不裁切
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
                                    "color": "#0F172A",
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "尚未認領",
                                    "size": "xxs",
                                    "color": "#EA580C"
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
                            "color": "#0F766E",
                            "height": "sm",
                            "flex": 3
                        }
                    ]
                })
            else:
                # 已認領：顯示負責人
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
                                    "color": "#475569",
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
                                    "color": "#0F766E",
                                    "align": "end",
                                    "weight": "bold",
                                    "wrap": True
                                }
                            ]
                        }
                    ]
                })

        # 底部操作按鈕
        footer_buttons = [
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "新增分工範本",
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
                "color": "#DC2626",
                "height": "sm",
                "margin": "sm"
            })
            
        footer_box = {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "paddingAll": "12px",
            "contents": footer_buttons
        }

    bubble = {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#334155",
            "paddingAll": "16px",
            "contents": [
                {"type": "text", "text": "小組工作清單與認領現況", "weight": "bold", "color": "#FFFFFF", "size": "md"}
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "paddingAll": "16px",
            "contents": item_boxes
        },
        "footer": footer_box
    }
    return FlexMessage(
        alt_text="小組工作清單與認領現況",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )


def create_roulette_flex(task_id: str, task_title: str, victim_name: str) -> FlexMessage:
    """隨機指派抽籤卡片（文字精簡置中）"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0284C7",
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
            "contents": [
                {
                    "type": "text",
                    "text": "由你負責：",
                    "size": "xs",
                    "color": "#64748B",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": victim_name,
                    "weight": "bold",
                    "size": "xl",
                    "color": "#0284C7",
                    "align": "center",
                    "wrap": True
                },
                {"type": "separator"},
                {
                    "type": "text",
                    "text": f"抽籤任務：【{task_id}】{task_title}",
                    "size": "sm",
                    "color": "#334155",
                    "wrap": True,
                    "weight": "bold"
                },
                {
                    "type": "text",
                    "text": "辛苦了！有問題隨時在群組討論。",
                    "size": "xs",
                    "color": "#64748B",
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
