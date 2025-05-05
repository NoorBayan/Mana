
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
import pandas as pd
import os
import traceback
import json
# ================================================
# 1. Hierarchical data structure (the complete dictionary)
# ================================================

poetry_topics_tree_complete = {
    "1": {
        "id": "1", "arabic_name": "العواطف والمشاعر", "english_name": "Emotions and Feelings",
        "children": {
            "1.1": {
                "id": "1.1", "arabic_name": "الحب والشغف", "english_name": "Love and Passion",
                "children": {
                    "1.1.1": {"id": "1.1.1", "arabic_name": "التعبير عن الحب (الغزل العاطفي)", "english_name": "Expression of Love - Emotional Ghazal", "children": {}},
                    "1.1.2": {"id": "1.1.2", "arabic_name": "الشوق والحنين (إلى الحبيب/الماضي)", "english_name": "Longing and Nostalgia - for Beloved/Past", "children": {}},
                    "1.1.3": {"id": "1.1.3", "arabic_name": "الهيام والوله (العشق الشديد)", "english_name": "Deep Love and Infatuation", "children": {}},
                    "1.1.4": {"id": "1.1.4", "arabic_name": "الألفة والمودة", "english_name": "Affection and Familiarity", "children": {}},
                    "1.1.5": {"id": "1.1.5", "arabic_name": "عذاب الحب وألمه", "english_name": "Torment and Pain of Love", "description": "يشمل الهجر، الفراق العاطفي، اللوعة.", "children": {}},
                    "1.1.6": {"id": "1.1.6", "arabic_name": "الغيرة", "english_name": "Jealousy", "children": {}},
                    "1.1.7": {"id": "1.1.7", "arabic_name": "الرغبة الحسية (ضمن سياق الحب)", "english_name": "Sensual Desire - within Love context", "children": {}}
                }
            },
            "1.2": {
                "id": "1.2", "arabic_name": "الحزن والأسى", "english_name": "Sadness and Sorrow",
                "children": {
                    "1.2.1": {"id": "1.2.1", "arabic_name": "الحزن العام والأسى", "english_name": "General Sadness and Grief", "description": "يشمل الحسرة، الكآبة.", "children": {}},
                    "1.2.2": {"id": "1.2.2", "arabic_name": "ألم الفقد والخسارة", "english_name": "Pain of Loss and Bereavement", "description": "مرتبط بالموت أو الفقد الدائم.", "children": {}},
                    "1.2.3": {"id": "1.2.3", "arabic_name": "الشعور بالهجر والترك", "english_name": "Feeling of Abandonment and Rejection", "children": {}},
                    "1.2.4": {"id": "1.2.4", "arabic_name": "الأسف والندم", "english_name": "Regret and Remorse", "description": "مرتبط بالأخطاء أو الفرص الضائعة.", "children": {}}
                }
            },
            "1.3": {
                "id": "1.3", "arabic_name": "الأمل والرجاء", "english_name": "Hope and Supplication",
                "children": {
                    "1.3.1": {"id": "1.3.1", "arabic_name": "الأمل العام والتفاؤل", "english_name": "General Hope and Optimism", "children": {}},
                    "1.3.2": {"id": "1.3.2", "arabic_name": "الرجاء (خاصة الديني أو المرتبط بالآخرين)", "english_name": "Supplication/Hoping - esp. Religious/Interpersonal", "children": {}},
                    "1.3.3": {"id": "1.3.3", "arabic_name": "الأمل باللقاء أو الوصال", "english_name": "Hope for Union or Meeting", "children": {}},
                    "1.3.4": {"id": "1.3.4", "arabic_name": "التضرع والدعاء (كتعبير عاطفي)", "english_name": "Supplication and Prayer - emotional expression", "children": {}}
                }
            },
            "1.4": {
                "id": "1.4", "arabic_name": "اليأس والإحباط", "english_name": "Despair and Frustration",
                "children": {
                    "1.4.1": {"id": "1.4.1", "arabic_name": "اليأس والقنوط", "english_name": "General Despair and Despondency", "children": {}},
                    "1.4.2": {"id": "1.4.2", "arabic_name": "الإحباط وخيبة الأمل", "english_name": "Frustration and Disappointment", "children": {}},
                    "1.4.3": {"id": "1.4.3", "arabic_name": "الشعور بالعبثية واللاجدوى", "english_name": "Feeling of Absurdity and Futility", "children": {}}
                }
            },
            "1.5": {
                "id": "1.5", "arabic_name": "الفرح والسرور", "english_name": "Joy and Happiness",
                "children": {
                    "1.5.1": {"id": "1.5.1", "arabic_name": "الفرح العام والبهجة", "english_name": "General Joy and Delight", "children": {}},
                    "1.5.2": {"id": "1.5.2", "arabic_name": "السعادة باللقاء أو الوصال", "english_name": "Happiness in Union or Meeting", "children": {}},
                    "1.5.3": {"id": "1.5.3", "arabic_name": "الابتهاج بالمناسبات أو الإنجازات", "english_name": "Rejoicing in Occasions/Achievements", "children": {}},
                    "1.5.4": {"id": "1.5.4", "arabic_name": "النشوة والوجد", "english_name": "Ecstasy/Euphoria - related to joy", "children": {}}
                }
            },
            "1.6": {
                "id": "1.6", "arabic_name": "الخوف والقلق", "english_name": "Fear and Anxiety",
                "children": {
                    "1.6.1": {"id": "1.6.1", "arabic_name": "الخوف العام والقلق", "english_name": "General Fear and Anxiety", "children": {}},
                    "1.6.2": {"id": "1.6.2", "arabic_name": "الخوف من الموت أو المصير", "english_name": "Fear of Death or Fate", "children": {}},
                    "1.6.3": {"id": "1.6.3", "arabic_name": "الخوف من الفقد أو الهجر", "english_name": "Fear of Loss or Abandonment", "children": {}},
                    "1.6.4": {"id": "1.6.4", "arabic_name": "الرهبة والخشية", "english_name": "Awe and Trepidation", "description": "قد تكون دينية أو مرتبطة بعظمة.", "children": {}}
                }
            },
            "1.7": {
                "id": "1.7", "arabic_name": "الغضب والاستياء", "english_name": "Anger and Resentment",
                "children": {
                    "1.7.1": {"id": "1.7.1", "arabic_name": "الغضب والسخط", "english_name": "Anger and Discontent", "children": {}},
                    "1.7.2": {"id": "1.7.2", "arabic_name": "الاستياء والتذمر والشكوى", "english_name": "Resentment, Grumbling, Complaint", "description": "شكوى عاطفية.", "children": {}}
                }
            },
            "1.8": {
                "id": "1.8", "arabic_name": "مشاعر أخرى", "english_name": "Other Emotions",
                "children": {
                    "1.8.1": {"id": "1.8.1", "arabic_name": "الحيرة والارتباك", "english_name": "Confusion and Perplexity", "children": {}},
                    "1.8.2": {"id": "1.8.2", "arabic_name": "الشجاعة (كحالة شعورية)", "english_name": "Courage - as an emotional state", "children": {}},
                    "1.8.3": {"id": "1.8.3", "arabic_name": "الاطمئنان والسكينة", "english_name": "Contentment and Tranquility", "children": {}},
                    "1.8.4": {"id": "1.8.4", "arabic_name": "الكبرياء والعزة (كحالة شعورية)", "english_name": "Pride and Dignity - as an emotional state", "children": {}},
                    "1.8.5": {"id": "1.8.5", "arabic_name": "التواضع والخضوع (كحالة شعورية)", "english_name": "Humility and Submission - as an emotional state", "children": {}}
                }
            }
        }
    },
    "2": {
        "id": "2", "arabic_name": "المقاصد والوظائف الشعرية", "english_name": "Poetic Intents and Functions",
        "children": {
            "2.1": {
                "id": "2.1", "arabic_name": "المدح", "english_name": "Praise - Madih",
                "children": {
                    "2.1.1": {"id": "2.1.1", "arabic_name": "مدح الأشخاص (ذوي السلطة، الأولياء، الأحباء)", "english_name": "Praising People - Rulers, Saints, Loved ones", "children": {}},
                    "2.1.2": {
                        "id": "2.1.2", "arabic_name": "مدح القيم والمثل العليا", "english_name": "Praising Values and Ideals",
                        "children": {
                            "2.1.2.1": {"id": "2.1.2.1", "arabic_name": "مدح الكرم", "english_name": "Praising Generosity", "children": {}},
                            "2.1.2.2": {"id": "2.1.2.2", "arabic_name": "مدح الشجاعة", "english_name": "Praising Courage", "children": {}},
                            "2.1.2.3": {"id": "2.1.2.3", "arabic_name": "مدح العدل", "english_name": "Praising Justice", "children": {}},
                            "2.1.2.4": {"id": "2.1.2.4", "arabic_name": "مدح الوفاء", "english_name": "Praising Loyalty", "children": {}},
                            "2.1.2.5": {"id": "2.1.2.5", "arabic_name": "مدح الحلم والصبر", "english_name": "Praising Forbearance/Patience", "children": {}},
                            "2.1.2.6": {"id": "2.1.2.6", "arabic_name": "مدح العفة", "english_name": "Praising Chastity", "children": {}},
                            "2.1.2.7": {"id": "2.1.2.7", "arabic_name": "مدح قيم أخرى", "english_name": "Praising Other Values", "children": {}}
                        }
                    },
                    "2.1.3": {"id": "2.1.3", "arabic_name": "مدح الأماكن أو الجماعات", "english_name": "Praising Places or Groups", "children": {}},
                    "2.1.4": {"id": "2.1.4", "arabic_name": "التهنئة", "english_name": "Congratulation - Tahni'a", "children": {}}
                }
            },
            "2.2": {
                "id": "2.2", "arabic_name": "الفخر", "english_name": "Boasting/Pride - Fakhr",
                "children": {
                    "2.2.1": {"id": "2.2.1", "arabic_name": "الفخر الذاتي (بالنفس، بالشعر، بالقدرات)", "english_name": "Self-Pride - in self, poetry, abilities", "children": {}},
                    "2.2.2": {"id": "2.2.2", "arabic_name": "الفخر الجماعي (بالقبيلة، بالأمة، بالعائلة)", "english_name": "Collective Pride - tribal, national, familial", "children": {}},
                    "2.2.3": {"id": "2.2.3", "arabic_name": "الفخر بالقيم أو الانتماء", "english_name": "Pride in Values or Belonging", "children": {}}
                }
            },
            "2.3": {
                "id": "2.3", "arabic_name": "الهجاء", "english_name": "Satire/Invective - Hija'",
                "children": {
                    "2.3.1": {"id": "2.3.1", "arabic_name": "هجاء الأشخاص (أعداء، بخلاء، جبناء)", "english_name": "Satirizing People", "children": {}},
                    "2.3.2": {"id": "2.3.2", "arabic_name": "هجاء الصفات أو الظواهر السلبية", "english_name": "Satirizing Negative Traits or Phenomena", "children": {}},
                    "2.3.3": {"id": "2.3.3", "arabic_name": "الهجاء الاجتماعي أو السياسي", "english_name": "Social or Political Satire", "children": {}},
                    "2.3.4": {"id": "2.3.4", "arabic_name": "السخرية والتهكم", "english_name": "Sarcasm and Mockery", "children": {}}
                }
            },
            "2.4": {
                "id": "2.4", "arabic_name": "الرثاء والتأبين", "english_name": "Elegy and Eulogy - Ritha'",
                "children": {
                    "2.4.1": {"id": "2.4.1", "arabic_name": "رثاء الأشخاص", "english_name": "Lamenting People", "children": {}},
                    "2.4.2": {"id": "2.4.2", "arabic_name": "رثاء المدن أو الأمجاد الزائلة", "english_name": "Lamenting Cities or Lost Glories", "children": {}},
                    "2.4.3": {"id": "2.4.3", "arabic_name": "الرثاء الذاتي أو رثاء الحال", "english_name": "Self-Lamentation or Lamenting the State of Affairs", "children": {}},
                    "2.4.4": {"id": "2.4.4", "arabic_name": "التأبين وذكر المناقب", "english_name": "Eulogy and Recounting Virtues", "children": {}}
                }
            },
            "2.5": {
                "id": "2.5", "arabic_name": "الغزل", "english_name": "Love Poetry/Expression - Ghazal",
                "children": {
                    "2.5.1": {"id": "2.5.1", "arabic_name": "الغزل العذري (التركيز على المشاعر الطاهرة والمعاناة)", "english_name": "Platonic Love Poetry - Udhri", "children": {}},
                    "2.5.2": {"id": "2.5.2", "arabic_name": "الغزل الحسي (التركيز على الجمال الجسدي والرغبة)", "english_name": "Sensual Love Poetry - Hissi", "children": {}},
                    "2.5.3": {"id": "2.5.3", "arabic_name": "النسيب (المقدمة الغزلية/الطللية التقليدية)", "english_name": "Nasib - Traditional prelude", "children": {}}
                }
            },
            "2.6": {
                "id": "2.6", "arabic_name": "الحكمة والموعظة", "english_name": "Wisdom and Admonition - Hikma/Wa'dh",
                "children": {
                    "2.6.1": {"id": "2.6.1", "arabic_name": "تقديم الحكم والتجارب الحياتية", "english_name": "Presenting Wisdom and Life Experiences", "children": {}},
                    "2.6.2": {"id": "2.6.2", "arabic_name": "الموعظة والإرشاد الأخلاقي أو الديني", "english_name": "Admonition and Moral/Religious Guidance", "children": {}},
                    "2.6.3": {"id": "2.6.3", "arabic_name": "النصح والتوجيه", "english_name": "Advice and Guidance", "children": {}}
                }
            },
            "2.7": {
                "id": "2.7", "arabic_name": "الشكوى والتظلم", "english_name": "Complaint and Grievance - Shakwa",
                "children": {
                    "2.7.1": {"id": "2.7.1", "arabic_name": "الشكوى من الزمن أو الدهر", "english_name": "Complaining about Time or Fate", "children": {}},
                    "2.7.2": {"id": "2.7.2", "arabic_name": "الشكوى من الظلم (الاجتماعي أو السياسي)", "english_name": "Complaining about Injustice - social/political", "children": {}},
                    "2.7.3": {"id": "2.7.3", "arabic_name": "الشكوى من الهجر أو الصد", "english_name": "Complaining about Abandonment or Rejection", "description": "شكوى كفعل.", "children": {}}
                }
            },
            "2.8": {
                "id": "2.8", "arabic_name": "الاعتذار والاستعطاف", "english_name": "Apology and Appeasement - I'tidhar/Isti'taf",
                "children": {
                    "2.8.1": {"id": "2.8.1", "arabic_name": "تقديم الاعتذار المباشر", "english_name": "Offering a Direct Apology", "children": {}},
                    "2.8.2": {"id": "2.8.2", "arabic_name": "الاستعطاف وطلب الصفح أو الرضا", "english_name": "Appeasement and Seeking Forgiveness/Favor", "children": {}}
                }
            },
            "2.9": {
                "id": "2.9", "arabic_name": "الطلب والدعاء", "english_name": "Request and Prayer - Talab/Du'a",
                "children": {
                    "2.9.1": {"id": "2.9.1", "arabic_name": "طلب العون أو الحاجة المادية أو المعنوية", "english_name": "Requesting Help or Needs", "children": {}},
                    "2.9.2": {"id": "2.9.2", "arabic_name": "الدعاء والتوسل (إلى الله أو الأولياء)", "english_name": "Prayer and Supplication - to God or Saints", "children": {}},
                    "2.9.3": {"id": "2.9.3", "arabic_name": "الاستغاثة", "english_name": "Plea for Help", "children": {}}
                }
            },
            "2.10": {
                "id": "2.10", "arabic_name": "الوصف (كغاية أساسية)", "english_name": "Description - as a primary goal - Wasf",
                "children": {
                    "2.10.1": {"id": "2.10.1", "arabic_name": "الوصف الحسي الدقيق (للطبيعة، الأشخاص، الأشياء)", "english_name": "Detailed Sensory Description", "children": {}},
                    "2.10.2": {"id": "2.10.2", "arabic_name": "الوصف الحركي أو السردي (لوقائع، رحلات، أحداث)", "english_name": "Dynamic or Narrative Description", "children": {}}
                }
            },
            "2.11": {
                "id": "2.11", "arabic_name": "أغراض أخرى", "english_name": "Other Intents/Functions",
                "children": {
                    "2.11.1": {"id": "2.11.1", "arabic_name": "الإخبار والتقرير", "english_name": "Reporting and Informing", "children": {}},
                    "2.11.2": {"id": "2.11.2", "arabic_name": "التبرير والتعليل", "english_name": "Justification and Reasoning", "children": {}},
                    "2.11.3": {"id": "2.11.3", "arabic_name": "الحوار والمناظرة", "english_name": "Dialogue and Debate", "children": {}},
                    "2.11.4": {"id": "2.11.4", "arabic_name": "التهديد والوعيد", "english_name": "Threat and Warning", "children": {}},
                    "2.11.5": {"id": "2.11.5", "arabic_name": "الإثارة والتشويق", "english_name": "Evocation and Suspense", "children": {}},
                    "2.11.6": {"id": "2.11.6", "arabic_name": "الألغاز والأحاجي", "english_name": "Riddles and Puzzles - Alghaz", "children": {}},
                    "2.11.7": {"id": "2.11.7", "arabic_name": "التعليم (بمعنى نقل معرفة محددة كالفقه أو النحو)", "english_name": "Didactic - transmitting specific knowledge", "children": {}}
                }
            }
        }
    },
    "3": {
        "id": "3", "arabic_name": "المفاهيم والتأملات", "english_name": "Concepts and Reflections",
        "children": {
            "3.1": {
                "id": "3.1", "arabic_name": "الدين والعقيدة", "english_name": "Religion and Belief",
                "children": {
                    "3.1.1": {"id": "3.1.1", "arabic_name": "الإيمان والتوحيد واليقين", "english_name": "Faith, Monotheism, Certainty", "children": {}},
                    "3.1.2": {"id": "3.1.2", "arabic_name": "العبادة والتقوى", "english_name": "Worship and Piety", "children": {}},
                    "3.1.3": {"id": "3.1.3", "arabic_name": "التصوف والعرفان", "english_name": "Sufism and Gnosticism", "children": {}},
                    "3.1.4": {
                        "id": "3.1.4", "arabic_name": "الآخرة والجزاء", "english_name": "Afterlife and Recompense",
                        "children": {
                            "3.1.4.1": {"id": "3.1.4.1", "arabic_name": "الجنة ونعيمها", "english_name": "Paradise and its Bliss", "children": {}},
                            "3.1.4.2": {"id": "3.1.4.2", "arabic_name": "النار وعذابها", "english_name": "Hell and its Torment", "children": {}},
                            "3.1.4.3": {"id": "3.1.4.3", "arabic_name": "الحساب والبعث", "english_name": "Reckoning and Resurrection", "children": {}}
                        }
                    },
                    "3.1.5": {"id": "3.1.5", "arabic_name": "القضاء والقدر (الإيمان به والتسليم)", "english_name": "Fate and Destiny - belief/submission", "children": {}},
                    "3.1.6": {"id": "3.1.6", "arabic_name": "النبوات والرسالات والشخصيات الدينية", "english_name": "Prophethood, Messages, Religious Figures", "children": {}},
                    "3.1.7": {"id": "3.1.7", "arabic_name": "الشريعة والأحكام الدينية", "english_name": "Religious Law and Rulings", "children": {}},
                    "3.1.8": {"id": "3.1.8", "arabic_name": "الزهد والورع", "english_name": "Asceticism and Piety - Zuhd", "children": {}}
                }
            },
            "3.2": {
                "id": "3.2", "arabic_name": "الفلسفة والوجود", "english_name": "Philosophy and Existence",
                "children": {
                    "3.2.1": {"id": "3.2.1", "arabic_name": "تأملات وجودية (في الحياة والموت والزمن)", "english_name": "Existential Reflections - Life, Death, Time", "children": {}},
                    "3.2.2": {"id": "3.2.2", "arabic_name": "البحث عن الحقيقة والمعنى", "english_name": "Search for Truth and Meaning", "children": {}},
                    "3.2.3": {"id": "3.2.3", "arabic_name": "تأملات في طبيعة الوجود والعدم", "english_name": "Reflections on Being and Nothingness", "children": {}},
                    "3.2.4": {"id": "3.2.4", "arabic_name": "العقل والمنطق", "english_name": "Reason and Logic", "children": {}}
                }
            },
            "3.3": {
                "id": "3.3", "arabic_name": "الأخلاق والقيم", "english_name": "Ethics and Values",
                "children": {
                    "3.3.1": {
                        "id": "3.3.1", "arabic_name": "القيم الأخلاقية العليا", "english_name": "Core Ethical Values",
                        "children": {
                            "3.3.1.1": {"id": "3.3.1.1", "arabic_name": "الكرم والجود", "english_name": "Generosity and Munificence", "children": {}},
                            "3.3.1.2": {"id": "3.3.1.2", "arabic_name": "الشجاعة والإقدام", "english_name": "Courage and Bravery", "children": {}},
                            "3.3.1.3": {"id": "3.3.1.3", "arabic_name": "الوفاء والإخلاص", "english_name": "Loyalty and Sincerity", "children": {}},
                            "3.3.1.4": {"id": "3.3.1.4", "arabic_name": "الصبر والتحمل", "english_name": "Patience and Endurance", "children": {}},
                            "3.3.1.5": {"id": "3.3.1.5", "arabic_name": "العفة والنزاهة", "english_name": "Chastity and Integrity", "children": {}},
                            "3.3.1.6": {"id": "3.3.1.6", "arabic_name": "العدل والإنصاف", "english_name": "Justice and Fairness", "children": {}},
                            "3.3.1.7": {"id": "3.3.1.7", "arabic_name": "قيم أخلاقية أخرى", "english_name": "Other Ethical Values", "children": {}}
                        }
                    },
                    "3.3.2": {"id": "3.3.2", "arabic_name": "الصراع بين الحق والباطل", "english_name": "Conflict between Right and Wrong/Truth and Falsehood", "children": {}},
                    "3.3.3": {"id": "3.3.3", "arabic_name": "الآداب الاجتماعية", "english_name": "Social Etiquette", "description": "مثل آداب الشرب، الجوار.", "children": {}}
                }
            },
            "3.4": {
                "id": "3.4", "arabic_name": "المعرفة والعلم", "english_name": "Knowledge and Science",
                "children": {
                    "3.4.1": {"id": "3.4.1", "arabic_name": "قيمة العلم والمعرفة والعلماء", "english_name": "Value of Knowledge, Science, Scholars", "children": {}},
                    "3.4.2": {"id": "3.4.2", "arabic_name": "طلب العلم والسعي للمعرفة", "english_name": "Seeking Knowledge", "children": {}},
                    "3.4.3": {"id": "3.4.3", "arabic_name": "التعليم والإرشاد المعرفي", "english_name": "Education and Intellectual Guidance", "children": {}},
                    "3.4.4": {"id": "3.4.4", "arabic_name": "الكتب والقراءة والكتابة", "english_name": "Books, Reading, Writing", "children": {}}
                }
            }
        }
    },
    "4": {
        "id": "4", "arabic_name": "الحياة الاجتماعية والسياسية", "english_name": "Social and Political Life",
        "children": {
            "4.1": {
                "id": "4.1", "arabic_name": "المجتمع والعلاقات", "english_name": "Society and Relationships",
                "children": {
                    "4.1.1": {"id": "4.1.1", "arabic_name": "نقد المجتمع (الظواهر السلبية، الطبقية، النفاق)", "english_name": "Social Critique - negative phenomena, classism, hypocrisy", "children": {}},
                    "4.1.2": {
                        "id": "4.1.2", "arabic_name": "العلاقات الإنسانية", "english_name": "Human Relations",
                        "children": {
                            "4.1.2.1": {"id": "4.1.2.1", "arabic_name": "الصداقة", "english_name": "Friendship", "children": {}},
                            "4.1.2.2": {"id": "4.1.2.2", "arabic_name": "الأخوة", "english_name": "Brotherhood", "children": {}},
                            "4.1.2.3": {"id": "4.1.2.3", "arabic_name": "الجوار", "english_name": "Neighborliness", "children": {}}
                        }
                    },
                    "4.1.3": {"id": "4.1.3", "arabic_name": "الأسرة والقرابة", "english_name": "Family and Kinship", "children": {}},
                    "4.1.4": {"id": "4.1.4", "arabic_name": "العادات والتقاليد والأعراف", "english_name": "Customs, Traditions, Norms", "children": {}}
                }
            },
            "4.2": {
                "id": "4.2", "arabic_name": "الوطن والانتماء", "english_name": "Homeland and Belonging",
                "children": {
                    "4.2.1": {"id": "4.2.1", "arabic_name": "حب الوطن والفخر به", "english_name": "Love and Pride for the Homeland", "children": {}},
                    "4.2.2": {"id": "4.2.2", "arabic_name": "الحنين إلى الوطن", "english_name": "Nostalgia for the Homeland", "children": {}},
                    "4.2.3": {"id": "4.2.3", "arabic_name": "الغربة والاغتراب", "english_name": "Exile and Alienation", "children": {}},
                    "4.2.4": {"id": "4.2.4", "arabic_name": "الهوية الوطنية/القومية", "english_name": "National/Ethnic Identity", "children": {}}
                }
            },
            "4.3": {
                "id": "4.3", "arabic_name": "السياسة والحكم", "english_name": "Politics and Governance",
                "children": {
                    "4.3.1": {"id": "4.3.1", "arabic_name": "العلاقة بالحاكم (مدحاً أو ذماً أو نصحاً)", "english_name": "Relationship with the Ruler - praise, blame, advice", "children": {}},
                    "4.3.2": {"id": "4.3.2", "arabic_name": "الظلم والاستبداد والطغيان", "english_name": "Oppression, Tyranny, Despotism", "children": {}},
                    "4.3.3": {"id": "4.3.3", "arabic_name": "العدل والحكم الرشيد", "english_name": "Justice and Good Governance", "children": {}},
                    "4.3.4": {"id": "4.3.4", "arabic_name": "الثورة والتمرد والمقاومة", "english_name": "Revolution, Rebellion, Resistance", "children": {}},
                    "4.3.5": {"id": "4.3.5", "arabic_name": "نقد الأوضاع السياسية", "english_name": "Critique of Political Situations", "children": {}}
                }
            },
            "4.4": {
                "id": "4.4", "arabic_name": "الحرب والصراع", "english_name": "War and Conflict",
                "children": {
                    "4.4.1": {"id": "4.4.1", "arabic_name": "وصف المعارك والقتال", "english_name": "Describing Battles and Fighting", "children": {}},
                    "4.4.2": {"id": "4.4.2", "arabic_name": "الحماسة والتحريض على القتال", "english_name": "Enthusiasm and Incitement to Fight", "children": {}},
                    "4.4.3": {"id": "4.4.3", "arabic_name": "ويلات الحرب ومآسيها", "english_name": "Woes and Tragedies of War", "children": {}},
                    "4.4.4": {"id": "4.4.4", "arabic_name": "السلم والصلح", "english_name": "Peace and Reconciliation", "children": {}},
                    "4.4.5": {"id": "4.4.5", "arabic_name": "الثأر والانتقام", "english_name": "Revenge and Vengeance", "children": {}}
                }
            }
        }
    },
    "5": {
        "id": "5", "arabic_name": "الذات والتجربة الشخصية", "english_name": "The Self and Personal Experience",
        "children": {
            "5.1": {
                "id": "5.1", "arabic_name": "الهوية والبحث عن الذات", "english_name": "Identity and Self-Discovery",
                "children": {
                    "5.1.1": {"id": "5.1.1", "arabic_name": "البحث عن الهوية أو المعنى الذاتي", "english_name": "Search for Identity or Self-Meaning", "children": {}},
                    "5.1.2": {"id": "5.1.2", "arabic_name": "الاغتراب الذاتي أو الضياع", "english_name": "Self-Alienation or Feeling Lost", "children": {}},
                    "5.1.3": {"id": "5.1.3", "arabic_name": "تحقيق الذات أو تجاوزها", "english_name": "Self-Actualization or Transcendence", "children": {}},
                    "5.1.4": {"id": "5.1.4", "arabic_name": "الصراع الداخلي", "english_name": "Internal Conflict", "children": {}}
                }
            },
            "5.2": {
                "id": "5.2", "arabic_name": "التجارب الشخصية", "english_name": "Personal Experiences",
                "children": {
                    "5.2.1": {"id": "5.2.1", "arabic_name": "الذكريات والأحلام", "english_name": "Memories and Dreams", "children": {}},
                    "5.2.2": {"id": "5.2.2", "arabic_name": "المعاناة الشخصية (المرض، الفقر، إلخ)", "english_name": "Personal Suffering - illness, poverty, etc.", "children": {}},
                    "5.2.3": {"id": "5.2.3", "arabic_name": "السيرة الذاتية أو الاعترافات", "english_name": "Autobiography or Confessions", "children": {}},
                    "5.2.4": {"id": "5.2.4", "arabic_name": "التجارب الروحية أو الصوفية الخاصة", "english_name": "Personal Spiritual/Sufi Experiences", "children": {}}
                }
            },
            "5.3": {
                "id": "5.3", "arabic_name": "مراحل العمر", "english_name": "Life Stages",
                "children": {
                    "5.3.1": {"id": "5.3.1", "arabic_name": "الشباب والصبا", "english_name": "Youth and Early Youth", "children": {}},
                    "5.3.2": {"id": "5.3.2", "arabic_name": "الشيخوخة والشيب", "english_name": "Old Age and Grey Hair", "children": {}}
                }
            }
        }
    },
    "6": {
        "id": "6", "arabic_name": "الطبيعة والعالم المادي", "english_name": "Nature and the Material World",
        "children": {
            "6.1": {
                "id": "6.1", "arabic_name": "عناصر الطبيعة", "english_name": "Elements of Nature",
                "children": {
                    "6.1.1": {"id": "6.1.1", "arabic_name": "الحيوان", "english_name": "Fauna", "children": {}},
                    "6.1.2": {"id": "6.1.2", "arabic_name": "النبات والزهر", "english_name": "Flora and Flowers", "children": {}},
                    "6.1.3": {
                        "id": "6.1.3", "arabic_name": "المناظر الطبيعية", "english_name": "Landscapes",
                        "children": {
                            "6.1.3.1": {"id": "6.1.3.1", "arabic_name": "الصحراء والبرية", "english_name": "Desert and Wilderness", "children": {}},
                            "6.1.3.2": {"id": "6.1.3.2", "arabic_name": "الرياض والحدائق والبساتين", "english_name": "Gardens and Orchards", "children": {}},
                            "6.1.3.3": {"id": "6.1.3.3", "arabic_name": "الجبال والتلال", "english_name": "Mountains and Hills", "children": {}},
                            "6.1.3.4": {"id": "6.1.3.4", "arabic_name": "الأنهار والجداول والعيون", "english_name": "Rivers, Streams, Springs", "children": {}},
                            "6.1.3.5": {"id": "6.1.3.5", "arabic_name": "البحر والشاطئ", "english_name": "Sea and Coast", "children": {}}
                        }
                    },
                    "6.1.4": {
                        "id": "6.1.4", "arabic_name": "الظواهر الكونية والفلكية", "english_name": "Cosmic and Astronomical Phenomena",
                        "children": {
                            "6.1.4.1": {"id": "6.1.4.1", "arabic_name": "الليل والظلام", "english_name": "Night and Darkness", "children": {}},
                            "6.1.4.2": {"id": "6.1.4.2", "arabic_name": "النهار والصباح والشروق والغروب", "english_name": "Day, Morning, Sunrise, Sunset", "children": {}},
                            "6.1.4.3": {"id": "6.1.4.3", "arabic_name": "النجوم والكواكب والأجرام السماوية", "english_name": "Stars, Planets, Celestial Bodies", "children": {}},
                            "6.1.4.4": {"id": "6.1.4.4", "arabic_name": "المطر والسحاب والبرق والرعد", "english_name": "Rain, Clouds, Lightning, Thunder", "children": {}},
                            "6.1.4.5": {"id": "6.1.4.5", "arabic_name": "الفصول (المواسم)", "english_name": "Seasons", "children": {}}
                        }
                    }
                }
            },
            "6.2": {
                "id": "6.2", "arabic_name": "الأماكن والأطلال", "english_name": "Places and Ruins",
                "children": {
                    "6.2.1": {"id": "6.2.1", "arabic_name": "الوقوف على الأطلال (الديار المهجورة)", "english_name": "Standing by the Ruins - Abandoned Abodes", "children": {}},
                    "6.2.2": {"id": "6.2.2", "arabic_name": "وصف المدن والقرى", "english_name": "Describing Cities and Villages", "children": {}},
                    "6.2.3": {"id": "6.2.3", "arabic_name": "وصف المباني والعمارة", "english_name": "Describing Buildings and Architecture", "children": {}}
                }
            },
            "6.3": {
                "id": "6.3", "arabic_name": "الأشياء والماديات", "english_name": "Objects and Material Things",
                "children": {
                    "6.3.1": {"id": "6.3.1", "arabic_name": "الأدوات والأشياء (أسلحة، أدوات كتابة، ملابس، حلي)", "english_name": "Tools and Objects - weapons, writing tools, clothes, jewelry", "children": {}},
                    "6.3.2": {"id": "6.3.2", "arabic_name": "الخمر (كوصف مادي أو لوني أو لرائحته)", "english_name": "Wine - material description", "children": {}},
                    "6.3.3": {"id": "6.3.3", "arabic_name": "الطعام والشراب", "english_name": "Food and Drink", "children": {}}
                }
            }
        }
    },
    "7": {
        "id": "7", "arabic_name": "ما وراء الشعر واللغة", "english_name": "Meta-Poetry and Language",
        "children": {
            "7.1": {
                "id": "7.1", "arabic_name": "عن الشعر", "english_name": "About Poetry",
                "children": {
                    "7.1.1": {"id": "7.1.1", "arabic_name": "طبيعة الشعر وأهميته وقدرته", "english_name": "Nature, Importance, Power of Poetry", "children": {}},
                    "7.1.2": {"id": "7.1.2", "arabic_name": "عملية الإبداع الشعري والإلهام", "english_name": "The Poetic Creative Process and Inspiration", "children": {}},
                    "7.1.3": {"id": "7.1.3", "arabic_name": "نقد الشعر والشعراء", "english_name": "Criticism of Poetry and Poets", "children": {}},
                    "7.1.4": {"id": "7.1.4", "arabic_name": "الفخر بالشعر والقدرة الشعرية", "english_name": "Pride in Poetry and Poetic Ability", "children": {}}
                }
            },
            "7.2": {
                "id": "7.2", "arabic_name": "عن اللغة", "english_name": "About Language",
                "children": {
                    "7.2.1": {"id": "7.2.1", "arabic_name": "اللغة والبيان والبلاغة", "english_name": "Language, Expression, Rhetoric", "children": {}},
                    "7.2.2": {"id": "7.2.2", "arabic_name": "الأسلوب والأوزان والقوافي", "english_name": "Style, Meter, Rhyme", "children": {}}
                }
            }
        }
    }
}




