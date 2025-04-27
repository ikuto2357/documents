お疲れ様です。
とてもよくできていると思います！
この調子で頑張ってください！

## requirements.txtの更新について

今回の課題で、pycopgなど新たに追加したpackageがあると思うので、あらたにpackageを追加したときは、
```
pip freeze > requirements.txt
```

を実行し、更新するようにしましょう！

## メールアドレスログインについて

教材が変わってわかりにくくなってしまっていたのですが、今回の課題の内容には「メールアドレスでログイン」するも実は含まれていました。
ユーザーネームでログインするよりも、メールアドレスとパスワードでログインする場合の方がユニーク性を持たせるのに適切だからです。
(実際、多くのアプリではメールアドレスによるログインor Googleアカウントなどの他のアプリと連携した認証が主流になっています。ちなみに、他のアプリと連携した認証をOAuth認証といいます。)

AbstractUserのUSERNAME_FIELDをいじり、それに合わせてREQUIRED_FIELDを変更するなどで、割と簡単に実装できるので調べてみてください！

## ログアウトできない
ログアウトボタンでログアウトしようとすると405 Method Not Allowedが発生しています。
前回のレビューを受けてLogoutというCBVにトライしてくれたと思うのですが、ログインがPOSTでしか受け付けないようになりました。
設定ページにあるログアウトボタンはaタグで実装されており、これだとGETによるリクエストになってしまうので、formにしてmethodを
postにするなどがおすすめです。

## コーディングを楽にする裏技
セッションをうまく使いこなしてくれてGOODです！
もし、request.sessionって長くて打つのめんどくさかったら、初めに


```session = request.session```

のように宣言すると、例えば
```
session_code = request.session.get("ver_code")
```
を、
```
session_code = session.get("ver_code")
```

と書けるので、おすすめです。

## 検索フォームのnameについてのおすすめ
nameをqとしてくれて、悪くはないのですが、「検索」フォームなので、searchなどがbetterな気がします。

## emptyについてのおすすめ
friend.htmlのfor文について、emptyを設定してくれているのですが、せっかく設置したのであれば、何かしら書くのがおすすめです！
例えば、「トーク可能なともだちはいません」などなどです☺️

## /verifyへのアクセスについて

セキュリティ的にそこまで問題があるわけではないのですが、ログイン段階で、usernameとpasswordを正しく入力すると言うプロセスを経ていなくても/verify/と打てばそのページに飛べてしまうのはあまり好ましく思っていたかもしれません。  
ただ、まだログインをしていないのでLoginRequiredMixinやis_authenticatedを使えずもどかしいですよね。

そんなときにおすすめなのがdispatchメソッドをoverrideする方法です！！

このメソッドは呼ばれた時のHTTPメソッド(getやpostなど)に応じたメソッドを呼び出すためのメソッド(dispatchと言う英単語がそういう意味)なのですが、嬉しい、**Viewが呼ばれた時にまず一番最初に呼ばれる**という注目すべき特徴があります。
この性質を活かし、overrideすることで実装の自由度が広がります。

例えば、
```
def dispatch(self, request, *args, **kwargs):
        if not request.session.get("user_id") or not request.session.get("ver_code"):
            # 不正アクセスなのでログインページにリダイレクト
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)
```
のようにすると、sessionにuser_idやver_codeがないときにリダイレクトすると言う処理を加えることができます。

今回は2FA(2段階認証)についてでしたが、dispatchメソッドにifとredirectを加える実装方法は覚えたほうが得かもしれません。

このdispatchメソッドは、Viewと言うCBV(クラスベースビュー)が持っているメソッドで、全てのCBVで利用可能です。

## 命名について
メールアドレスについて、mailではなくてemailにした方が良いです。そちらの方が一般的であり、メールは和製英語であることも含め、可読性があがります。

