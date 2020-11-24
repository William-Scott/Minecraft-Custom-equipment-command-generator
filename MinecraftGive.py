import tkinter as tk
import tkinter.ttk as ttk
import sys
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.bg_image = tk.PhotoImage(file=resource_path("res\\bg.png"))
        self.imgLabel_bg = tk.Label(root, image=self.bg_image)
        self.imgLabel_bg.place(x=0,y=0)

        self.tab_main = ttk.Notebook()
        self.tab_main.place(relx=0.02, rely=0.02, relwidth=0.962, relheight=0.96)


        self.create_widgets_weapon()
        self.create_widgets_tool()
        self.create_widgets_armor()
        self.create_widgets_bow()
        self.create_widgets_crossbow()
        self.create_widgets_trident()
        self.create_widgets_fishingbobber()
        #self.create_widgets_tab('方块',600)

    '''
    重构的模板函数，对性能无太大影响，暂搁置
    def create_widgets_tab(self,name_zh,tabpos,ico_path,tachie_path,langs1,langs2):
        tab = tk.Frame(self.tab_main)
        tab.place(x=tabpos,y=30)
        self.tab_main.add(tab, text=name_zh)

        canvas_bg = tk.Canvas(tab, width=800, height=600, highlightthickness=0, borderwidth=0)
        canvas_bg.place(x=0,y=0)
        bgid = canvas_bg.create_image(385,263, image=self.bg_image)
        image_ico = tk.PhotoImage(file=resource_path(ico_path))
        image_tachie = tk.PhotoImage(file=resource_path(tachie_path))
        create_ico = canvas_bg.create_image(250,280, image=image_ico)
        create_tachie = canvas_bg.create_image(680,430, image=image_tachie)

        LFselect = tk.LabelFrame(tab, text='选择%s:' %(name_zh), padx=5,pady=5)
        LFselect.place(x=10,y=20)
    '''

    def create_widgets_weapon(self):
        #武器的tab页面
        self.tab_weapon = tk.Frame(self.tab_main)
        self.tab_weapon.place(x=0,y=30)
        self.tab_main.add(self.tab_weapon,text='武器')
        #canvas图片控件
        self.canvas_bg_weapon = tk.Canvas(self.tab_weapon, width=800, height=600, highlightthickness=0, borderwidth=0)
        self.canvas_bg_weapon.place(x=0, y=0)
        self.bgid_weapon = self.canvas_bg_weapon.create_image(385,263, image=self.bg_image)
        self.image_weapon = tk.PhotoImage(file=resource_path("res\\weapon.png"))
        self.image_seija0 = tk.PhotoImage(file=resource_path("res\\0.png"))
        self.id_weapon = self.canvas_bg_weapon.create_image(250,280, image=self.image_weapon)
        self.seijaid_weapon = self.canvas_bg_weapon.create_image(680,430, image=self.image_seija0)
        #武器的LabelFrame
        self.LFselect_weapon = tk.LabelFrame(self.tab_weapon, text='选择武器：', padx=5,pady=5)
        self.LFselect_weapon.place(x=10,y=20)
        #武器的Radiobutton
        self.weapon_langs = [('木剑','minecraft:wooden_sword'),
                             ('石剑','minecraft:stone_sword'),
                             ('铁剑','minecraft:iron_sword'),
                             ('钻石剑','minecraft:diamond_sword'),
                             ('金剑','minecraft:golden_sword'),
                             ('下界合金剑','minecraft:netherite_sword')]
        self.str_weapon = tk.StringVar()
        self.str_weapon.set('0')
        for name_zh,name_en in self.weapon_langs:
            self.weapon = tk.Radiobutton(self.LFselect_weapon, text=name_zh, variable=self.str_weapon, value=name_en, command=self.string_splicing_weapon)
            self.weapon.pack(anchor='w')
        #武器的附魔的LabelFrame
        self.LFselect_weapon_enchant = tk.LabelFrame(self.tab_weapon, text='选择附魔：', padx=5,pady=5)
        self.LFselect_weapon_enchant.place(x=430,y=20)
        #武器的附魔的Checkbutton
        self.weapon_enchant_langs = [('节肢杀手','minecraft:bane_of_arthropods',0,0),
                                     ('火焰附加','minecraft:fire_aspect',0,1),
                                     ('击退','minecraft:knockback',1,0),
                                     ('抢夺','minecraft:looting',1,1),
                                     ('经验修补','minecraft:mending',2,0),
                                     ('锋利','minecraft:sharpness',2,1),
                                     ('亡灵杀手','minecraft:smite',3,0),
                                     ('横扫之刃','minecraft:sweeping',3,1),
                                     ('耐久','minecraft:unbreaking',4,0)]
        #self.gridlist = [(0,0),(0,1),(0,2),
                         #(1,0),(1,1),(1,2),
                         #(2,0),(2,1),(2,2)]
        #存放武器附魔和附魔等级的列表
        self.array_weapon_enchant = []
        self.array_weapon_enchantlv = []
        #武器的附魔的Frame
        for name_zh,name_en,posx,posy in self.weapon_enchant_langs:
            self.Fselect_weapon_enchant = tk.Frame(self.LFselect_weapon_enchant)
            self.Fselect_weapon_enchant.grid(row=posx, column=posy, padx=5,pady=5, sticky=tk.W)
            #武器的附魔的Checkbutton
            self.str_weapon_enchant = tk.StringVar()
            self.str_weapon_enchant.set("0")
            self.array_weapon_enchant.append(self.str_weapon_enchant)
            self.weapon_enchant = tk.Checkbutton(self.Fselect_weapon_enchant, text=name_zh, onvalue=name_en, variable=self.array_weapon_enchant[-1], command=self.string_splicing_weapon)
            self.weapon_enchant.pack(side="left")
            #武器的附魔的等级的Spinbox
            self.str_weapon_enchantlv = tk.IntVar()
            self.str_weapon_enchantlv.set(0)
            self.array_weapon_enchantlv.append(self.str_weapon_enchantlv)
            self.weapon_enchantlv = tk.Spinbox(self.Fselect_weapon_enchant, from_=1, to=10, increment=1, textvariable=self.array_weapon_enchantlv[-1], width=2, command=self.string_splicing_weapon)
            self.weapon_enchantlv.pack(side="left")
        #武器的额外的LabelFrame
        self.LFselect_weapon_extra = tk.LabelFrame(self.tab_weapon, text='选择额外属性：', padx=5,pady=5)
        self.LFselect_weapon_extra.place(x=10,y=250)
        self.str_weapon_extra = tk.StringVar()
        self.str_weapon_extra.set("0")
        self.weapon_extra = tk.Checkbutton(self.LFselect_weapon_extra, text='不损', onvalue="Unbreakable:1", variable=self.str_weapon_extra, command=self.string_splicing_weapon)
        self.weapon_extra.pack()
        #武器名输入框
        self.LFselect_weapon_name = tk.LabelFrame(self.tab_weapon, text='输入武器名称', padx=5,pady=5)
        self.LFselect_weapon_name.place(x=10,y=350)
        self.str_weapon_name = tk.StringVar()
        self.str_weapon_name.set("")
        self.Text_weapon_name = tk.Entry(self.LFselect_weapon_name, textvariable=self.str_weapon_name, width=30, insertwidth=1)
        self.Text_weapon_name.pack()
        self.Text_weapon_name.bind("<KeyRelease>", self.string_splicing_weapon)
        #武器的输出框
        self.Text_weapon = tk.Text(self.tab_weapon,width=80,height=5)
        self.Text_weapon.place(x=10,y=410)
        #武器的生成按钮
        self.button_weapon = tk.Button(self.tab_weapon,text='生成/Give命令',width=15, command=self.output_weapon)
        self.button_weapon.place(x=10,y=510)
        #长度计数
        self.str_num_weapon = tk.StringVar()
        self.str_num_weapon.set('当前命令包含的字符个数为：')
        self.canvas_str_num_weapon = self.canvas_bg_weapon.create_text(10,495, text=self.str_num_weapon.get(), anchor = tk.W)

    def create_widgets_tool(self):
        #工具的tab页面
        self.tab_tool = tk.Frame(self.tab_main)
        self.tab_tool.place(x=100,y=30)
        self.tab_main.add(self.tab_tool,text='工具')

        self.canvas_bg_tool = tk.Canvas(self.tab_tool, width=800, height=600, highlightthickness=0, borderwidth=0)
        self.canvas_bg_tool.place(x=0, y=0)
        self.bgid_tool = self.canvas_bg_tool.create_image(385,263, image=self.bg_image)
        self.image_tool = tk.PhotoImage(file=resource_path("res\\tool.png"))
        self.image_seija1 = tk.PhotoImage(file=resource_path("res\\1.png"))
        self.id_tool = self.canvas_bg_tool.create_image(250,280, image=self.image_tool)
        self.seijaid_tool = self.canvas_bg_tool.create_image(680,430, image=self.image_seija1)

        self.LFselect_tool = tk.LabelFrame(self.tab_tool, text='选择工具：', padx=5,pady=5)
        self.LFselect_tool.place(x=10,y=20)

        self.tool_langs = [('木斧','minecraft:wooden_axe',0,0),
                           ('石斧','minecraft:stone_axe',1,0),
                           ('铁斧','minecraft:iron_axe',2,0),
                           ('钻石斧','minecraft:diamond_axe',3,0),
                           ('金斧','minecraft:golden_axe',4,0),
                           ('下界合金斧','minecraft:netherite_axe',5,0),
                           ('木镐','minecraft:wooden_pickaxe',0,1),
                           ('石镐','minecraft:stone_pickaxe',1,1),
                           ('铁镐','minecraft:iron_pickaxe',2,1),
                           ('钻石镐','minecraft:diamond_pickaxe',3,1),
                           ('金镐','minecraft:golden_pickaxe',4,1),
                           ('下界合金镐','minecraft:netherite_pickaxe',5,1),
                           ('木锹','minecraft:wooden_shovel',0,2),
                           ('石锹','minecraft:stone_shovel',1,2),
                           ('铁锹','minecraft:iron_shovel',2,2),
                           ('钻石锹','minecraft:diamond_shovel',3,2),
                           ('金锹','minecraft:golden_shovel',4,2),
                           ('下界合金锹','minecraft:netherite_shovel',5,2),
                           ('木锄','minecraft.wooden_hoe',0,3),
                           ('石锄','minecraft.stone_hoe',1,3),
                           ('铁锄','minecraft.iron_hoe',2,3),
                           ('钻石锄','minecraft.diamond_hoe',3,3),
                           ('金锄','minecraft.golden_hoe',4,3),
                           ('下界合金锄','minecraft.netherite_hoe',5,3)]
        self.str_tool = tk.StringVar()
        self.str_tool.set("0")
        for name_zh,name_en,posx,posy in self.tool_langs:
            self.tool = tk.Radiobutton(self.LFselect_tool, text=name_zh, variable=self.str_tool, value=name_en, command=self.string_splicing_tool)
            self.tool.grid(row=posx, column=posy, sticky=tk.W)

        self.LFselect_tool_enchant = tk.LabelFrame(self.tab_tool, text='选择附魔：', padx=5,pady=5)
        self.LFselect_tool_enchant.place(x=430,y=20)

        self.tool_enchant_langs = [('效率','minecraft:efficiency',0,0),
                                   ('时运','minecraft:fortune',1,0),
                                   ('精准采集','minecraft:silk_touch',2,0),
                                   ('经验修补','minecraft:mending',3,0),
                                   ('耐久','minecraft:unbreaking',4,0)]

        self.array_tool_enchant = []
        self.array_tool_enchantlv = []

        for name_zh,name_en,posx,posy in self.tool_enchant_langs:
            self.Fselect_tool_enchant = tk.Frame(self.LFselect_tool_enchant)
            self.Fselect_tool_enchant.grid(row=posx, column=posy, padx=5,pady=5, sticky=tk.W)

            self.str_tool_enchant = tk.StringVar()
            self.str_tool_enchant.set("0")
            self.array_tool_enchant.append(self.str_tool_enchant)
            self.tool_enchant = tk.Checkbutton(self.Fselect_tool_enchant, text=name_zh, onvalue=name_en, variable=self.array_tool_enchant[-1], command=self.string_splicing_tool)
            self.tool_enchant.pack(side='left')

            self.str_tool_enchantlv = tk.IntVar()
            self.str_tool_enchantlv.set(0)
            self.array_tool_enchantlv.append(self.str_tool_enchantlv)
            self.tool_enchantlv = tk.Spinbox(self.Fselect_tool_enchant, from_=1, to=10, increment=1, textvariable=self.array_tool_enchantlv[-1], width=2, command=self.string_splicing_tool)
            self.tool_enchantlv.pack(side='left')

        self.LFselect_tool_extra = tk.LabelFrame(self.tab_tool, text='选择额外属性：', padx=5,pady=5)
        self.LFselect_tool_extra.place(x=10,y=250)
        self.str_tool_extra = tk.StringVar()
        self.str_tool_extra.set("0")
        self.tool_extra = tk.Checkbutton(self.LFselect_tool_extra, text='不损', onvalue='Unbreakable:1', variable=self.str_tool_extra, command=self.string_splicing_tool)
        self.tool_extra.pack()

        self.LFselect_tool_name = tk.LabelFrame(self.tab_tool, text='输入工具名称', padx=5,pady=5)
        self.LFselect_tool_name.place(x=10,y=350)
        self.str_tool_name = tk.StringVar()
        self.str_tool_name.set("")
        self.Text_tool_name = tk.Entry(self.LFselect_tool_name, textvariable=self.str_tool_name, width=30, insertwidth=1)
        self.Text_tool_name.pack()
        self.Text_tool_name.bind("<KeyRelease>", self.string_splicing_tool)

        self.Text_tool = tk.Text(self.tab_tool,width=80,height=5)
        self.Text_tool.place(x=10,y=410)
        self.button_tool = tk.Button(self.tab_tool,text='生成/Give命令',width=15, command=self.output_tool)
        self.button_tool.place(x=10,y=510)

        self.str_num_tool = tk.StringVar()
        self.str_num_tool.set('当前命令包含的字符个数为：')
        self.canvas_str_num_tool = self.canvas_bg_tool.create_text(10,495, text=self.str_num_tool.get(), anchor = tk.W)

    def create_widgets_armor(self):
        self.tab_armor = tk.Frame(self.tab_main)
        self.tab_armor.place(x=200,y=30)
        self.tab_main.add(self.tab_armor,text='盔甲')

        self.canvas_bg_armor = tk.Canvas(self.tab_armor, width=800, height=600, highlightthickness=0, borderwidth=0)
        self.canvas_bg_armor.place(x=0, y=0)
        self.bgid_armor = self.canvas_bg_armor.create_image(385,263, image=self.bg_image)
        self.image_armor = tk.PhotoImage(file=resource_path("res\\armor.png"))
        self.image_seija2 = tk.PhotoImage(file=resource_path("res\\2.png"))
        self.id_armor = self.canvas_bg_armor.create_image(250,280, image=self.image_armor)
        self.seijaid_armor = self.canvas_bg_armor.create_image(680,430, image=self.image_seija2)

        self.LFselect_armor = tk.LabelFrame(self.tab_armor, text='选择盔甲：', padx=5,pady=5)
        self.LFselect_armor.place(x=10,y=20)

        self.armor_langs = [('皮革帽子','minecraft:leather_helmet',0,0),
                            ('皮革外套','minecraft:leather_chestplate',0,1),
                            ('皮革裤子','minecraft:leather_leggings',0,2),
                            ('皮革靴子','minecraft:leather_boots',0,3),
                            ('锁链头盔','minecraft:chainmail_helmet',1,0),
                            ('锁链胸甲','minecraft:chainmail_chestplate',1,1),
                            ('锁链护腿','minecraft:chainmail_leggings',1,2),
                            ('锁链靴子','minecraft:chainmail_boots',1,3),
                            ('铁头盔','minecraft:iron_helmet',2,0),
                            ('铁胸甲','minecraft:iron_chestplate',2,1),
                            ('铁护腿','minecraft:iron_leggings',2,2),
                            ('铁靴子','minecraft:iron_boots',2,3),
                            ('钻石头盔','minecraft:diamond_helmet',3,0),
                            ('钻石胸甲','minecraft:diamond_chestplate',3,1),
                            ('钻石护腿','minecraft:diamond_leggings',3,2),
                            ('钻石靴子','minecraft:diamond_boots',3,3),
                            ('金头盔','minecraft:golden_helmet',4,0),
                            ('金胸甲','minecraft:gold_chestplate',4,1),
                            ('金护腿','minecraft:golden_leggings',4,2),
                            ('金靴子','minecraft:golden_boots',4,3),
                            ('下界合金头盔','minecraft:netherite_helmet',5,0),
                            ('下界合金胸甲','minecraft:netherite_chestplate',5,1),
                            ('下界合金护腿','minecraft:netherite_leggings',5,2),
                            ('下界合金靴子','minecraft:netherite_boots',5,3)]
        self.str_armor = tk.StringVar()
        self.str_armor.set("0")
        for name_zh,name_en,posx,posy in self.armor_langs:
            self.armor = tk.Radiobutton(self.LFselect_armor, text=name_zh, variable=self.str_armor, value=name_en, command=self.string_splicing_armor)
            self.armor.grid(row=posx, column=posy, sticky=tk.W)

        self.LFselect_armor_enchant = tk.LabelFrame(self.tab_armor, text='选择附魔：', padx=5,pady=5)
        self.LFselect_armor_enchant.place(x=430,y=20)

        self.armor_enchant_langs = [('保护','minecraft:protection',0,0),
                                    ('弹射物保护','minecraft:projectile_protection',0,1),
                                    ('爆炸保护','minecraft:blast_protection',1,0),
                                    ('火焰保护','minecraft:fire_protection',1,1),
                                    ('摔落保护','minecraft:feather_falling',2,0),
                                    ('冰霜行者','minecraft:frost_walker',2,1),
                                    ('水下呼吸','minecraft:respiration',3,0),
                                    ('灵魂疾行','minecraft:soul_speed',3,1),
                                    ('荆棘','minecraft:thorns',4,0),
                                    ('水下速掘','minecraft:aqua_affinity',4,1),
                                    ('耐久','minecraft:unbreaking',5,0),
                                    ('深海探索者','minecraft:depth_strider',5,1),
                                    ('经验修补','minecraft:mending',6,0)]
        self.array_armor_enchant = []
        self.array_armor_enchantlv = []

        for name_zh,name_en,posx,posy in self.armor_enchant_langs:
            self.Fselect_armor_enchant = tk.Frame(self.LFselect_armor_enchant)
            self.Fselect_armor_enchant.grid(row=posx, column=posy, padx=5,pady=5, sticky=tk.W)

            self.str_armor_enchant = tk.StringVar()
            self.str_armor_enchant.set("0")
            self.array_armor_enchant.append(self.str_armor_enchant)
            self.armor_enchant = tk.Checkbutton(self.Fselect_armor_enchant, text=name_zh, onvalue=name_en, variable=self.array_armor_enchant[-1], command=self.string_splicing_armor)
            self.armor_enchant.pack(side='left')

            self.str_armor_enchantlv = tk.IntVar()
            self.str_armor_enchantlv.set(0)
            self.array_armor_enchantlv.append(self.str_armor_enchantlv)
            self.armor_enchantlv = tk.Spinbox(self.Fselect_armor_enchant, from_=1, to=10, increment=1, textvariable=self.array_armor_enchantlv[-1], width=2, command=self.string_splicing_armor)
            self.armor_enchantlv.pack(side='left')

        self.LFselect_armor_extra = tk.LabelFrame(self.tab_armor, text='选择额外属性：', padx=5,pady=5)
        self.LFselect_armor_extra.place(x=10,y=250)
        self.str_armor_extra = tk.StringVar()
        self.str_armor_extra.set("0")
        self.armor_extra = tk.Checkbutton(self.LFselect_armor_extra, text='不损', onvalue='Unbreakable:1', variable=self.str_armor_extra, command=self.string_splicing_armor)
        self.armor_extra.pack()

        self.LFselect_armor_name = tk.LabelFrame(self.tab_armor, text='输入盔甲名称', padx=5,pady=5)
        self.LFselect_armor_name.place(x=10,y=350)
        self.str_armor_name = tk.StringVar()
        self.str_armor_name.set("")
        self.Text_armor_name = tk.Entry(self.LFselect_armor_name, textvariable=self.str_armor_name, width=30, insertwidth=1)
        self.Text_armor_name.pack()
        self.Text_armor_name.bind("<KeyRelease>", self.string_splicing_armor)

        self.Text_armor = tk.Text(self.tab_armor,width=80,height=5)
        self.Text_armor.place(x=10,y=410)
        self.button_armor = tk.Button(self.tab_armor,text='生成/Give命令',width=15, command=self.output_armor)
        self.button_armor.place(x=10,y=510)

        self.str_num_armor = tk.StringVar()
        self.str_num_armor.set('当前命令包含的字符个数为：')
        self.canvas_str_num_armor = self.canvas_bg_armor.create_text(10,495, text=self.str_num_armor.get(), anchor = tk.W)

    def create_widgets_bow(self):
        self.tab_bow = tk.Frame(self.tab_main)
        self.tab_bow.place(x=300,y=30)
        self.tab_main.add(self.tab_bow,text='弓')

        self.canvas_bg_bow = tk.Canvas(self.tab_bow, width=800, height=600, highlightthickness=0, borderwidth=0)
        self.canvas_bg_bow.place(x=0, y=0)
        self.bgid_bow = self.canvas_bg_bow.create_image(385,263, image=self.bg_image)
        self.image_bow = tk.PhotoImage(file=resource_path("res\\bow.png"))
        self.image_seija3 = tk.PhotoImage(file=resource_path("res\\3.png"))
        self.id_bow = self.canvas_bg_bow.create_image(250,280, image=self.image_bow)
        self.seijaid_bow = self.canvas_bg_bow.create_image(680,430, image=self.image_seija3)

        self.LFselect_bow = tk.LabelFrame(self.tab_bow, text='选择弓：', padx=5,pady=5)
        self.LFselect_bow.place(x=10,y=20)

        self.bow_langs = [('弓','minecraft:bow')]
        self.str_bow = tk.StringVar()
        self.str_bow.set('0')
        for name_zh,name_en in self.bow_langs:
            self.bow = tk.Radiobutton(self.LFselect_bow, text=name_zh, variable=self.str_bow, value=name_en, command=self.string_splicing_bow)
            self.bow.pack(anchor='w')

        self.LFselect_bow_enchant = tk.LabelFrame(self.tab_bow, text='选择附魔：', padx=5,pady=5)
        self.LFselect_bow_enchant.place(x=430,y=20)

        self.bow_enchant_langs = [('力量','minecraft:power',0,0),
                                  ('冲击','minecraft:punch',1,0),
                                  ('无限','minecraft:infinity',2,0),
                                  ('火矢','minecraft:flame',3,0),
                                  ('经验修补','minecraft:mending',4,0),
                                  ('耐久','minecraft:unbreaking',5,0)]
        self.array_bow_enchant = []
        self.array_bow_enchantlv = []

        for name_zh,name_en,posx,posy in self.bow_enchant_langs:
            self.Fselect_bow_enchant = tk.Frame(self.LFselect_bow_enchant)
            self.Fselect_bow_enchant.grid(row=posx, column=posy, padx=5,pady=5, sticky=tk.W)

            self.str_bow_enchant = tk.StringVar()
            self.str_bow_enchant.set("0")
            self.array_bow_enchant.append(self.str_bow_enchant)
            self.bow_enchant = tk.Checkbutton(self.Fselect_bow_enchant, text=name_zh, onvalue=name_en, variable=self.array_bow_enchant[-1], command=self.string_splicing_bow)
            self.bow_enchant.pack(side="left")

            self.str_bow_enchantlv = tk.IntVar()
            self.str_bow_enchantlv.set(0)
            self.array_bow_enchantlv.append(self.str_bow_enchantlv)
            self.bow_enchantlv = tk.Spinbox(self.Fselect_bow_enchant, from_=1, to=10, increment=1, textvariable=self.array_bow_enchantlv[-1], width=2, command=self.string_splicing_bow)
            self.bow_enchantlv.pack(side="left")

        self.LFselect_bow_extra = tk.LabelFrame(self.tab_bow, text='选择额外属性：', padx=5,pady=5)
        self.LFselect_bow_extra.place(x=10,y=250)
        self.str_bow_extra = tk.StringVar()
        self.str_bow_extra.set("0")
        self.bow_extra = tk.Checkbutton(self.LFselect_bow_extra, text='不损', onvalue="Unbreakable:1", variable=self.str_bow_extra, command=self.string_splicing_bow)
        self.bow_extra.pack()

        self.LFselect_bow_name = tk.LabelFrame(self.tab_bow, text='输入弓名称', padx=5,pady=5)
        self.LFselect_bow_name.place(x=10,y=350)
        self.str_bow_name = tk.StringVar()
        self.str_bow_name.set("")
        self.Text_bow_name = tk.Entry(self.LFselect_bow_name, textvariable=self.str_bow_name, width=30, insertwidth=1)
        self.Text_bow_name.pack()
        self.Text_bow_name.bind("<KeyRelease>", self.string_splicing_bow)

        self.Text_bow = tk.Text(self.tab_bow,width=80,height=5)
        self.Text_bow.place(x=10,y=410)
        self.button_bow = tk.Button(self.tab_bow,text='生成/Give命令',width=15, command=self.output_bow)
        self.button_bow.place(x=10,y=510)

        self.str_num_bow = tk.StringVar()
        self.str_num_bow.set('当前命令包含的字符个数为：')
        self.canvas_str_num_bow = self.canvas_bg_bow.create_text(10,495, text=self.str_num_bow.get(), anchor = tk.W)

    def create_widgets_crossbow(self):
        self.tab_crossbow = tk.Frame(self.tab_main)
        self.tab_crossbow.place(x=400,y=30)
        self.tab_main.add(self.tab_crossbow,text='弩')

        self.canvas_bg_crossbow = tk.Canvas(self.tab_crossbow, width=800, height=600, highlightthickness=0, borderwidth=0)
        self.canvas_bg_crossbow.place(x=0, y=0)
        self.bgid_crossbow = self.canvas_bg_crossbow.create_image(385,263, image=self.bg_image)
        self.image_crossbow = tk.PhotoImage(file=resource_path("res\\crossbow.png"))
        self.image_seija4 = tk.PhotoImage(file=resource_path("res\\4.png"))
        self.id_crossbow = self.canvas_bg_crossbow.create_image(250,280, image=self.image_crossbow)
        self.seijaid_crossbow = self.canvas_bg_crossbow.create_image(680,430, image=self.image_seija4)

        self.LFselect_crossbow = tk.LabelFrame(self.tab_crossbow, text='选择弩：', padx=5,pady=5)
        self.LFselect_crossbow.place(x=10,y=20)

        self.crossbow_langs = [('弩','minecraft:crossbow')]
        self.str_crossbow = tk.StringVar()
        self.str_crossbow.set('0')
        for name_zh,name_en in self.crossbow_langs:
            self.crossbow = tk.Radiobutton(self.LFselect_crossbow, text=name_zh, variable=self.str_crossbow, value=name_en, command=self.string_splicing_crossbow)
            self.crossbow.pack(anchor='w')

        self.LFselect_crossbow_enchant = tk.LabelFrame(self.tab_crossbow, text='选择附魔：', padx=5,pady=5)
        self.LFselect_crossbow_enchant.place(x=430,y=20)

        self.crossbow_enchant_langs = [('多重射击','minecraft:multishot',0,0),
                                  ('穿透','minecraft:piercing',1,0),
                                  ('快速装填','minecraft:quick_charge',2,0),
                                  ('经验修补','minecraft:mending',3,0),
                                  ('耐久','minecraft:unbreaking',4,0)]
        self.array_crossbow_enchant = []
        self.array_crossbow_enchantlv = []

        for name_zh,name_en,posx,posy in self.crossbow_enchant_langs:
            self.Fselect_crossbow_enchant = tk.Frame(self.LFselect_crossbow_enchant)
            self.Fselect_crossbow_enchant.grid(row=posx, column=posy, padx=5,pady=5, sticky=tk.W)

            self.str_crossbow_enchant = tk.StringVar()
            self.str_crossbow_enchant.set("0")
            self.array_crossbow_enchant.append(self.str_crossbow_enchant)
            self.crossbow_enchant = tk.Checkbutton(self.Fselect_crossbow_enchant, text=name_zh, onvalue=name_en, variable=self.array_crossbow_enchant[-1], command=self.string_splicing_crossbow)
            self.crossbow_enchant.pack(side="left")

            self.str_crossbow_enchantlv = tk.IntVar()
            self.str_crossbow_enchantlv.set(0)
            self.array_crossbow_enchantlv.append(self.str_crossbow_enchantlv)
            self.crossbow_enchantlv = tk.Spinbox(self.Fselect_crossbow_enchant, from_=1, to=10, increment=1, textvariable=self.array_crossbow_enchantlv[-1], width=2, command=self.string_splicing_crossbow)
            self.crossbow_enchantlv.pack(side="left")

        self.LFselect_crossbow_extra = tk.LabelFrame(self.tab_crossbow, text='选择额外属性：', padx=5,pady=5)
        self.LFselect_crossbow_extra.place(x=10,y=250)
        self.str_crossbow_extra = tk.StringVar()
        self.str_crossbow_extra.set("0")
        self.crossbow_extra = tk.Checkbutton(self.LFselect_crossbow_extra, text='不损', onvalue="Unbreakable:1", variable=self.str_crossbow_extra, command=self.string_splicing_crossbow)
        self.crossbow_extra.pack()

        self.LFselect_crossbow_name = tk.LabelFrame(self.tab_crossbow, text='输入弩名称', padx=5,pady=5)
        self.LFselect_crossbow_name.place(x=10,y=350)
        self.str_crossbow_name = tk.StringVar()
        self.str_crossbow_name.set("")
        self.Text_crossbow_name = tk.Entry(self.LFselect_crossbow_name, textvariable=self.str_crossbow_name, width=30, insertwidth=1)
        self.Text_crossbow_name.pack()
        self.Text_crossbow_name.bind("<KeyRelease>", self.string_splicing_crossbow)

        self.Text_crossbow = tk.Text(self.tab_crossbow,width=80,height=5)
        self.Text_crossbow.place(x=10,y=410)
        self.button_crossbow = tk.Button(self.tab_crossbow,text='生成/Give命令',width=15, command=self.output_crossbow)
        self.button_crossbow.place(x=10,y=510)

        self.str_num_crossbow = tk.StringVar()
        self.str_num_crossbow.set('当前命令包含的字符个数为：')
        self.canvas_str_num_crossbow = self.canvas_bg_crossbow.create_text(10,495, text=self.str_num_crossbow.get(), anchor = tk.W)

    def create_widgets_trident(self):
        self.tab_trident = tk.Frame(self.tab_main)
        self.tab_trident.place(x=500,y=30)
        self.tab_main.add(self.tab_trident,text='三叉戟')

        self.canvas_bg_trident = tk.Canvas(self.tab_trident, width=800, height=600, highlightthickness=0, borderwidth=0)
        self.canvas_bg_trident.place(x=0, y=0)
        self.bgid_trident = self.canvas_bg_trident.create_image(385,263, image=self.bg_image)
        self.image_trident = tk.PhotoImage(file=resource_path("res\\trident.png"))
        self.image_seija5 = tk.PhotoImage(file=resource_path("res\\5.png"))
        self.id_trident = self.canvas_bg_trident.create_image(250,280, image=self.image_trident)
        self.seijaid_trident = self.canvas_bg_trident.create_image(680,430, image=self.image_seija5)

        self.LFselect_trident = tk.LabelFrame(self.tab_trident, text='选择三叉戟：', padx=5,pady=5)
        self.LFselect_trident.place(x=10,y=20)

        self.trident_langs = [('三叉戟','minecraft:trident')]
        self.str_trident = tk.StringVar()
        self.str_trident.set('0')
        for name_zh,name_en in self.trident_langs:
            self.trident = tk.Radiobutton(self.LFselect_trident, text=name_zh, variable=self.str_trident, value=name_en, command=self.string_splicing_trident)
            self.trident.pack(anchor='w')

        self.LFselect_trident_enchant = tk.LabelFrame(self.tab_trident, text='选择附魔：', padx=5,pady=5)
        self.LFselect_trident_enchant.place(x=430,y=20)

        self.trident_enchant_langs = [('忠诚','minecraft:loyalty',0,0),
                                  ('穿刺','minecraft:impaling',1,0),
                                  ('激流','minecraft:riptide',2,0),
                                  ('引雷','minecraft:channeling',3,0),
                                  ('经验修补','minecraft:mending',4,0),
                                  ('耐久','minecraft:unbreaking',5,0)]
        self.array_trident_enchant = []
        self.array_trident_enchantlv = []

        for name_zh,name_en,posx,posy in self.trident_enchant_langs:
            self.Fselect_trident_enchant = tk.Frame(self.LFselect_trident_enchant)
            self.Fselect_trident_enchant.grid(row=posx, column=posy, padx=5,pady=5, sticky=tk.W)

            self.str_trident_enchant = tk.StringVar()
            self.str_trident_enchant.set("0")
            self.array_trident_enchant.append(self.str_trident_enchant)
            self.trident_enchant = tk.Checkbutton(self.Fselect_trident_enchant, text=name_zh, onvalue=name_en, variable=self.array_trident_enchant[-1], command=self.string_splicing_trident)
            self.trident_enchant.pack(side="left")

            self.str_trident_enchantlv = tk.IntVar()
            self.str_trident_enchantlv.set(0)
            self.array_trident_enchantlv.append(self.str_trident_enchantlv)
            self.trident_enchantlv = tk.Spinbox(self.Fselect_trident_enchant, from_=1, to=10, increment=1, textvariable=self.array_trident_enchantlv[-1], width=2, command=self.string_splicing_trident)
            self.trident_enchantlv.pack(side="left")

        self.LFselect_trident_extra = tk.LabelFrame(self.tab_trident, text='选择额外属性：', padx=5,pady=5)
        self.LFselect_trident_extra.place(x=10,y=250)
        self.str_trident_extra = tk.StringVar()
        self.str_trident_extra.set("0")
        self.trident_extra = tk.Checkbutton(self.LFselect_trident_extra, text='不损', onvalue="Unbreakable:1", variable=self.str_trident_extra, command=self.string_splicing_trident)
        self.trident_extra.pack()

        self.LFselect_trident_name = tk.LabelFrame(self.tab_trident, text='输入三叉戟名称', padx=5,pady=5)
        self.LFselect_trident_name.place(x=10,y=350)
        self.str_trident_name = tk.StringVar()
        self.str_trident_name.set("")
        self.Text_trident_name = tk.Entry(self.LFselect_trident_name, textvariable=self.str_trident_name, width=30, insertwidth=1)
        self.Text_trident_name.pack()
        self.Text_trident_name.bind("<KeyRelease>", self.string_splicing_trident)

        self.Text_trident = tk.Text(self.tab_trident,width=80,height=5)
        self.Text_trident.place(x=10,y=410)
        self.button_trident = tk.Button(self.tab_trident,text='生成/Give命令',width=15, command=self.output_trident)
        self.button_trident.place(x=10,y=510)

        self.str_num_trident = tk.StringVar()
        self.str_num_trident.set('当前命令包含的字符个数为：')
        self.canvas_str_num_trident = self.canvas_bg_trident.create_text(10,495, text=self.str_num_trident.get(), anchor = tk.W)

    def create_widgets_fishingbobber(self):
        self.tab_fishingbobber = tk.Frame(self.tab_main)
        self.tab_fishingbobber.place(x=500,y=30)
        self.tab_main.add(self.tab_fishingbobber,text='钓鱼竿')

        self.canvas_bg_fishingbobber = tk.Canvas(self.tab_fishingbobber, width=800, height=600, highlightthickness=0, borderwidth=0)
        self.canvas_bg_fishingbobber.place(x=0, y=0)
        self.bgid_fishingbobber = self.canvas_bg_fishingbobber.create_image(385,263, image=self.bg_image)
        self.image_fishingbobber = tk.PhotoImage(file=resource_path("res\\fishingbobber.png"))
        self.image_seija6 = tk.PhotoImage(file=resource_path("res\\6.png"))
        self.id_fishingbobber = self.canvas_bg_fishingbobber.create_image(250,280, image=self.image_fishingbobber)
        self.seijaid_fishingbobber = self.canvas_bg_fishingbobber.create_image(680,430, image=self.image_seija6)

        self.LFselect_fishingbobber = tk.LabelFrame(self.tab_fishingbobber, text='选择钓鱼竿：', padx=5,pady=5)
        self.LFselect_fishingbobber.place(x=10,y=20)

        self.fishingbobber_langs = [('钓鱼竿','minecraft:fishingbobber')]
        self.str_fishingbobber = tk.StringVar()
        self.str_fishingbobber.set('0')
        for name_zh,name_en in self.fishingbobber_langs:
            self.fishingbobber = tk.Radiobutton(self.LFselect_fishingbobber, text=name_zh, variable=self.str_fishingbobber, value=name_en, command=self.string_splicing_fishingbobber)
            self.fishingbobber.pack(anchor='w')

        self.LFselect_fishingbobber_enchant = tk.LabelFrame(self.tab_fishingbobber, text='选择附魔：', padx=5,pady=5)
        self.LFselect_fishingbobber_enchant.place(x=430,y=20)

        self.fishingbobber_enchant_langs = [('海之眷顾','minecraft.luck_of_the_sea',0,0),
                                  ('饵钓','minecraft.lure',1,0),
                                  ('经验修补','minecraft:mending',2,0),
                                  ('耐久','minecraft:unbreaking',3,0)]
        self.array_fishingbobber_enchant = []
        self.array_fishingbobber_enchantlv = []

        for name_zh,name_en,posx,posy in self.fishingbobber_enchant_langs:
            self.Fselect_fishingbobber_enchant = tk.Frame(self.LFselect_fishingbobber_enchant)
            self.Fselect_fishingbobber_enchant.grid(row=posx, column=posy, padx=5,pady=5, sticky=tk.W)

            self.str_fishingbobber_enchant = tk.StringVar()
            self.str_fishingbobber_enchant.set("0")
            self.array_fishingbobber_enchant.append(self.str_fishingbobber_enchant)
            self.fishingbobber_enchant = tk.Checkbutton(self.Fselect_fishingbobber_enchant, text=name_zh, onvalue=name_en, variable=self.array_fishingbobber_enchant[-1], command=self.string_splicing_fishingbobber)
            self.fishingbobber_enchant.pack(side="left")

            self.str_fishingbobber_enchantlv = tk.IntVar()
            self.str_fishingbobber_enchantlv.set(0)
            self.array_fishingbobber_enchantlv.append(self.str_fishingbobber_enchantlv)
            self.fishingbobber_enchantlv = tk.Spinbox(self.Fselect_fishingbobber_enchant, from_=1, to=10, increment=1, textvariable=self.array_fishingbobber_enchantlv[-1], width=2, command=self.string_splicing_fishingbobber)
            self.fishingbobber_enchantlv.pack(side="left")

        self.LFselect_fishingbobber_extra = tk.LabelFrame(self.tab_fishingbobber, text='选择额外属性：', padx=5,pady=5)
        self.LFselect_fishingbobber_extra.place(x=10,y=250)
        self.str_fishingbobber_extra = tk.StringVar()
        self.str_fishingbobber_extra.set("0")
        self.fishingbobber_extra = tk.Checkbutton(self.LFselect_fishingbobber_extra, text='不损', onvalue="Unbreakable:1", variable=self.str_fishingbobber_extra, command=self.string_splicing_fishingbobber)
        self.fishingbobber_extra.pack()

        self.LFselect_fishingbobber_name = tk.LabelFrame(self.tab_fishingbobber, text='输入钓鱼竿名称', padx=5,pady=5)
        self.LFselect_fishingbobber_name.place(x=10,y=350)
        self.str_fishingbobber_name = tk.StringVar()
        self.str_fishingbobber_name.set("")
        self.Text_fishingbobber_name = tk.Entry(self.LFselect_fishingbobber_name, textvariable=self.str_fishingbobber_name, width=30, insertwidth=1)
        self.Text_fishingbobber_name.pack()
        self.Text_fishingbobber_name.bind("<KeyRelease>", self.string_splicing_fishingbobber)

        self.Text_fishingbobber = tk.Text(self.tab_fishingbobber,width=80,height=5)
        self.Text_fishingbobber.place(x=10,y=410)
        self.button_fishingbobber = tk.Button(self.tab_fishingbobber,text='生成/Give命令',width=15, command=self.output_fishingbobber)
        self.button_fishingbobber.place(x=10,y=510)

        self.str_num_fishingbobber = tk.StringVar()
        self.str_num_fishingbobber.set('当前命令包含的字符个数为：')
        self.canvas_str_num_fishingbobber = self.canvas_bg_fishingbobber.create_text(10,495, text=self.str_num_fishingbobber.get(), anchor = tk.W)

    strlink_weapon1 = []
    strlink_weapon2 = ""
    strlink_weapon3 = []
    strlink_weapon4 = ""
    strlink_waepon_fin = ""

    def string_splicing_weapon(self, event=0):
        self.Text_weapon.delete(1.0,'end')
        #转录地址数组里的值
        array_enchant_str = []
        for str_ in self.array_weapon_enchant:
            array_enchant_str.append(str_.get())

        global strlink_weapon1
        global strlink_weapon2
        global strlink_weapon3
        global strlink_weapon4
        global strlink_waepon_fin
        index = 0
        #全局变量初始化
        self.strlink_weapon1 = []
        self.strlink_weapon2 = ""
        self.strlink_weapon3 = []
        self.strlink_weapon4 = ""
        self.strlink_waepon_fin = ""

        for str_ in self.array_weapon_enchant:
            if str_.get() != "0":
                index = array_enchant_str.index(str_.get())
                temp = '{id:"' + str_.get() + '",lvl:' + str(self.array_weapon_enchantlv[index].get()) + '}'
                self.strlink_weapon1.append(temp)

        if len(self.strlink_weapon1) != 0:
            self.strlink_weapon2 = 'Enchantments:['
            for str_ in self.strlink_weapon1:
                self.strlink_weapon2 = self.strlink_weapon2 + str_
                if str_ != self.strlink_weapon1[-1]:
                    self.strlink_weapon2 = self.strlink_weapon2 + ','
            self.strlink_weapon2 = self.strlink_weapon2 + ']'

        if self.str_weapon_extra.get() != "0":
            self.strlink_weapon3.append(self.str_weapon_extra.get())
        if self.str_weapon_name.get() != "":
            self.strlink_weapon3.append('display:{Name:"[{\\"text\":\\"%s\\"}]"}' %(self.str_weapon_name.get()))
        if self.strlink_weapon2 != "":
            self.strlink_weapon3.append(self.strlink_weapon2)

        for str_ in self.strlink_weapon3:
            self.strlink_weapon4 = self.strlink_weapon4 + str_
            if str_ != self.strlink_weapon3[-1]:
                self.strlink_weapon4 = self.strlink_weapon4+ ','

        if self.str_weapon.get() != "0":
            self.strlink_waepon_fin = '/give @s ' + self.str_weapon.get() + '{' + self.strlink_weapon4 + '} 1'

    strlink_tool1 = []
    strlink_tool2 = ""
    strlink_tool3 = []
    strlink_tool4 = ""
    strlink_tool_fin = ""

    def string_splicing_tool(self, event=0):
        self.Text_tool.delete(1.0,'end')

        array_enchant_str = []
        for str_ in self.array_tool_enchant:
            array_enchant_str.append(str_.get())

        global strlink_tool1
        global strlink_tool2
        global strlink_tool3
        global strlink_tool4
        global strlink_tool_fin
        index = 0

        self.strlink_tool1 = []
        self.strlink_tool2 = ""
        self.strlink_tool3 = []
        self.strlink_tool4 = ""
        self.strlink_tool_fin = ""

        for str_ in self.array_tool_enchant:
            if str_.get() != "0":
                index = array_enchant_str.index(str_.get())
                temp = '{id:"' + str_.get() + '",lvl:' + str(self.array_tool_enchantlv[index].get()) + '}'
                self.strlink_tool1.append(temp)

        if len(self.strlink_tool1) != 0:
            self.strlink_tool2 = 'Enchantments:['
            for str_ in self.strlink_tool1:
                self.strlink_tool2 = self.strlink_tool2 + str_
                if str_ != self.strlink_tool1[-1]:
                    self.strlink_tool2 = self.strlink_tool2 + ','
            self.strlink_tool2 = self.strlink_tool2 + ']'

        if self.str_tool_extra.get() != "0":
            self.strlink_tool3.append(self.str_tool_extra.get())
        if self.str_tool_name.get() != "":
            self.strlink_tool3.append('display:{Name:"[{\\"text\":\\"%s\\"}]"}' %(self.str_tool_name.get()))
        if self.strlink_tool2 != "":
            self.strlink_tool3.append(self.strlink_tool2)

        for str_ in self.strlink_tool3:
            self.strlink_tool4 = self.strlink_tool4 + str_
            if str_ != self.strlink_tool3[-1]:
                self.strlink_tool4 = self.strlink_tool4+ ','

        if self.str_tool.get() != "0":
            self.strlink_tool_fin = '/give @s ' + self.str_tool.get() + '{' + self.strlink_tool4 + '} 1'

    strlink_armor1 = []
    strlink_armor2 = ""
    strlink_armor3 = []
    strlink_armor4 = ""
    strlink_armor_fin = ""

    def string_splicing_armor(self, event=0):
        self.Text_armor.delete(1.0,'end')

        array_enchant_str = []
        for str_ in self.array_armor_enchant:
            array_enchant_str.append(str_.get())

        global strlink_armor1
        global strlink_armor2
        global strlink_armor3
        global strlink_armor4
        global strlink_armor_fin
        index = 0

        self.strlink_armor1 = []
        self.strlink_armor2 = ""
        self.strlink_armor3 = []
        self.strlink_armor4 = ""
        self.strlink_armor_fin = ""

        for str_ in self.array_armor_enchant:
            if str_.get() != "0":
                index = array_enchant_str.index(str_.get())
                temp = '{id:"' + str_.get() + '",lvl:' + str(self.array_armor_enchantlv[index].get()) + '}'
                self.strlink_armor1.append(temp)

        if len(self.strlink_armor1) != 0:
            self.strlink_armor2 = 'Enchantments:['
            for str_ in self.strlink_armor1:
                self.strlink_armor2 = self.strlink_armor2 + str_
                if str_ != self.strlink_armor1[-1]:
                    self.strlink_armor2 = self.strlink_armor2 + ','
            self.strlink_armor2 = self.strlink_armor2 + ']'

        if self.str_armor_extra.get() != "0":
            self.strlink_armor3.append(self.str_armor_extra.get())
        if self.str_armor_name.get() != "":
            self.strlink_armor3.append('display:{Name:"[{\\"text\":\\"%s\\"}]"}' %(self.str_armor_name.get()))
        if self.strlink_armor2 != "":
            self.strlink_armor3.append(self.strlink_armor2)

        for str_ in self.strlink_armor3:
            self.strlink_armor4 = self.strlink_armor4 + str_
            if str_ != self.strlink_armor3[-1]:
                self.strlink_armor4 = self.strlink_armor4+ ','

        if self.str_armor.get() != "0":
            self.strlink_armor_fin = '/give @s ' + self.str_armor.get() + '{' + self.strlink_armor4 + '} 1'

    strlink_bow1 = []
    strlink_bow2 = ""
    strlink_bow3 = []
    strlink_bow4 = ""
    strlink_bow_fin = ""

    def string_splicing_bow(self, event=0):
        self.Text_bow.delete(1.0,'end')

        array_enchant_str = []
        for str_ in self.array_bow_enchant:
            array_enchant_str.append(str_.get())

        global strlink_bow1
        global strlink_bow2
        global strlink_bow3
        global strlink_bow4
        global strlink_bow_fin
        index = 0

        self.strlink_bow1 = []
        self.strlink_bow2 = ""
        self.strlink_bow3 = []
        self.strlink_bow4 = ""
        self.strlink_bow_fin = ""

        for str_ in self.array_bow_enchant:
            if str_.get() != "0":
                index = array_enchant_str.index(str_.get())
                temp = '{id:"' + str_.get() + '",lvl:' + str(self.array_bow_enchantlv[index].get()) + '}'
                self.strlink_bow1.append(temp)

        if len(self.strlink_bow1) != 0:
            self.strlink_bow2 = 'Enchantments:['
            for str_ in self.strlink_bow1:
                self.strlink_bow2 = self.strlink_bow2 + str_
                if str_ != self.strlink_bow1[-1]:
                    self.strlink_bow2 = self.strlink_bow2 + ','
            self.strlink_bow2 = self.strlink_bow2 + ']'

        if self.str_bow_extra.get() != "0":
            self.strlink_bow3.append(self.str_bow_extra.get())
        if self.str_bow_name.get() != "":
            self.strlink_bow3.append('display:{Name:"[{\\"text\":\\"%s\\"}]"}' %(self.str_bow_name.get()))
        if self.strlink_bow2 != "":
            self.strlink_bow3.append(self.strlink_bow2)

        for str_ in self.strlink_bow3:
            self.strlink_bow4 = self.strlink_bow4 + str_
            if str_ != self.strlink_bow3[-1]:
                self.strlink_bow4 = self.strlink_bow4+ ','

        if self.str_bow.get() != "0":
            self.strlink_bow_fin = '/give @s ' + self.str_bow.get() + '{' + self.strlink_bow4 + '} 1'

    strlink_crossbow1 = []
    strlink_crossbow2 = ""
    strlink_crossbow3 = []
    strlink_crossbow4 = ""
    strlink_crossbow_fin = ""

    def string_splicing_crossbow(self, event=0):
        self.Text_crossbow.delete(1.0,'end')

        array_enchant_str = []
        for str_ in self.array_crossbow_enchant:
            array_enchant_str.append(str_.get())

        global strlink_crossbow1
        global strlink_crossbow2
        global strlink_crossbow3
        global strlink_crossbow4
        global strlink_crossbow_fin
        index = 0

        self.strlink_crossbow1 = []
        self.strlink_crossbow2 = ""
        self.strlink_crossbow3 = []
        self.strlink_crossbow4 = ""
        self.strlink_crossbow_fin = ""

        for str_ in self.array_crossbow_enchant:
            if str_.get() != "0":
                index = array_enchant_str.index(str_.get())
                temp = '{id:"' + str_.get() + '",lvl:' + str(self.array_crossbow_enchantlv[index].get()) + '}'
                self.strlink_crossbow1.append(temp)

        if len(self.strlink_crossbow1) != 0:
            self.strlink_crossbow2 = 'Enchantments:['
            for str_ in self.strlink_crossbow1:
                self.strlink_crossbow2 = self.strlink_crossbow2 + str_
                if str_ != self.strlink_crossbow1[-1]:
                    self.strlink_crossbow2 = self.strlink_crossbow2 + ','
            self.strlink_crossbow2 = self.strlink_crossbow2 + ']'

        if self.str_crossbow_extra.get() != "0":
            self.strlink_crossbow3.append(self.str_crossbow_extra.get())
        if self.str_crossbow_name.get() != "":
            self.strlink_crossbow3.append('display:{Name:"[{\\"text\":\\"%s\\"}]"}' %(self.str_crossbow_name.get()))
        if self.strlink_crossbow2 != "":
            self.strlink_crossbow3.append(self.strlink_crossbow2)

        for str_ in self.strlink_crossbow3:
            self.strlink_crossbow4 = self.strlink_crossbow4 + str_
            if str_ != self.strlink_crossbow3[-1]:
                self.strlink_crossbow4 = self.strlink_crossbow4+ ','

        if self.str_crossbow.get() != "0":
            self.strlink_crossbow_fin = '/give @s ' + self.str_crossbow.get() + '{' + self.strlink_crossbow4 + '} 1'

    strlink_trident1 = []
    strlink_trident2 = ""
    strlink_trident3 = []
    strlink_trident4 = ""
    strlink_trident_fin = ""

    def string_splicing_trident(self, event=0):
        self.Text_trident.delete(1.0,'end')

        array_enchant_str = []
        for str_ in self.array_trident_enchant:
            array_enchant_str.append(str_.get())

        global strlink_trident1
        global strlink_trident2
        global strlink_trident3
        global strlink_trident4
        global strlink_trident_fin
        index = 0

        self.strlink_trident1 = []
        self.strlink_trident2 = ""
        self.strlink_trident3 = []
        self.strlink_trident4 = ""
        self.strlink_trident_fin = ""

        for str_ in self.array_trident_enchant:
            if str_.get() != "0":
                index = array_enchant_str.index(str_.get())
                temp = '{id:"' + str_.get() + '",lvl:' + str(self.array_trident_enchantlv[index].get()) + '}'
                self.strlink_trident1.append(temp)

        if len(self.strlink_trident1) != 0:
            self.strlink_trident2 = 'Enchantments:['
            for str_ in self.strlink_trident1:
                self.strlink_trident2 = self.strlink_trident2 + str_
                if str_ != self.strlink_trident1[-1]:
                    self.strlink_trident2 = self.strlink_trident2 + ','
            self.strlink_trident2 = self.strlink_trident2 + ']'

        if self.str_trident_extra.get() != "0":
            self.strlink_trident3.append(self.str_trident_extra.get())
        if self.str_trident_name.get() != "":
            self.strlink_trident3.append('display:{Name:"[{\\"text\":\\"%s\\"}]"}' %(self.str_trident_name.get()))
        if self.strlink_trident2 != "":
            self.strlink_trident3.append(self.strlink_trident2)

        for str_ in self.strlink_trident3:
            self.strlink_trident4 = self.strlink_trident4 + str_
            if str_ != self.strlink_trident3[-1]:
                self.strlink_trident4 = self.strlink_trident4+ ','

        if self.str_trident.get() != "0":
            self.strlink_trident_fin = '/give @s ' + self.str_trident.get() + '{' + self.strlink_trident4 + '} 1'

    strlink_fishingbobber1 = []
    strlink_fishingbobber2 = ""
    strlink_fishingbobber3 = []
    strlink_fishingbobber4 = ""
    strlink_fishingbobber_fin = ""

    def string_splicing_fishingbobber(self, event=0):
        self.Text_fishingbobber.delete(1.0,'end')

        array_enchant_str = []
        for str_ in self.array_fishingbobber_enchant:
            array_enchant_str.append(str_.get())

        global strlink_fishingbobber1
        global strlink_fishingbobber2
        global strlink_fishingbobber3
        global strlink_fishingbobber4
        global strlink_fishingbobber_fin
        index = 0

        self.strlink_fishingbobber1 = []
        self.strlink_fishingbobber2 = ""
        self.strlink_fishingbobber3 = []
        self.strlink_fishingbobber4 = ""
        self.strlink_fishingbobber_fin = ""

        for str_ in self.array_fishingbobber_enchant:
            if str_.get() != "0":
                index = array_enchant_str.index(str_.get())
                temp = '{id:"' + str_.get() + '",lvl:' + str(self.array_fishingbobber_enchantlv[index].get()) + '}'
                self.strlink_fishingbobber1.append(temp)

        if len(self.strlink_fishingbobber1) != 0:
            self.strlink_fishingbobber2 = 'Enchantments:['
            for str_ in self.strlink_fishingbobber1:
                self.strlink_fishingbobber2 = self.strlink_fishingbobber2 + str_
                if str_ != self.strlink_fishingbobber1[-1]:
                    self.strlink_fishingbobber2 = self.strlink_fishingbobber2 + ','
            self.strlink_fishingbobber2 = self.strlink_fishingbobber2 + ']'

        if self.str_fishingbobber_extra.get() != "0":
            self.strlink_fishingbobber3.append(self.str_fishingbobber_extra.get())
        if self.str_fishingbobber_name.get() != "":
            self.strlink_fishingbobber3.append('display:{Name:"[{\\"text\":\\"%s\\"}]"}' %(self.str_fishingbobber_name.get()))
        if self.strlink_fishingbobber2 != "":
            self.strlink_fishingbobber3.append(self.strlink_fishingbobber2)

        for str_ in self.strlink_fishingbobber3:
            self.strlink_fishingbobber4 = self.strlink_fishingbobber4 + str_
            if str_ != self.strlink_fishingbobber3[-1]:
                self.strlink_fishingbobber4 = self.strlink_fishingbobber4+ ','

        if self.str_fishingbobber.get() != "0":
            self.strlink_fishingbobber_fin = '/give @s ' + self.str_fishingbobber.get() + '{' + self.strlink_fishingbobber4 + '} 1'

    def output_weapon(self):
        global strlink_waepon_fin
        self.Text_weapon.delete(1.0,'end')
        self.Text_weapon.insert(1.0,self.strlink_waepon_fin)
        self.str_num_weapon.set('当前命令包含的字符个数为：%s' %(len(self.strlink_waepon_fin)))
        self.canvas_bg_weapon.delete(self.canvas_str_num_weapon)
        self.canvas_str_num_weapon = self.canvas_bg_weapon.create_text(10,495, text=self.str_num_weapon.get(), anchor = tk.W)

    def output_tool(self):
        global strlink_tool_fin
        self.Text_tool.delete(1.0,'end')
        self.Text_tool.insert(1.0,self.strlink_tool_fin)
        self.str_num_tool.set('当前命令包含的字符个数为：%s' %(len(self.strlink_tool_fin)))
        self.canvas_bg_tool.delete(self.canvas_str_num_tool)
        self.canvas_str_num_tool = self.canvas_bg_tool.create_text(10,495, text=self.str_num_tool.get(), anchor = tk.W)

    def output_armor(self):
        global strlink_armor_fin
        self.Text_armor.delete(1.0,'end')
        self.Text_armor.insert(1.0,self.strlink_armor_fin)
        self.str_num_armor.set('当前命令包含的字符个数为：%s' %(len(self.strlink_armor_fin)))
        self.canvas_bg_armor.delete(self.canvas_str_num_armor)
        self.canvas_str_num_armor = self.canvas_bg_armor.create_text(10,495, text=self.str_num_armor.get(), anchor = tk.W)
    def output_bow(self):
        global strlink_bow_fin
        self.Text_bow.delete(1.0,'end')
        self.Text_bow.insert(1.0,self.strlink_bow_fin)
        self.str_num_bow.set('当前命令包含的字符个数为：%s' %(len(self.strlink_bow_fin)))
        self.canvas_bg_bow.delete(self.canvas_str_num_bow)
        self.canvas_str_num_bow = self.canvas_bg_bow.create_text(10,495, text=self.str_num_bow.get(), anchor = tk.W)

    def output_crossbow(self):
        global strlink_crossbow_fin
        self.Text_crossbow.delete(1.0,'end')
        self.Text_crossbow.insert(1.0,self.strlink_crossbow_fin)
        self.str_num_crossbow.set('当前命令包含的字符个数为：%s' %(len(self.strlink_crossbow_fin)))
        self.canvas_bg_crossbow.delete(self.canvas_str_num_crossbow)
        self.canvas_str_num_crossbow = self.canvas_bg_crossbow.create_text(10,495, text=self.str_num_crossbow.get(), anchor = tk.W)

    def output_trident(self):
        global strlink_trident_fin
        self.Text_trident.delete(1.0,'end')
        self.Text_trident.insert(1.0,self.strlink_trident_fin)
        self.str_num_trident.set('当前命令包含的字符个数为：%s' %(len(self.strlink_trident_fin)))
        self.canvas_bg_trident.delete(self.canvas_str_num_trident)
        self.canvas_str_num_trident = self.canvas_bg_trident.create_text(10,495, text=self.str_num_trident.get(), anchor = tk.W)

    def output_fishingbobber(self):
        global strlink_fishingbobber_fin
        self.Text_fishingbobber.delete(1.0,'end')
        self.Text_fishingbobber.insert(1.0,self.strlink_fishingbobber_fin)
        self.str_num_fishingbobber.set('命令包含的字符个数为：%s' %(len(self.strlink_fishingbobber_fin)))
        self.canvas_bg_fishingbobber.delete(self.canvas_str_num_fishingbobber)
        self.canvas_str_num_fishingbobber = self.canvas_bg_fishingbobber.create_text(10,495, text=self.str_num_fishingbobber.get(), anchor = tk.W)

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = tk.Tk()
root.title("MC自定义装备指令生成器 by YBChun")
root.geometry('800x600+10+10')
root.iconbitmap(resource_path("res\\logo.ico"))
root.resizable(0,0)
app =  Application(master=root)
app.mainloop()