お疲れ様です。
とてもよくできていると思います！
アプリとして必要な機能をしっかり実装できていて良いと思います！
管理画面でlist_displayを使っていたり、細かいところまで意識できていてすごいです。
クラスベースビューも上手に使えていてコードも簡潔でいいと思います。

以下にいくつかポイントをあげます。

## Userモデルについて

・Userモデルの名前はCustomUserではなくUserの方が一般的だそうです。
これは教材がCustomUserで作れと指示していたので、そうしてもらっただけだと思うのでごめんなさい。

・プロフィールアイコンのImageFiledについて、defaultの画像を設定するとより良いと感じました。また、upload_toはmedia_localというフォルダから見た相対的なパスになるので、media_localと入力するのではなく、プロフィールアイコンの画像を格納するフォルダを作るのが良いと思います。
実際、ローカルのフォルダ構成が、media_local/media_localというふうになっているかと思います。

・新たなfieldとしてcreated_atというfieldを設定してくれていますが、実はAbstractUserにdate_joinedというfieldがあり、それを継承している
ので、実は自作しなくても大丈夫です！

```
date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
```
というfieldが作られています。

## Talkモデルについて

・Talkモデルのfiledで、send_userとreceive_userというfieldについて、senderやreceiverにすると、より簡潔で他の人にもわかりやすいと個人的に感じました。

・send_userとreceive_user、talk_atについて、null=Trueとなっていますが、送信者と受信者が存在しないことはあり得ないので、null=Falseだと思います。
デフォルトではnull=Falseなので、書かなくても大丈夫です！

## モデル全体について

実は、verbose_nameというフィールドオプション(null=とかupload_toとかfieldごとに設定する項目のこと)があり、それを記述するとコードが読みやすくなるので、ぜひ記述すると良いと思います。人間用に、これが何のフィールドかを表します。

## myapp/urls.pyについて

実は、名前空間という概念があり、これを設定するとプロジェクトに複数アプリがあるときに、url名の名前の衝突を回避することができるのでこれを設定するのがおすすめです。

[参考](https://qiita.com/KI1208/items/6e2047372f775bbb6905)

## クラスベースビュー(CBV)におけるユーザーモデルの扱いについて

さまざまなビューで、model=CustomUserと指定しているところを、get_user_model()を用いると、ユーザーモデルを変更したときに、一つ一つのビューを書き換えなくて良くなるのでおすすめです！

[参考](https://qiita.com/Quest_love33/items/77c5cbf3acd2c09edd0a)

[課題1の解答例](https://github.com/AkaDeMiA-Kyoto/intern_chat_app/blob/kadai1_sample/myapp/views.py)
も、そのように書いているので参考にしてみてください。

## ログインビューにおけるリダイレクト処理において

これもまた発展的な内容なのですが、ログイン済みのユーザーがログイン画面に訪れられるのはあまり良い仕様ではないです。
実は、LoginViewには、redirect_authenticated_user=True と設定することでこの処理を自動で設定できるので試してみてください！

## Q関数について

orは|が必要なのですが、andに関しては、&を使わずとも,で並列することで「かつ」を表すことができます。

## 会員登録フォームについて

UserCreationFormがModelFormを拡張したものなので、自分で新たにフォームのフィールドを設定しなくても、Metaクラスでfieldsを設定することで必要な機能を実装できます！password1やpassword2も、実は書かなくても問題ありません。

## talk_room.htmlについて

```
<button onclick="location.href='{% url 'friends' %}'">＜</button>
```
の部分はbuttonではなくaタグの方が自然かもしれません。

