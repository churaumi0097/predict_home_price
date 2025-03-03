from django.db import models
from multiselectfield import MultiSelectField


class Post(models.Model):
    AREA_CHOICES = [
    ('北区', '北区'),
    ('中央区', '中央区'),
    ('渋谷区', '渋谷区'),
    ('杉並区', '杉並区'),
    ('葛飾区', '葛飾区'),
    ('荒川区', '荒川区'),
    ('練馬区', '練馬区'),
    ('目黒区', '目黒区'),
    ('文京区', '文京区'),
    ('板橋区', '板橋区'),
    ('大田区', '大田区'),
    ('江戸川区', '江戸川区'),
    ('港区', '港区'),
    ('墨田区', '墨田区'),
    ('新宿区', '新宿区'),
    ('中野区', '中野区'),
    ('豊島区', '豊島区'),
    ('台東区', '台東区'),
    ('足立区', '足立区'),
    ('世田谷区', '世田谷区'),
    ('江東区', '江東区'),
    ('品川区', '品川区'),
    ('千代田区', '千代田区'),
    ]

    ROOM_CHOICES = [
        ('１部屋', [
            ('1K', '1K'),
            ('1R', '1R'),
            ('1DK', '1DK'),
            ('1LDK', '1LDK'),
            ('1K+S(納戸)', '1K+S(納戸)'),
            ('1LDK+S(納戸)', '1LDK+S(納戸)'),
            ('1DK+S(納戸)', '1DK+S(納戸)'),
            ('1LK+S(納戸)', '1LK+S(納戸)'),
        ]),
        ('２部屋', [
            ('2K', '2K'),
            ('2DK', '2DK'),
            ('2LDK', '2LDK'),
            ('2K+S(納戸)', '2K+S(納戸)'),
            ('2DK+S(納戸)', '2DK+S(納戸)'),
            ('2LDK+S(納戸)', '2LDK+S(納戸)'),
        ]),
        ('３部屋', [
            ('3K', '3K'),
            ('3DK', '3DK'),
            ('3LDK', '3LDK'),
            ('3K+S(納戸)', '3K+S(納戸)'),
            ('3DK+S(納戸)', '3DK+S(納戸)'),
            ('3LDK+S(納戸)', '3LDK+S(納戸)'),
        ]),
        ('４部屋以上', [
            ('4K', '4K'),
            ('4DK', '4DK'),
            ('4LDK', '4LDK'),
            ('4LDK+S(納戸)', '4LDK+S(納戸)'),
            ('5K', '5K'),
            ('5DK', '5DK'),
            ('5LDK', '5LDK'),
            ('5DK+S(納戸)', '5DK+S(納戸)'),
            ('5LDK+S(納戸)', '5LDK+S(納戸)'),
            ('6LDK', '6LDK'),
        ]),
    ]
    STRUCTURE_CHOICES = [
    ('RC（鉄筋コンクリート）', 'RC（鉄筋コンクリート）'),
    ('鉄骨造', '鉄骨造'),
    ('木造', '木造'),
    ('SRC（鉄骨鉄筋コンクリート）', 'SRC（鉄骨鉄筋コンクリート）'),
    ('軽量鉄骨', '軽量鉄骨'),
    ('ALC（軽量気泡コンクリート）', 'ALC（軽量気泡コンクリート）'),
    ('その他', 'その他'),
    ('PC（プレキャスト・コンクリート（鉄筋コンクリート））', 'PC（プレキャスト・コンクリート（鉄筋コンクリート））'),
    ('HPC（プレキャスト・コンクリート（重量鉄骨））', 'HPC（プレキャスト・コンクリート（重量鉄骨））'),
    ('ブロック', 'ブロック'),
    ]
    TOILET_CHOICES = [
        ('共同トイレ', '共同トイレ'),
        ('専用トイレ', '専用トイレ'),
    ]
    BATH_CHOICES = [
        ('バスなし', 'バスなし'),
        ('専用バス', '専用バス'),
        ('共同バス', '共同バス'),
        ('シャワー', 'シャワー'),
    ]

    ADD_BT_CHOICES = [
        ('追焚機能', '追焚機能'),
        ('浴室乾燥機', '浴室乾燥機'),
        ('温水洗浄便座', '温水洗浄便座'),
        ('脱衣所', '脱衣所'),
    ]

    KITCHEN_CHOICES = [
        ('システムキッチン', 'システムキッチン'),
        ('カウンターキッチン', 'カウンターキッチン'),
        ('独立キッチン', '独立キッチン'),
        ('L字キッチン', 'L字キッチン'),
    ]

    CONRO_CHOICES = [
        ('ガスコンロ', 'ガスコンロ'),
        ('電気コンロ', '電気コンロ'),
        ('IHコンロ', 'IHコンロ'),
    ]
    STORAGE_CHOICES = [
        ('床下収納', '床下収納'),
        ('ウォークインクローゼット', 'ウォークインクローゼット'),
        ('シューズボックス', 'シューズボックス'),
    ]

    AIR_CHOICES = [
        ('エアコン付', 'エアコン付'),
        ('床暖房', '床暖房'),
    ]

    BARRIER_FREE_CHOICES = [
        ('エレベーター', 'エレベーター'),
        ('バリアフリー', 'バリアフリー'),
    ]

    COMFORT_CHOICES = [
        ('フローリング', 'フローリング'),
        ('防音室', '防音室'),
    ]

    BUILDING_CHOICES = [
        ('ロフト付き', 'ロフト付き'),
        ('タイル張り', 'タイル張り'),
    ]

    OUTDOOR_CHOICES = [
        ('バルコニー', 'バルコニー'),
        ('ルーフバルコニー', 'ルーフバルコニー'),
    ]

    ENERGY_CHOICES = [
        ('都市ガス', '都市ガス'),
        ('プロパンガス', 'プロパンガス'),
    ]

    GARBAGE_CHOICES = [
        ('敷地内ごみ置き場', '敷地内ごみ置き場'),
    ]

    WATER_CHOICES = [
        ('公営水道', '公営水道'),
    ]

    area = models.CharField(
        max_length=10,
        choices=AREA_CHOICES,
        default="北区",
        verbose_name="地区",
    )
    floor_num = models.PositiveIntegerField(
        default = 1,
        verbose_name = "階数",
        blank = True,
        null = True,
    )
    all_floor_num = models.PositiveIntegerField(
        default = 1,
        verbose_name = "建物の階数",
        blank = True,
        null = True,
    )
    floor_plan = models.CharField(
        max_length = 30,
        choices=ROOM_CHOICES,
        verbose_name="間取り",
    )
    room_size = models.PositiveIntegerField(
        default = 10,
        verbose_name = "部屋の広さ"
    )
    structure = models.CharField(
        max_length = 80,
        choices=STRUCTURE_CHOICES,
        verbose_name="建物構造",
    )
    const_year = models.PositiveIntegerField(
        default = 5,
        verbose_name = "築年数"
    )
    station = models.PositiveIntegerField(
        default = 1,
        verbose_name = "駅までの時間",
    )
    sun = models.BooleanField(
        default=True,
        verbose_name="日当たり",
        blank = True,
        null = True,
    )
    bath = models.CharField(
        max_length=100,
        choices=BATH_CHOICES,
        verbose_name="バス",
        blank = True,
        null = True,
    )
    toilet = models.CharField(
        max_length=100,
        choices=TOILET_CHOICES,
        verbose_name="トイレ",
        blank = True,
        null = True,
    )
    bath_toilet = models.BooleanField(
        default=True,
        verbose_name="風呂トイレ別",
        blank=True,
    )
    add_bt = MultiSelectField(
        choices=ADD_BT_CHOICES,
        verbose_name="バストイレ追加機能",
        blank = True,
        null = True,
    )
    kitchen = MultiSelectField(
        choices=KITCHEN_CHOICES,
        verbose_name="キッチン",
        blank = True,
        null = True,
    )
    conro = MultiSelectField(
        choices=CONRO_CHOICES,
        verbose_name="コンロ",
        blank = True,
        null = True,
    )
    conro_num = models.PositiveIntegerField(
        default = 1,
        verbose_name="コンロ数",
        blank=True,
    )
    storage = MultiSelectField(
        choices=STORAGE_CHOICES,
        verbose_name="収納",
        blank = True,
        null = True,
    )
    air_conditioning = MultiSelectField(
        choices=AIR_CHOICES,
        verbose_name="空調",
        blank = True,
        null = True,
    )
    barrier_free = MultiSelectField(
        choices=BARRIER_FREE_CHOICES,
        verbose_name="バリアフリー",
        blank = True,
        null = True,
    )
    comfort = MultiSelectField(
        choices=COMFORT_CHOICES,
        verbose_name="快適設備",
        blank = True,
        null = True,
    )
    building = MultiSelectField(
        choices=BUILDING_CHOICES,
        verbose_name="建物特長",
        blank = True,
        null = True,
    )
    outdoor = MultiSelectField(
        choices=OUTDOOR_CHOICES,
        verbose_name="屋外設備",
        blank = True,
        null = True,
    )
    energy = models.CharField(
        max_length=100,
        choices=ENERGY_CHOICES,
        verbose_name="エネルギー",
        blank = True,
        null = True,
    )
    garbage = models.CharField(
        choices=GARBAGE_CHOICES,
        max_length=100,
        verbose_name="ゴミ捨て場",
        blank = True,
        null = True,
    )
    water_supply = models.CharField(
        max_length=100,
        choices=WATER_CHOICES,
        verbose_name="水道",
        blank = True,
        null = True,
    )
    predict_price = models.FloatField(
        verbose_name = "予測価格",
        blank = True,
        null = True
    )
    def __str__(self):
        return f"{self.area} : {self.predict_price}"