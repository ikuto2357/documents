### Djangoの`AbstractUser`についてプロのエンジニアが押さえておくべき知識

Djangoの`AbstractUser`は、`django.contrib.auth.models.AbstractBaseUser`を拡張した抽象クラスであり、Djangoのデフォルトユーザーモデルのフル機能を提供しつつ、カスタマイズ可能な設計となっています。

---

### **1. `AbstractUser`の基本**
- `AbstractUser`は、Djangoのデフォルトの`User`モデルのすべての機能を備えた抽象モデル。
- デフォルトの`User`モデルと同様に、以下のフィールドを提供：
  - `username`
  - `email`
  - `first_name`
  - `last_name`
  - `password`
  - `is_staff`
  - `is_active`
  - `is_superuser`
  - `last_login`
  - `date_joined`
- `AbstractBaseUser`を直接継承するより、`AbstractUser`を継承する方が一般的な用途に適している。

---

### **2. `AbstractUser`を使う理由**
- `User`モデルをそのまま使うと、追加フィールドを持たせることが難しい。
- `AbstractUser`を拡張することで、新しいフィールドを追加できる。
- Djangoの管理画面や認証関連機能との互換性を維持しやすい。

#### **カスタムユーザーモデルの定義例**
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
```
- `AUTH_USER_MODEL`を適切に設定することを忘れずに：
  ```python
  AUTH_USER_MODEL = "myapp.CustomUser"
  ```
- **重要**: `AUTH_USER_MODEL`の設定はプロジェクト開始時に行うべき。途中で変更するとデータベース移行が非常に困難。

---

### **3. `AbstractUser`を拡張する場合の注意点**
- Djangoの管理画面と連携するには、適切な`UserAdmin`の設定が必要：
  ```python
  from django.contrib import admin
  from django.contrib.auth.admin import UserAdmin
  from .models import CustomUser

  @admin.register(CustomUser)
  class CustomUserAdmin(UserAdmin):
      fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("phone_number",)}),)
  ```
- Djangoの認証フォーム（`UserCreationForm`など）をカスタムユーザーモデルに対応させる必要がある：
  ```python
  from django.contrib.auth.forms import UserCreationForm
  from .models import CustomUser

  class CustomUserCreationForm(UserCreationForm):
      class Meta:
          model = CustomUser
          fields = UserCreationForm.Meta.fields + ("phone_number",)
  ```
  
---

### **4. `AbstractUser`のカスタムマネージャ**
- Djangoの`UserManager`を利用できるが、カスタムフィールドを追加する場合はカスタムマネージャを作成する：
  ```python
  from django.contrib.auth.models import BaseUserManager

  class CustomUserManager(BaseUserManager):
      def create_user(self, username, email, password=None, **extra_fields):
          if not email:
              raise ValueError("The Email field must be set")
          email = self.normalize_email(email)
          user = self.model(username=username, email=email, **extra_fields)
          user.set_password(password)
          user.save(using=self._db)
          return user

      def create_superuser(self, username, email, password=None, **extra_fields):
          extra_fields.setdefault("is_staff", True)
          extra_fields.setdefault("is_superuser", True)
          return self.create_user(username, email, password, **extra_fields)
  ```
- `CustomUser`のモデルに適用：
  ```python
  class CustomUser(AbstractUser):
      objects = CustomUserManager()
  ```

---

### **5. `AbstractUser`を使用する際のポイント**
✅ **プロジェクト開始時に`AUTH_USER_MODEL`を設定する**  
✅ **カスタムフィールドを追加する場合は`AbstractUser`を継承する**  
✅ **管理画面で使う場合は`UserAdmin`を適切にカスタマイズする**  
✅ **カスタムマネージャを適用することで、ユーザー作成時の挙動を制御する**  
✅ **フォーム（`UserCreationForm`など）もカスタムユーザーモデルに対応させる**

---

### **まとめ**
`AbstractUser`は、Djangoのデフォルトユーザーモデルを拡張し、カスタムユーザーモデルを簡単に作成できる便利なクラスです。基本的な認証機能をそのまま使いつつ、フィールドの追加やマネージャのカスタマイズが可能なため、多くのプロジェクトで推奨されます。

プロジェクト開始時に`AbstractUser`を継承したカスタムユーザーモデルを定義し、適切に`AUTH_USER_MODEL`を設定することで、後から変更する際の手間を省くことができます。