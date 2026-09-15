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
        QuickReplyItem(action=MessageAction(label="⚡ 常用分工範本", text="/task 範本")),
        QuickReplyItem(action=MessageAction(label="📋 任務清單", text="/task 清單")),
        QuickReplyItem(action=MessageAction(label="🎲 抽籤分工", text="/roulette")),
        QuickReplyItem(action=MessageAction(label="📊 專案進度", text="/status")),
        QuickReplyItem(action=MessageAction(label="📖 使用指南", text="/help")),
    ])

def create_preset_tasks_carousel() -> FlexMessage:
    """常見小組專案工作範本輪播卡片（不用使用者自己打字，直接一鍵按鈕建立）"""
    carousel_contents = [
        # 卡片 1：簡報製作
        {
            "type": "bubble",
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#0F766E",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "📊 簡報製作與美編", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#0F172A"},
                    {"type": "text", "text": "• 統整各組員文字與圖表\n• PPT / Canva 視覺美化排版\n• 整理報告講稿備忘錄", "size": "xs", "color": "#64748B", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "➕ 建立此任務",
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
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#0284C7",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "🎤 上台口頭報告", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#0F172A"},
                    {"type": "text", "text": "• 掌握全組報告架構與脈絡\n• 代表小組進行上台口頭發表\n• 現場教授與同學提問 Q&A 應答", "size": "xs", "color": "#64748B", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "➕ 建立此任務",
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
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#7C3AED",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "🔍 文獻查證與資料蒐集", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#0F172A"},
                    {"type": "text", "text": "• 前期相關主題論文/資料調研\n• 競品案例分析與背景研究\n• 驗證數據來源與文獻整理", "size": "xs", "color": "#64748B", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "➕ 建立此任務",
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
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#D97706",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "📝 書面報告撰寫統整", "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {"type": "text", "text": "負責項目：", "weight": "bold", "size": "xs", "color": "#0F172A"},
                    {"type": "text", "text": "• 彙整各章節文字與圖表\n• 校對格式、目錄與參考文獻\n• 產出期末正式 Word / PDF 報告", "size": "xs", "color": "#64748B", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "➕ 建立此任務",
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
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#1E293B",
                "paddingAll": "16px",
                "contents": [
                    {"type": "text", "text": "⚡ 一鍵全套分工", "weight": "bold", "color": "#38BDF8", "size": "md"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {"type": "text", "text": "組長省時首選！", "weight": "bold", "size": "sm", "color": "#0F172A"},
                    {"type": "text", "text": "直接一次建立以上 4 項小組標準分工（簡報、報告、資料、書面），全組立刻開搶認領！", "size": "xs", "color": "#64748B", "wrap": True}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "🚀 一鍵建立全部",
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
        alt_text="⚡ 小組專案常用分工範本（可直接點擊建立）",
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
                    "text": "📋【組長保險】專案協作功能選單",
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
                            "text": "⚡ 專案工作分工（不用手打字）",
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
                                        "label": "⚡ 常用分工範本",
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
                                        "label": "📋 查看任務清單",
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
                            "text": "🎲 隨機抽籤分工（不用組長當壞人）",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#991B1B"
                        },
                        {
                            "type": "text",
                            "text": "卡關沒人認領的工作？直接交給系統隨機抽籤，公平又省事。",
                            "size": "xs",
                            "color": "#B91C1C",
                            "margin": "xs",
                            "wrap": True
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "🎲 抽籤決定人選",
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
                            "text": "📊 專案狀況與使用說明",
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
                                        "label": "📊 當前進度",
                                        "text": "/status"
                                    },
                                    "style": "secondary",
                                    "height": "sm"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "📖 常用指令",
                                        "text": "/help"
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
        alt_text="📋【組長保險】專案協作功能選單",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )


def create_help_flex() -> FlexMessage:
    """操作指南 Flex 卡片"""
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
                    "text": "📖 組長保險・常用指令說明",
                    "weight": "bold",
                    "color": "#F8FAFC",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": "專案溝通不尷尬，工作認領與進度一次搞定",
                    "color": "#94A3B8",
                    "size": "xs",
                    "margin": "sm"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#F8FAFC",
                    "paddingAll": "12px",
                    "cornerRadius": "8px",
                    "contents": [
                        {"type": "text", "text": "📌 任務建立與認領", "weight": "bold", "size": "sm", "color": "#0F172A"},
                        {"type": "text", "text": "• /task 範本：瀏覽常見專案工作一鍵建立", "size": "xs", "color": "#0284C7", "weight": "bold", "margin": "xs"},
                        {"type": "text", "text": "• /task 新增 [名稱] [說明]：自訂待辦工作", "size": "xs", "color": "#475569"},
                        {"type": "text", "text": "• /task 清單：查看目前大家的進度（附一鍵認領）", "size": "xs", "color": "#475569"},
                        {"type": "text", "text": "• /claim [任務編號]：主動認領負責項目", "size": "xs", "color": "#475569"}
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FEF2F2",
                    "paddingAll": "12px",
                    "cornerRadius": "8px",
                    "contents": [
                        {"type": "text", "text": "🎲 抽籤分工", "weight": "bold", "size": "sm", "color": "#991B1B"},
                        {"type": "text", "text": "• /roulette 或 /抽籤：沒人認領的工作，讓系統隨機分配。", "size": "xs", "color": "#B91C1C", "margin": "xs"}
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#ECFDF5",
                    "paddingAll": "12px",
                    "cornerRadius": "8px",
                    "contents": [
                        {"type": "text", "text": "📊 貢獻度與狀態", "weight": "bold", "size": "sm", "color": "#065F46"},
                        {"type": "text", "text": "• /status：查看群組目前已認領與未認領件數", "size": "xs", "color": "#047857", "margin": "xs"}
                    ]
                }
            ]
        }
    }
    return FlexMessage(
        alt_text="📖 組長保險・常用指令說明",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )


def create_task_created_flex(task_id: str, title: str, description: str, creator_name: str) -> FlexMessage:
    """任務建立成功通知卡片"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0F766E",
            "contents": [
                {
                    "type": "text",
                    "text": "📌 新增小組任務",
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
            "contents": [
                {
                    "type": "text",
                    "text": f"【{task_id}】{title}",
                    "weight": "bold",
                    "size": "lg",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": description if description else "（無補充說明）",
                    "size": "sm",
                    "color": "#64748B",
                    "wrap": True
                },
                {"type": "separator"},
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {"type": "text", "text": "發起人", "size": "xs", "color": "#94A3B8"},
                        {"type": "text", "text": creator_name, "size": "xs", "color": "#334155", "align": "end"}
                    ]
                },
                {
                    "type": "text",
                    "text": "大家記得來認領～如果一直沒人認領，可以使用抽籤隨機分配喔！",
                    "size": "xs",
                    "color": "#EA580C",
                    "wrap": True
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": f"🙋 我來負責 ({task_id})",
                        "text": f"/claim {task_id}"
                    },
                    "style": "primary",
                    "color": "#0F766E"
                }
            ]
        }
    }
    return FlexMessage(
        alt_text=f"📌 新任務待認領：{title}",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )


def create_task_list_flex(tasks: list) -> FlexMessage:
    """任務清單卡片（每筆待認領項目皆附帶直接按鈕，點擊即認領）"""
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
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "⚡ 瀏覽常見分工範本",
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
                # 待認領：提供小巧的「我來負責」直接點擊按鈕
                item_boxes.append({
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "md",
                    "alignItems": "center",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 7,
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
                                    "text": "⏳ 尚未認領",
                                    "size": "xxs",
                                    "color": "#EA580C"
                                }
                            ]
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "🙋 我負責",
                                "text": f"/claim {task_id}"
                            },
                            "style": "primary",
                            "color": "#0F766E",
                            "height": "sm",
                            "flex": 4
                        }
                    ]
                })
            else:
                # 已認領：顯示綠色徽章與負責人
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
                            "flex": 7,
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
                            "flex": 4,
                            "contents": [
                                {
                                    "type": "text",
                                    "text": f"✅ {assignee_name}",
                                    "size": "xs",
                                    "color": "#10B981",
                                    "align": "end",
                                    "weight": "bold"
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
                    "label": "⚡ 新增更多工作範本",
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
                    "label": "🎲 抽籤決定未認領工作",
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
            "contents": footer_buttons
        }

    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#334155",
            "contents": [
                {"type": "text", "text": "📋 小組工作清單與認領現況", "weight": "bold", "color": "#FFFFFF", "size": "md"}
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": item_boxes
        },
        "footer": footer_box
    }
    return FlexMessage(
        alt_text="📋 小組工作清單與認領現況",
        contents=FlexContainer.from_dict(bubble),
        quick_reply=get_main_quick_reply()
    )


def create_roulette_flex(task_id: str, task_title: str, victim_name: str) -> FlexMessage:
    """隨機指派抽籤卡片"""
    bubble = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": "#0284C7",
            "contents": [
                {"type": "text", "text": "🎲 隨機抽籤分工結果", "weight": "bold", "color": "#FFFFFF", "size": "lg", "align": "center"}
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
                {
                    "type": "text",
                    "text": "🎯 這次由你負責：",
                    "size": "sm",
                    "color": "#64748B",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": f"👉 {victim_name}",
                    "weight": "bold",
                    "size": "xxl",
                    "color": "#0284C7",
                    "align": "center"
                },
                {"type": "separator"},
                {
                    "type": "text",
                    "text": f"這項工作全組還沒人認領，系統抽籤決定由你負責【{task_id}：{task_title}】囉！",
                    "size": "sm",
                    "color": "#334155",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": "辛苦了！有問題隨時在群組提出，大家一起分工搞定 💪",
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
