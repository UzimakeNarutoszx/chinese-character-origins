import os
import sys
# resource
base_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(base_dir)
import tkinter as tk
from tkinter import ttk
import random

# 定义图片存放的文件夹路径
IMAGE_FOLDER = "ooooo"

# 完整文字数据（无任何省略）
stages = {
    "甲骨文": {
        "desc": """甲骨文（约公元前14世纪-前11世纪）是中国最早的成熟文字体系，因刻于龟甲兽骨得名。核心特征：
1. 宗教起源：主要用于商王室占卜记录，内容涉及祭祀、战争、农事等。占卜时将问题刻于龟甲，通过灼烧裂纹判断吉凶
2. 象形本源：保留强烈图画特征，如"日"作⊙、"月"作🌙，但已具备指事、会意等造字法雏形
3. 考古价值：现存约15万片甲骨，破译4500余单字，完整记录商代天文历法、官职制度、方国关系等，实证《史记》记载可靠性
4. 书写材质：多使用龟腹甲与牛肩胛骨，需经削锯、刮磨等复杂处理。刻写工具为青铜刀，后期出现朱书墨书未刻稿
5. 文化意义：2017年入选《世界记忆名录》，证实中华文明连续未断，推翻西方"殷商神话论"质疑""",
        "examples": {"人": "𠆢", "日": "⊙", "月": "🌙"}
    },
    "金文": {
        "desc": """金文（西周至战国）是青铜器铭文的统称，承载着礼乐文明精髓：
铸造工艺：采用"失蜡法"在陶范上刻字，浇铸后形成凸起阳文，线条浑厚圆润
发展阶段：
- 早期（西周）：承袭甲骨文，如利簋记载武王伐纣具体日期
- 盛期（西周中期）：毛公鼎499字鸿篇，记载册命仪式完整流程，书法结体严整
- 晚期（战国）：楚器鸟虫书、秦器石鼓文呈现地域分化，为六国文字差异实证
铭文内容：记载分封、赏赐、诉讼等重大事件，如曶鼎记录中国最早知识产权纠纷案
书法价值：开启"金石学"传统，清代阮元提出"北碑南帖"理论皆源于此""",
        "examples": {"王": "𤤴", "鼎": "𓍝", "车": "𨏖"}
    },
    "隶书": {
        "desc": """隶书（秦汉）的"隶变"是汉字古今分水岭：
社会动因：秦代文书剧增，"奏事繁多，篆字难成"，狱吏程邈整理民间简写体
演变分期：
1. 秦隶：睡虎地秦简保留篆意，字形趋方，产生波磔萌芽
2. 汉隶：马王堆帛书展现隶化完成过程，东汉《曹全碑》达到"精妙秀逸"巅峰
革新意义：
- 结构扁平化：打破篆书纵势，确立汉字横势结体原则
- 笔画符号化：出现"蚕头燕尾"特征笔法，奠定永字八法基础
- 书写效率提升：据测算较篆书提速3倍以上，适应大一统行政需求""",
        "examples": {"书": "𦘠", "水": "𣸑", "永": "𠘙"}
    },
    "楷书": {
        "desc": """楷书（汉末至今）的规范化历程：
起源争议：传统认为钟繇创制，但敦煌遗书P.3866显示东汉永寿二年（156年）已有成熟楷体
鼎盛时期：
- 魏碑：洛阳龙门二十品展现方笔雄强之美，代表北方书风
- 唐楷：欧阳询《九成宫》确立"楷法极则"，颜真卿突破"二王"体系创新法度
笔法体系：
1. 确立"永字八法"：侧（点）、勒（横）、弩（竖）、趯（钩）等基本笔形
2. 提按顿挫：通过笔锋弹性变化产生粗细对比，区别于隶书匀速运笔
3. 中宫收紧：结构内紧外松，如柳公权《玄秘塔碑》辐射式结体""",
        "examples": {"永": "永", "国": "國", "书": "書"}
    },
    "繁体字": {
        "desc": """繁体字（汉末-1956年）的文化承载：
文字学价值：
1. 保留造字理据："愛"存心部体现情感本质，"門"维持象形特征
2. 传承古籍原貌：四库全书733,300余卷均以繁体书写，简化后需专门转换
使用现状：
- 港澳地区：法律文书仍使用繁体，但基础教育推行"两文三语"
- 台湾争议：2006年《汉字整理方案》试图去中国化，将"臺"简作"台"引发文化割裂争议
书法应用：在篆刻、匾额、春联等传统场景保持主流，体现文化仪式感""",
        "examples": {"龙": "龍", "华": "華", "国": "國"}
    },
    "简体字": {
        "desc": """简体字（1956年至今）的改革历程：
历史渊源：1935年南京政府公布《第一批简体字表》，因戴季陶反对夭折
科学原则：
1. 草书楷化：專→专，保留怀素《自叙帖》笔意
2. 同音替代：後→后，遵循《广韵》音韵系统
3. 符号替代：漢→汉，采用南北朝已有俗字
社会效益：
- 文盲率变化：从民国80%降至1964年33%，2010年普查降至4.08%
- 信息处理：GB2312标准收录6,763字，覆盖99.75%现代汉语使用
国际影响：新加坡1969年全面采用，联合国1983年起中文文件采用简繁双版本""",
        "examples": {"龙": "龙", "华": "华", "国": "国"}
    }
}

class HanziApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("汉字的渊源")
        self.window.geometry("1200x750")
        
        # 初始化图片字典
        self.images = {}
        
        # 加载图片
        self.load_images()
        
        # 创建UI
        self.create_ui()
        
    def load_images(self):
        """加载并自动缩放图片"""
        image_files = {
            "甲骨文": "甲骨文.png",
            "金文": "金文.png",
            "隶书": "隶书.png",
            "楷书": "楷书.png",
            "繁体字": "繁体字.png",
            "简体字": "简体字.png"
        }
        
        for stage, filename in image_files.items():
            src_path = os.path.join('ooooo', filename)
            
            if not os.path.exists(src_path):
                # print(f"图片文件不存在: {src_path}")
                self.images[stage] = self.create_error_image()
                continue
                
            try:
                # 直接加载图片
                original_img = tk.PhotoImage(file=src_path)
                
                # 计算缩放比例（限制最大宽度300px）
                max_width = 300
                width = original_img.width()
                height = original_img.height()
                
                if width > max_width:
                    ratio = width / max_width
                    # 使用subsample方法缩小图片
                    self.images[stage] = original_img.subsample(int(ratio), int(ratio))
                else:
                    self.images[stage] = original_img
                    
                # print(f"成功加载: {stage} -> 原始尺寸: {width}x{height} -> 缩放后: "
                #       f"{self.images[stage].width()}x{self.images[stage].height()}")
                
            except Exception as e:
                # print(f"图片处理失败: {e}")
                self.images[stage] = self.create_error_image()

    def create_error_image(self):
        """创建错误占位图"""
        try:
            img = tk.PhotoImage(width=300, height=300)
            img.put("#FFCCCC", to=(0, 0, 299, 299))  # 浅红色背景
            return img
        except:
            return None

    def create_ui(self):
        """创建主界面"""
        # 顶部按钮区域
        top_frame = ttk.Frame(self.window)
        top_frame.pack(pady=10, fill=tk.X)
        
        style = ttk.Style()
        style.configure("TButton", font=('微软雅黑', 12), padding=5)
        
        # 创建导航按钮
        for stage in stages:
            btn = ttk.Button(top_frame, text=stage, 
                           command=lambda s=stage: self.show_info(s))
            btn.pack(side=tk.LEFT, padx=5)

        # 主内容区域
        content_frame = ttk.Frame(self.window)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # 左侧文字区域
        text_frame = ttk.Frame(content_frame)
        text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.info_text = tk.Text(text_frame, wrap=tk.WORD, font=('宋体', 14), 
                               bg="#FAF8F5", padx=15, pady=15)
        scrollbar = ttk.Scrollbar(text_frame, command=self.info_text.yview)
        self.info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.info_text.config(yscrollcommand=scrollbar.set)
        
        # 右侧图片区域（固定尺寸）
        self.image_frame = ttk.Frame(content_frame, width=320, height=320)
        self.image_frame.pack_propagate(False)
        self.image_frame.pack(side=tk.RIGHT, padx=10, pady=5)
        
        # 底部游戏区域
        self.create_game_section()
    
    def show_info(self, stage):
        """显示文字信息和图片"""
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        
        # 显示文字内容
        self.info_text.insert(tk.END, f"【{stage}】\n", "title")
        self.info_text.insert(tk.END, stages[stage]["desc"] + "\n\n", "content")
        self.info_text.insert(tk.END, "示例：\n", "subtitle")
        for modern, ancient in stages[stage]["examples"].items():
            self.info_text.insert(tk.END, f"{ancient} → {modern}   ", "example")
        
        # 设置文本样式
        self.info_text.tag_config("title", font=('微软雅黑', 18, 'bold'), foreground="#2F4F4F")
        self.info_text.tag_config("content", font=('宋体', 14), spacing3=8)
        self.info_text.tag_config("subtitle", font=('楷体', 16), foreground="#556B2F")
        self.info_text.tag_config("example", font=('SimSun', 20))
        self.info_text.config(state=tk.DISABLED)
        
        # 显示图片
        self.show_image(stage)
    
    def show_image(self, stage):
        """显示缩放后的图片"""
        for widget in self.image_frame.winfo_children():
            widget.destroy()
        
        if stage in self.images and self.images[stage]:
            label = ttk.Label(self.image_frame, image=self.images[stage])
            label.image = self.images[stage]  # 保持引用
            label.pack(padx=10, pady=10)
        else:
            ttk.Label(self.image_frame, text=f"无法加载图片", foreground="red").pack(pady=50)
    
    def create_game_section(self):
        """创建游戏区域"""
        game_frame = ttk.Frame(self.window)
        game_frame.pack(pady=20)
        
        self.question_label = ttk.Label(game_frame, font=('宋体', 14))
        self.answer_entry = ttk.Entry(game_frame, font=('宋体', 14), width=10)
        ttk.Button(game_frame, text="提交", command=self.check_answer).pack(side=tk.RIGHT, padx=10)
        self.answer_entry.pack(side=tk.RIGHT, padx=10)
        self.question_label.pack(side=tk.LEFT)
        
        self.new_question()
    
    def new_question(self):
        """生成新问题"""
        stage = random.choice(list(stages.keys()))
        example = random.choice(list(stages[stage]["examples"].items()))
        self.current_answer, self.current_char = example
        self.question_label.config(text=f"猜猜这个 {stage} 【{self.current_char}】 对应哪个现代汉字？")
        self.answer_entry.delete(0, tk.END)
    
    def check_answer(self):
        """验证答案"""
        user_answer = self.answer_entry.get().strip()
        if user_answer == self.current_answer:
            result = "✓ 正确！"
            self.info_text.config(bg="#90EE90")
        else:
            result = f"✗ 错误，正确答案是：{self.current_answer}"
            self.info_text.config(bg="#FF6B6B")
        
        self.info_text.config(state=tk.NORMAL)
        self.info_text.insert(tk.END, f"\n\n{result}", "result")
        self.info_text.see(tk.END)
        self.info_text.config(state=tk.DISABLED)
        self.new_question()

if __name__ == "__main__":
    app = HanziApp()
    app.window.mainloop()