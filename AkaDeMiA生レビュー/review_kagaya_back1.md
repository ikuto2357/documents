お疲れ様です。
とてもよくできていると思います！
この調子で頑張ってください！

教材には載っていなかったような気がするのですが、名前空間を設定できてたりverbose_nameを設定できていたりすごいです。その他至る所で工夫を感じられます。

## media_localのファイルについて

とても細かいことで、アプリとは関係ないのですが、media_local内のファイルは.gitignoreでgitの管理対象から外して良いと思います。

## ユーザーモデルの名前について

ユーザーモデルの名前はUserが良いと思います。
SignUpは会員登録という意味なので、その名前がUserの情報(アカウント情報)を表していることが伝わりにくくなってしまいます。

## ユーザーネームのunique性について
ユーザーネームにuniqueを設定していて、とてもいいバリデーションだと思います。ただ、実際に同じユーザーネームを登録しようとすると、

TypeError at /signup
'in <string>' requires string as left operand, not NoneType

というエラーが発生してしまいました。

これは、

```
if (username in password1 or password1 in username) and username >= 4:
            raise ValidationError("ユーザーネームとパスワードが酷似しています。")
```

と書いてくれたフォームのバリデーションが原因です。

```
username = cleaned_data.get("username")
```

と変数を定義していますが、ユーザーが既にあるusernameを登録しようとすると設定してくれたバリデーションに引っかかってしまい、フォームに入力されたusernameがcleaned_dataに含まれずにNoneになってしまいます。そのためNoneTypeエラーが発生してしまいます。

```
if username and password1 and len(username) >= 4:
```
のように、もしusernameやpassword1が存在するのであればという保険をかけて上げるとエラーが発生しなくなります。

```
if ○○ :
```
のような書き方はよく使われている印象があるので、覚えておくと便利かもしれません。

## ユーザーモデルのfieldについて

ユーザーモデルはAbstractUserを継承していて、passwordというfiledを持っています。password1やpassword2はフォームの一時的な確認用フィールドであって、backendのモデルのfieldとしてデータベースには、セキュリティの観点から保存しない方が良いです。
passwordはハッシュ化されて保存されており、平文で別のフィールドにも保存されてしまうと、データベースが漏洩したときに危険という理由です。

## ユーザーモデルのlatest_messageについて

おそらく初期にモデルのフィールドに含めようと考えてくれていたと思うのですが、実際はアプリを使う上で要らなくなったものは、削除した方がわかりやすくて良いです。latest_messageに格納されているMessageオブジェクトがアプリ内では使用されていません。

## verbose_nameの設定について

verbose_nameを設定してくれいるのは、とても可読性がありいいと思います！
とても個人的な感覚だし、大したことではないのですが、verbose_nameは人間の可読性のために記述されるフィールドオプションなので、usernameに"ユーザーネーム"、emailに"メールアドレス"と日本語で書いたのであれば、passwordに関するverbose_nameも日本語でいいんじゃないかと思いました。

また、こっちは知っておいて損がない豆知識なのですが、verbose_nameは第一引数に持ってくることで省略して書くことができます！
例えば、
```
first_name = models.CharField("person's first name", max_length=30)
```
のように、verbose=と書かなくても記述量を減らして書くことができます。
この省略は主流なもので、自分自身も楽だし、他人のコードを読むときにもえ？ってならなくて済むので覚えておくとおすすめです。
多言語対応しているアプリの場合は、初めに_が書かれていることもあります。これは、
```
from django.utils.translation import gettext_lazy as _
```
に由来するもので気になったら調べてみてください！

## Messageモデルのrelated_nameについて

related_nameは、わかりやすいように元のfield名とは別の名前にした方良いです。e.g.) senderというfieldのrelated_nameをsenderにはしない。

## Messageモデルのuser1とuser2について

トークルームが重複しないように工夫してくれていますが、実際はそういった心配をしなくても重複しないので安心してください。
送信者や受信者といったフィールド以外に、user1やuser2といったフィールドを追加しなくても大丈夫です。


## ユーザーのフォーム(front)でのバリデーションについて

カスタムで設定していること自体がすごいgoodです。
いくつか改善点を上げるので参考にしてみてください。

まず、これはフォームのバリデーションに限らないことですが、emailという変数は使われていないので削除した方が良いです。
vscodeでは、宣言したものの使われていない変数は薄い色にしてくれるので、薄い色があったら削除するか、何に使おうとしていたかを考えると良いと思います。

また、UserCreationFormを継承してフォームを作成しているため、基本的なバリデーションは既に実装されています。パスワードと確認用パスワードの一致等は自分で書かなくてもOKです。
settings.pyのauth_password_validatorが消されていたので、おそらく意図的に消して自分でtryしてくれたのだと思うのですが、空にする必要はなく、末尾にカスタムのバリデーションを追加する方がセキュリティが低下するリスクが減って安全なのでおすすめです。

## LOGIN_REDIRECT_URLとLOGOUT_REDIRECT_URLについて

settings.pyに記述してくれていますが、実際のログインとログアウトのビューでは遷移先を直接記述しているので特に効力を発揮していません。LoginViewなどのクラスベースビュー(CBV)を継承した場合は、LOGIN_REDIRET_URLが参照されます。関数ベースビュー(FBV)を使う場合でも、直接遷移先を記述するよりも、LOGIN_REDIRECT_URLを参照させるようにビューがセキュリティの観点等であったり、コードの可読性であったりいくつかの理由から推奨されます。

例えば、このような形になります。
```
return redirect(settings.LOGIN_REDIRECT_URL)
```

似たような記述方法は実は他のファイルにもあって、例えばurls.pyには
```
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
のような記述をしています。このような記述の仕方をハードコーディングを避けるという風に言って、djangoに限らず推奨されるのでぜひ覚えてください！

## ログアウトの処理について

ログアウトの処理はGETよりもPOSTの方がセキュリティ上の観点から推奨されています。
余力があればPOSTでログアウトをする処理を考えてみてください！
また、all-authなどのライブラリはPOSTでログアウト機能を実装してk流えていて、そうしたライブラリを使えば簡単にログアウトの処理を安全に書くことができます。

## プロフィール設定変更のビューについて

GETの場合、POSTの場合、それ以外の場合と丁寧に書いてくれてとてもいいと思います。実は、実際は、POSTかそれ以外かという形でもっと簡潔に条件分岐を表すことができます。(処理が特殊なのはPOSTの場合のみなので)また、実際にアプリを使う上でGETとPOST以外の処理に今回出会していないので影響が出ていないのですが、else節に該当する
```
return render(request, "myapp/username_update.html", {'fomr':form})
```
の部分で、fomrはタイポ(タイプミス)があったので軽く直してください。messagesを取り入れているのはいいですね！

## トークルームのメッセージの表示について

新しいメッセージが上に来る仕様になっていて、実用上の利便性を考えれば逆が良いのかなと思います。