# ================================================
# HTML generation function (version that uses names and saves the file)
# ================================================
def generate_poem_html(title, poet, era, theme_ids, theme_names, percentages, verses):
    # Ensure the number of names, IDs, and ratios match
    if not (len(theme_ids) == len(theme_names) == len(percentages)):
        print("Warning: Mismatch between theme IDs, names, and percentages. Chart might be incorrect.")
        theme_names_json = json.dumps([])
        percentages_json = json.dumps([])
    else:
        try:
            theme_names_json = json.dumps(theme_names, ensure_ascii=False)
            percentages_json = json.dumps(percentages)
        except TypeError as e:
            print(f"خطأ في تحويل بيانات المخطط إلى JSON: {e}")
            theme_names_json = json.dumps(["خطأ"])
            percentages_json = json.dumps([1])

    html_template = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Cairo', sans-serif; background-color: #f0f2f5; margin: 0; padding: 20px; color: #333; line-height: 1.6; }}
            .poem-container {{ background-color: #fff; padding: 25px 35px; border-radius: 15px; max-width: 800px; margin: auto; box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08); }}
            .poem-title {{ font-size: 28px; font-weight: 700; margin-bottom: 8px; color: #2c3e50; text-align: center; }}
            .poet-info {{ font-size: 17px; color: #555; margin-bottom: 8px; text-align: center; }}
            .poet-info span {{ font-weight: 700; color: #333; }}
            .section-title {{ margin-top: 30px; margin-bottom: 15px; font-weight: 700; font-size: 22px; color: #34495e; border-right: 5px solid #3498db; padding-right: 12px; }}
            .verses-container {{ margin-top: 15px; padding-right: 10px; }}
            ul.verses-list {{ list-style: none; padding: 0; margin: 0; }}
            .verse {{ margin-bottom: 12px; padding: 10px 15px; background-color: #f8f9fa; border-radius: 8px; border-right: 4px solid #e0e0e0; transition: background-color 0.2s ease, border-color 0.2s ease; font-size: 16px; }}
            .verse:hover {{ background-color: #e9ecef; border-right-color: #3498db; }}
            canvas {{ max-width: 300px; max-height: 300px; margin-top: 20px; margin-bottom: 20px; }}
            .chart-container {{ display: flex; justify-content: center; margin-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="poem-container">
            <div class="poem-title">{title}</div>
            <div class="poet-info" dir="rtl">الشاعر: <span>{poet}</span></div>
            <div class="poet-info"dir="rtl">العصر: <span>{era}</span></div>
            <div class="section-title" dir="rtl">الموضوعات الأدبية</div>
            <div class="chart-container"><canvas id="themeChart"></canvas></div>
            <div class="section-title" dir="rtl">أبيات القصيدة</div>
            <div class="verses-container"><ul class="verses-list"  dir="rtl">{''.join(f'<li class="verse">{v}</li>' for v in verses)}</ul></div>
        </div>
        <script>
            const themeLabels = {theme_names_json};
            const themePercentages = {percentages_json};
            setTimeout(function() {{
                try {{
                    const ctx = document.getElementById('themeChart');
                    if (!ctx) {{ return; }}
                    const chartContext = ctx.getContext('2d');
                    let chartStatus = Chart.getChart(ctx);
                    if (chartStatus != undefined) {{ chartStatus.destroy(); }}
                    new Chart(chartContext, {{
                        type: 'pie', data: {{ labels: themeLabels, datasets: [{{ label: 'نسبة الموضوعات', data: themePercentages, backgroundColor: [ '#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#1abc9c', '#e67e22', '#34495e', '#7f8c8d', '#f39c12' ], borderColor: '#ffffff', borderWidth: 2 }}] }},
                        options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ position: 'bottom', labels: {{ font: {{ family: 'Cairo', size: 13 }}, color: '#333', padding: 15 }} }}, title: {{ display: false }}, tooltip: {{ bodyFont: {{ family: 'Cairo' }}, titleFont: {{ family: 'Cairo' }}, callbacks: {{ label: function(context) {{ let label = context.label || ''; if (label) {{ label += ': '; }} let value = context.dataset.data[context.dataIndex]; if (value !== null) {{ label += (value * 100).toFixed(1) + '%'; }} return label; }} }} }} }} }}
                    }});
                }} catch (e) {{ console.error("Error initializing chart:", e); }}
            }}, 150);
        </script>
    </body>
    </html>
    """
    filename = "selected_poem_temp.html"
    try:
        with open(filename, "w", encoding="utf-8") as f: f.write(html_template)
        return filename
    except Exception: return None


# --- Node search function (as is) ---
def find_node_by_id(tree_dict, target_id):
    if not tree_dict or not isinstance(tree_dict, dict):
        return None
    nodes_to_visit = list(tree_dict.values())
    while nodes_to_visit:
        current_node = nodes_to_visit.pop(0)
        if isinstance(current_node, dict):
            if current_node.get("id") == target_id:
                return current_node
            children = current_node.get("children")
            if children and isinstance(children, dict):
                nodes_to_visit.extend(children.values())
    return None

