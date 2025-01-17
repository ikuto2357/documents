## 1. 必要なパッケージをインストール
Riverpodを利用するには、まず`flutter_riverpod`パッケージをインストールします。

```bash
flutter pub add flutter_riverpod
```

---

## 2. プロバイダーを定義する
`Provider`は読み取り専用の値を提供します。以下は、`Provider`を使って「現在の日付」を提供する例です。

```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';

// プロバイダーを定義
final dateProvider = Provider<DateTime>((ref) {
  return DateTime.now();
});
```

---

## 3. プロバイダーの値をUIで使用する
`ConsumerWidget`または`Consumer`を使って、プロバイダーの値を読み取ります。

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

// プロバイダーを定義
final dateProvider = Provider<DateTime>((ref) {
  return DateTime.now();
});

void main() {
  runApp(
    // Riverpodのプロバイダーを使うために、アプリ全体をProviderScopeで包む
    ProviderScope(
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: HomePage(),
    );
  }
}

class HomePage extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // プロバイダーの値を取得
    final currentDate = ref.watch(dateProvider);

    return Scaffold(
      appBar: AppBar(title: Text('Riverpod Provider Example')),
      body: Center(
        child: Text(
          'Current Date: $currentDate',
          style: TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}
```

---

## 4. 実行結果
アプリを実行すると、以下のように現在の日付と時刻が表示されます。

```
Current Date: 2025-01-18 15:30:00.000
```

---

## 5. ポイント
- **読み取り専用:** `Provider`はステートレスで、計算された値や固定値を提供します。
- **更新不要:** 値は固定されているか、必要に応じて再計算されます。

---

これで、Riverpodの`Provider`の基本的な使い方がわかります！このコードを拡張して、より複雑なアプリケーションにも適用できます。
```