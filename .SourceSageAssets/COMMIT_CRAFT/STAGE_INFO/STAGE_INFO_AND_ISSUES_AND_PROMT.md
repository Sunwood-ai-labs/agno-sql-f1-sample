下記はissuesの情報です


```json

[
  {
    "number": 44,
    "title": "レポジトリにtagが無いとエラーで止まる",
    "body": "# エラー内容\n\n```\n  ____  _                                 _                 ____                                  _\n / ___|| |__    __ _  _ __    __ _   ___ | |  ___    __ _  / ___|  ___  _ __    ___  _ __   __ _ | |_   ___   _ __\n| |    | '_ \\  / _` || '_ \\  / _` | / _ \\| | / _ \\  / _` || |  _  / _ \\| '_ \\  / _ \\| '__| / _` || __| / _ \\ | '__|\n| |___ | | | || (_| || | | || (_| ||  __/| || (_) || (_| || |_| ||  __/| | | ||  __/| |   | (_| || |_ | (_) || |\n \\____||_| |_| \\__,_||_| |_| \\__, | \\___||_| \\___/  \\__, | \\____| \\___||_| |_| \\___||_|    \\__,_| \\__| \\___/ |_|\n                             |___/                  |___/\n\n2025-02-03 12:07:52.147 | INFO       | sourcesage.modules.ChangelogGenerator        :29    | リポジトリパス: ./\n2025-02-03 12:07:52.147 | INFO       | sourcesage.modules.ChangelogGenerator        :30    | 出力ディレクトリ: ./.SourceSageAssets/Changelog\n2025-02-03 12:07:52.147 | INFO       | sourcesage.modules.ChangelogGenerator        :31    | 開始タグ: None\n2025-02-03 12:07:52.147 | INFO       | sourcesage.modules.ChangelogGenerator        :32    | 終了タグ: None\n2025-02-03 12:07:52.147 | SUBPROCESS | sourcesage.modules.GitCommander              :14    | >>>>>> 実行コマンド: git branch\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :116   | ブランチ一覧:\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :118   | - feature/buildings\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :118   | - feature/export\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :118   | - feature/graphql\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :118   | - feature/import-map\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :118   | - feature/pagy\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :118   | - feature/rails8\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :118   | - feature/ruby31\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :118   | - feature/yarn-upgrade\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :118   | - feature/yarn2\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :118   | -  master\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :123   | 変更履歴の生成を開始します...\n2025-02-03 12:07:52.173 | INFO       | sourcesage.modules.ChangelogGenerator        :128   | ブランチ 'master' の変更履歴を生成しています...\n2025-02-03 12:07:52.173 | SUBPROCESS | sourcesage.modules.GitCommander              :14    | >>>>>> 実行コマンド: git tag --sort=-creatordate\n2025-02-03 12:07:52.188 | WARNING    | sourcesage.modules.ChangelogGenerator        :51    | タグが2つ未満のため、最新のタグと1つ前のタグを取得できません。\nTraceback (most recent call last):\n  File \"/opt/homebrew/bin/sourcesage\", line 8, in <module>\n    sys.exit(main())\n             ^^^^^^\n  File \"/opt/homebrew/lib/python3.11/site-packages/sourcesage/cli.py\", line 186, in main\n    run(args)\n  File \"/opt/homebrew/lib/python3.11/site-packages/sourcesage/cli.py\", line 125, in run\n    sourcesage.run()\n  File \"/opt/homebrew/lib/python3.11/site-packages/sourcesage/core.py\", line 46, in run\n    changelog_generator.generate_changelog_for_all_branches()\n  File \"/opt/homebrew/lib/python3.11/site-packages/sourcesage/modules/ChangelogGenerator.py\", line 133, in generate_changelog_for_all_branches\n    with open(output_file, 'w', encoding='utf-8') as f:\n         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nFileNotFoundError: [Errno 2] No such file or directory: './.SourceSageAssets/Changelog/CHANGELOG_features.md'\n```\n\n# 環境\n\n```\n❯ pip list|grep source\nsourcesage                   6.1.1\n```\n\n\n```\n❯ python --version\nPython 3.12.7\n```\n"
  },
  {
    "number": 43,
    "title": "ヘッダー画像",
    "body": "![Image](https://github.com/user-attachments/assets/0ea1d6ce-c6f1-4e5a-95cf-098fc64e8f49)"
  },
  {
    "number": 42,
    "title": "【機能追加】IssueOpt - IssueWizeによる自動改善案提案機能",
    "body": "\r\n### 1. 概要\r\n本Issueでは、IssueWizeで生成されたissueに対して、自動的に改善案を提案する機能「IssueOpt」を実装する。IssueOptは、生成されたissueの内容と関連リポジトリの情報をLLMに入力することで、より詳細な解決策やアイデアを提案する。また、SourceSageのモードの1つとして「IssueOpt」を追加する。\r\n### 2. IssueOptの機能詳細\r\n#### 2.1. CLIコマンドによるIssueOpt実行\r\n- SourceSageのCLIコマンドに「IssueOpt」モードを追加する。\r\n    - コマンド例： `sourcesage --mode IssueOpt`\r\n- CLIコマンド実行時に、IssueOptに必要なパラメータを指定できるようにする。\r\n    - パラメータ例：\r\n        - `repo_overview_file`: リポジトリ情報ファイルのパス\r\n        - `model`: 利用するLLMのモデル名 (例: `gpt-3.5-turbo`)\r\n        - `issue_number`: 改善案を提案するissue番号\r\n#### 2.2. LLMを用いた自動改善案提案\r\n- IssueWizeで生成されたissueのタイトルと本文、および`repo_overview_file`で指定されたリポジトリ情報をLLMに入力する。\r\n- LLMは入力情報に基づき、以下の内容を含む改善案を提案する。\r\n    - より具体的な解決策\r\n    - 関連するコード例\r\n    - 考慮すべき追加事項\r\n    - 既存issueやプルリクエストとの関連付け\r\n- 提案された改善案は、指定されたissueのコメントとして追記される。\r\n### 3. ペルソナとユースケース\r\n#### 3.1. ペルソナ: ソフトウェア開発者\r\n- 日常的にIssueWizeを利用してissueを作成している。\r\n- より質の高いissueを作成し、開発効率を向上させたいと考えている。\r\n#### 3.2. ユースケース\r\n1. 開発者はIssueWizeを使用してissueを生成する。\r\n2. 開発者はSourceSage CLIコマンドを用いて、IssueOptモードを実行し、改善案を必要とするissue番号を指定する。\r\n3. IssueOptが指定されたissueとリポジトリ情報に基づいて、自動的に改善案を提案する。\r\n4. 開発者は提案された改善案を参考に、issueの内容を充実させる。\r\n### 4. 期待される効果\r\n- IssueOptの自動改善案提案機能により、開発者はより質の高いissueを作成することができる。\r\n- 提案された改善案を参考にissueを充実させることで、開発の効率化、問題解決の迅速化などが期待できる。\r\n### 5. 留意事項\r\n- LLMの出力はあくまで提案であり、完璧な解決策を保証するものではない。\r\n- 提案内容の正確性や妥当性は、開発者が最終的に判断する必要がある。\r\n### 6. 今後の展望\r\n- IssueOptの提案精度向上のため、LLMのモデルやパラメータの調整を行う。\r\n- ユーザーからのフィードバックを収集し、機能改善に役立てる。\r\n- IssueWize以外のツールとの連携も視野に入れ、IssueOptの適用範囲を拡大する。"
  },
  {
    "number": 32,
    "title": "リリースノートの生成中にエラーが発生しました: 429 Resource has been exhausted (e.g. check quota).",
    "body": "`.SourceSageAssets\\DOCUMIND\\_PROMPT_v5.1.0.md`の出力内容を絞る！"
  },
  {
    "number": 29,
    "title": "成功する時もあるがたまに起きてしまうエラー",
    "body": "こんにちは最近 SourceSage を知って使わさせてもらっています。\r\nGitの差分までプロンプトとして出力できる機能や、プロンプトとして考慮されているデータの示し方が素晴らしいと思っております👍\r\n\r\n以下のエラーが発生しましたので報告になります。\r\n```\r\nTraceback (most recent call last):\r\n  File \"/home/myusername/.pyenv/versions/3.12.3/bin/sourcesage\", line 8, in <module>\r\n    sys.exit(main())\r\n             ^^^^^^\r\n  File \"/home/myusername/.pyenv/versions/3.12.3/lib/python3.12/site-packages/sourcesage/cli.py\", line 96, in main\r\n    sourcesage.run()\r\n  File \"/home/myusername/.pyenv/versions/3.12.3/lib/python3.12/site-packages/sourcesage/core.py\", line 46, in run\r\n    changelog_generator.integrate_changelogs()\r\n  File \"/home/myusername/.pyenv/versions/3.12.3/lib/python3.12/site-packages/sourcesage/modules/ChangelogGenerator.py\", line 123, in integrate_changelogs\r\n    with open(file_path, 'r', encoding='utf-8') as f:\r\n         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r\n```\r\n- 他リポジトリでは、全て正しく出力できることもあるため、すべてのケースで失敗するわけではありません。\r\n- 一度失敗すると再度実行しても失敗します\r\n\r\n\r\nすみませんが再現方法がこちらでもわかっていないので、もしわかったら追記します 🙇 \r\n"
  }
]

```

また、下記はgitはStageの情報です

issueを解決していればそれも含めてコミットメッセージを書いて
解決していないissueは掲載しないで

見やすくコミットメッセージにして
章やパラグラフ、箇条書きを多用して見やすくして

コミットメッセージは日本語にして
正確にstep-by-stepで処理して

コミットメッセージは下記のフォーマットにして

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

種類は下記を参考にして

例：
  - feat: 新機能
  - fix: バグ修正
  - docs: ドキュメントのみの変更
  - style: コードの動作に影響しない変更（空白、フォーマット、セミコロンの欠落など） 
  - refactor: バグの修正も機能の追加も行わないコードの変更
  - perf: パフォーマンスを向上させるコードの変更
  - test: 欠けているテストの追加や既存のテストの修正
  - chore: ビルドプロセスやドキュメント生成などの補助ツールやライブラリの変更


## Stageの情報

```markdown


```