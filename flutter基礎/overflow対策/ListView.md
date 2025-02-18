`ListView` は Flutter でスクロール可能なリストを作成するためのウィジェットです。基本的な使い方を紹介します。

---

## **1. 基本的な `ListView`**
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('ListView 基本')),
        body: ListView(
          children: const [
            ListTile(title: Text('アイテム 1')),
            ListTile(title: Text('アイテム 2')),
            ListTile(title: Text('アイテム 3')),
            ListTile(title: Text('アイテム 4')),
          ],
        ),
      ),
    );
  }
}
```
**ポイント**
- `ListView` に `children` を渡してリストを作成する
- `ListTile` を使うとリストアイテムを簡単に作れる

---

## **2. 動的リスト (`ListView.builder`)**
アイテム数が多い場合は `ListView.builder` を使うことでパフォーマンスを向上できます。

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('ListView.builder')),
        body: ListView.builder(
          itemCount: 100, // 100個のアイテムを生成
          itemBuilder: (context, index) {
            return ListTile(
              title: Text('アイテム ${index + 1}'),
            );
          },
        ),
      ),
    );
  }
}
```
**ポイント**
- `itemCount` でリストの長さを指定
- `itemBuilder` で `index` を利用して動的にリストを生成

---

## **3. `ListView.separated` で区切り線を入れる**
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('ListView.separated')),
        body: ListView.separated(
          itemCount: 20,
          itemBuilder: (context, index) {
            return ListTile(
              title: Text('アイテム ${index + 1}'),
            );
          },
          separatorBuilder: (context, index) {
            return const Divider(); // 各アイテムの間に区切り線
          },
        ),
      ),
    );
  }
}
```
**ポイント**
- `separatorBuilder` を使って区切り線を挿入できる

---

## **4. `ListView` を `Column` 内で使用する（スクロールの問題を回避）**
`Column` 内で `ListView` を使う場合は `Expanded` で囲むか `ShrinkWrap` を `true` にする。

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('ListView in Column')),
        body: Column(
          children: [
            const Text('上部のウィジェット'),
            Expanded( // これがないとエラーになる
              child: ListView.builder(
                itemCount: 10,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text('アイテム ${index + 1}'),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```
**ポイント**
- `Column` の中で `ListView` を使うときは `Expanded` で囲む
- `shrinkWrap: true` を指定すると `ListView` が必要最小限の高さで表示されるが、スクロール性能が低下する可能性がある

---

## **まとめ**
- `ListView(children: [])` → 簡単なリスト
- `ListView.builder` → アイテム数が多い場合の動的リスト
- `ListView.separated` → 区切り線を入れたリスト
- `Expanded` を使うと `Column` 内でも `ListView` を快適に使用可能

どの `ListView` を使うかは、用途に応じて選択すると良いです！🚀