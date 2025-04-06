了解です！  
以下に「知っておくと開発がかなり捗る」「ちょっとニッチだけど超便利」な Git コマンドやオプションを目的別にまとめました。  
**初心者向けの定番コマンドは省いて、実用的なTips中心**で紹介します。

---

## 🔄 状態の巻き戻し・復旧系

### 1. 直前のコミットまで戻す（作業ディレクトリも含めてリセット）
```bash
git reset --hard HEAD
```
- 作業中の変更をすべて破棄。
- **完全にクリーンな状態に戻したい時**に使える。

---

### 2. 直前のコミットだけ取り消す（内容は保持）
```bash
git reset --soft HEAD~1
```
- 直前のコミットを取り消して、ステージされた状態に戻す。
- つまり「コミット前の状態」に戻したい時に使える。

---

### 3. 特定のファイルだけ、前のコミットの状態に戻す
```bash
git checkout HEAD^ -- path/to/file
```
- そのファイルだけ、**1つ前の状態**に戻せる。
- `HEAD^` → 1つ前のコミット、`HEAD~2` → 2つ前。

---

### 4. コミット履歴をなかったことにする（reflog）
```bash
git reflog
```
```bash
git reset --hard <過去のHEAD>
```
- 「やばい、rebase や reset で消えた！」という時に使える救世主。
- `reflog`で過去の履歴がすべて見られる。

---

## 🚀 clone・pullの便利ワザ

### 5. 特定のブランチだけ clone（容量節約にもなる）
```bash
git clone --branch <branch-name> --single-branch <repo-url>
```
- 通常の clone は全ブランチ含むが、これで **必要なブランチだけ取得**。

---

### 6. 履歴も含めず最新だけ取得（超軽量 clone）
```bash
git clone --depth=1 <repo-url>
```
- **最新コミット1つだけ**取得。履歴は不要なときに便利。
- 例：CIツールでとりあえずビルドだけしたいときなど。

---

## 🧹 履歴やステージ整理

### 7. 複数のコミットをひとつにまとめる（squash）
```bash
git rebase -i HEAD~3
```
- 対話的に過去のコミットをまとめてクリーンに整える。
- 開発終盤で「PR用にきれいにしたい」時によく使う。

---

### 8. 直前のコミットをやり直す
```bash
git commit --amend
```
- メッセージ修正や、ファイル追加忘れのときに重宝。

---

## 🧪 ワンライナーで一括処理

### 9. ステージしてコミット・プッシュまで一発
```bash
git add . && git commit -m "fix: 修正" && git push
```
- 一連の操作をまとめてやりたい時のテンプレ。

---

### 10. ブランチを一括削除（ローカル or リモート追跡）
```bash
# ローカルの削除済みリモート追跡ブランチを削除
git fetch -p

# マージ済みのローカルブランチを削除（mainとdevelop以外）
git branch --merged | grep -v '\*' | grep -v 'main' | grep -v 'develop' | xargs git branch -d
```

---

## 🔍 差分・変更確認

### 11. 直近の変更を確認（行単位で）
```bash
git diff HEAD
```
- ステージされてない変更を確認。

---

### 12. コミットログをグラフ付きで表示（ブランチの関係が視覚的にわかる）
```bash
git log --oneline --graph --all --decorate
```

---

## その他：ちょっと便利

### 13. 現在のブランチ名だけ取得（スクリプト用）
```bash
git rev-parse --abbrev-ref HEAD
```

### 14. 作業ブランチの変更を stash して一時退避
```bash
git stash
```
```bash
git stash pop
```
- 緊急で別の作業に切り替える時に便利。

---

### 15. リモートの URL を変更
```bash
git remote set-url origin git@github.com:yourname/repo.git
```

---

必要であれば、目的別（「トラブル復旧系だけ」「履歴整理系だけ」）や、**GUI（GitHub Desktop / Sourcetree）でどう対応するか**もあわせてまとめられます。興味ありますか？