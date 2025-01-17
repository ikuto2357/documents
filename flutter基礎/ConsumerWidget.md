# ConsumerWidgetとは

`ConsumerWidget` は、Flutterの状態管理ライブラリである **Riverpod** において、UIを構築するための基本的なウィジェットです。  
Riverpodで管理されているプロバイダから状態を取得し、それに応じてUIを更新する役割を持ちます。

`ConsumerWidget` は **StatelessWidget** を拡張したウィジェットであり、リビルドされる際にプロバイダから必要なデータを再取得します。

---

## 特徴
- **簡潔な設計**: プロバイダの状態を明示的に読み取ることができる。
- **高効率**: 必要な部分だけをリビルドする。
- **依存関係の明示**: 使用するプロバイダを簡単に特定できる。

---

## 使用方法

以下に、`ConsumerWidget` を使った基本的な例を示します。

### プロバイダの定義
```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';

final counterProvider = StateProvider<int>((ref) => 0);
