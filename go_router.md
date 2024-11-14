# go_routerを使ってみよう

go_routerパッケージは画面遷移を簡単に管理するためのパッケージです。
[(公式ドキュメント)](https://pub.dev/packages/go_router)
flutter favoriteにも選ばれており、主に自分のアウトプット用だが、業務ではよく使うみたいで、今後学習する人の役に立つかもしれないのでまとめてみます。

# いいところ(公式ドキュメントから抜粋)：
- パスパラメータやクエリパラメータを取り出すことができます。<br>
  パスパラメータというのは<br>
  /user/id<br>
  のidの部分<br>
  クエリパラメータというのは<br>
  ?source=abc<br>
  のsource=abcの部分

  ただし、受け渡すデータが複雑なときは向いてません。(現に、私は使いませんでした。)

- 階層的な画面構成(Sub Route)ができる(ルーティングのネスト)<br>
  ex.)todo一覧ページからtodo追加ページとtodo詳細ページの二つがネストされている等

- リダイレクト機能 <br>
  ログインしていない時にサインイン画面に移すなど

# 使い方 (router.dartの書き方)

ある程度テンプレートのように使えそうです。
公式ドキュメントのexampleではmain.dart内に記述していましたが、router.dartというファイルを作りそれに分離することもできます。
アプリケーションの規模が大きい場合、分けていた方が管理がしやすく、テストも容易です。
router.dartではルーティングを行います。

0. コード例<br>
最初にコード例を示します。
あとの節で詳細を見ていきます。

```dart
final GoRouter router = GoRouter(
  // ルート設定のリスト
  routes: <RouteBase>[
    // 親ルート（GoRoute）
    GoRoute(
      path: '/',  // ルートのパス
      builder: (BuildContext context, GoRouterState state) {
        return const HomePage();  // パスに対応するページ
      },
      routes: <RouteBase>[
        // サブルート（GoRoute）
        GoRoute(
          path: '/detail',
          builder: (BuildContext context, GoRouterState state) {
            return const DetailPage();  // サブルートに対応するページ
          },
        ),
        GoRoute(
          path: '/settings',
          builder: (BuildContext context, GoRouterState state) {
            return const SettingsPage();  // サブルートに対応するページ
          },
        ),
      ],
    ),
  ],
);

```


1. テンプレート
  ```dart
  final GoRouter router = GoRouter(
    routes:<RouteBase>[
    ],
   );
  ```
  ここの部分がgo_routerのテンプレートともいうべき部分で、おそらく共通で使えます。
  RouteBase[]の[]の中にルーティングを記述していきます。

2. GoRoute関数<br>
各ルートは、GoRoute関数の内部に書いていきます。
GoRoute関数内では、次のようなプロパティがあります。<br>
    a. path: ここにurlを書きます。<br>
     　　ex.)path: '/',path: '/detail',<br>
    　　'/'に指定したページが、最初に開かれるページです。<br>
    b. builder: これはルートにアクセスした際に表示するウィジェットを作成する関数です。引数には、context, stateを取ります。公式ドキュメントには、<br>`BuilContext context,GoRouterState state`<br>と型表示して書かれていますが、省略可能です。一応別の名前(_など)いを用いることもできるみたいですが、わかりにくいと思います。
    return　の部分に、表示するページのウィジェットを書きます。
    ```dart
    return const HomePage();
    ```
    のようにするといいです。
    処理が単純な場合はアロー関数を用いて記述するとより簡潔です。例えば、こんなふうに書けます。
    ```dart
    builder: (context,state) =>const SettingsPage();
    ```

    c. routes:さらにルーティングをネストさせることができます。
    ```dart
    routes:<RouteBase>[]
    ```
    とし、内部にGoRoute関数を重ねることでネストできます。
    <br>
    0節の例を見てもらえればと思います。

  3. 値の引き渡し<br>
    値の引き渡しは`state.extra as データ型`でできます。
    コード例はこんな感じです。
        ```dart
        builder: (context, state) {
            final message = state.extra as String; 
            // extraからメッセージを受け取る
            return DetailsPage(message: message);
      },
        ```

# 使い方(main.dartの書き方)
router.dartにルーティングを書いたら、main.dartでそれを読み込みます。
テンプレートのように書けばよく、例えば、以下のように書けます。
```dart
import 'package:flutter/material.dart';
import 'router.dart';  // router.dart をインポート

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      routerConfig: router,  // router.dart で定義した GoRouter を設定
    );
  }
}
```

# 使い方 (各ページでの遷移)
実際のページ遷移の記述の仕方はこのようにします。
主に、context.goとcontext.pushの二つがあります。<br>
context.goは遷移の履歴を残さず、次のページに飛ぶ方法で、ログイン画面などに適しています。<br>
context.pushは遷移履歴をスタックする方法で、context.pop()で前のページに戻ることができます。<br>
例えば、ボタンを押した時にページに遷移したかったら、このように書けます。<br>
```dart
ElevatedButton(
    onPressed: () {
        context.go('/settings');
    },
    child: Text('Go to Settings Page'),
    ),
```

state.extraでデータを渡しているときは、

```dart
ElevatedButton(
    onPressed: () {
        context.push('/settings', extra: 'Hello from Home Page!');
          },
    child: Text('Go to Settings with Extra'),
);
```

のようにかけて、context.pop()は、
```dart
ElevatedButton(
    onPressed: () => context.pop(),
    child: Text('Back to Page A'),
    ),
```
のように書けます。

# まとめ

他にも機能はありますが、routers.dartの書き方を覚え、context.push(),go(),pop()が使えるようになればひとまず第一関門クリアな気がします。読んでくださりありがとうございました。