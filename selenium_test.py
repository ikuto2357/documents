from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriverをセットアップ
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

# サイトにアクセス
url = "https://rensa.jp.net/seimeihandan"
driver.get(url)
time.sleep(2)

# 名前リスト
name_list = [
    ("渡部", "希"),  # 佐々木希（結婚後：渡部建の妻）
    ("東山", "佳乃"),  # 木村佳乃（結婚後：東山紀之の妻）
    ("石橋", "保奈美"),  # 鈴木保奈美（結婚後：石橋貴明の妻）
    ("田中", "美佐子"),  # 田中美佐子（結婚後：深沢邦之の妻）
    ("三浦", "りさ子"),  # 三浦りさ子（結婚後：三浦知良の妻）
    ("本木", "也哉子"),  # 内田也哉子（結婚後：本木雅弘の妻）
    ("堺", "美穂"),  # 菅野美穂（結婚後：堺雅人の妻）
    ("福山", "一恵"),  # 吹石一恵（結婚後：福山雅治の妻）
    ("中林", "結子"),  # 竹内結子（結婚後：中林大樹の妻）
    ("長谷川", "京子"),  # 旧姓：新藤京子（結婚後：長谷川博己の妻）
    ("片岡", "愛之助"),  # 旧姓：藤原紀香（結婚後：片岡愛之助の妻）
    ("森田", "千晶"),  # 宇多田ヒカル（結婚後：森田彰司の妻）
    ("玉山", "千明"),  # 栗山千明（結婚後：玉山鉄二の妻）
    ("井ノ原", "朝香"),  # 瀬戸朝香（結婚後：井ノ原快彦の妻）
    ("谷", "亮子"),  # 旧姓：田村亮子（結婚後：谷佳知の妻）
    ("本並", "桂里奈"),  # 旧姓：丸山桂里奈（結婚後：本並健治の妻）
    ("及川", "れい"),  # 檀れい（結婚後：及川光博の妻）
    ("矢部", "裕子"),  # 旧姓：青木裕子（結婚後：ナイナイ矢部浩之の妻）
    ("杉浦", "希美"),  # 旧姓：辻希美（結婚後：杉浦太陽の妻）
    ("市村", "涼子"),  # 旧姓：篠原涼子（結婚後：市村正親の妻）
]


for last_name, first_name in name_list:
    try:
        # XPath で姓・名を入力
        sei_input = driver.find_element(By.XPATH, "//*[@id='name']/p[1]/input")
        mei_input = driver.find_element(By.XPATH, "//*[@id='name']/p[2]/input")

        sei_input.clear()
        mei_input.clear()
        sei_input.send_keys(last_name)
        mei_input.send_keys(first_name)

        # XPath で判定ボタンをクリック
        judge_button = driver.find_element(
            By.XPATH, "//*[@id='seimei-fortune-form']/div[2]/input"
        )
        judge_button.click()

        time.sleep(2)  # ページ遷移待ち

        # XPath で結果を取得
        result_text = driver.find_element(
            By.XPATH,
            "//*[@id='post-25628']/section/div[1]/div[1]/div/div/div/div[4]/div/div/span[2]",
        ).text
        print(f"{last_name} {first_name} の診断結果: {result_text}")

        # 元のページに戻る
        driver.back()
        time.sleep(2)  # ページが戻るのを待つ

    except Exception as e:
        print(f"エラー: {e}")

# WebDriverを終了
driver.quit()
