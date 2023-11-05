想定する開発の流れ

1. Model 定義 マイグレーション作成
2. Serializer 定義
3. View 作成 各エンドポイントの関数を pass して定義 Res, Req のスキーマだけ指定
4. make generate-types でフロントエンド、モックに反映
   TODO:
5. テストの作成(フローの定義?)

[Common]

## Pre-commit

https://installati.one/install-pre-commit-ubuntu-22-04/
https://dev.classmethod.jp/articles/introduce-pre-commit/
https://qiita.com/ijufumi/items/6dfee715b40979017d1d

## Makefile

### 複数ディレクトリでの実行/並列化

https://devlights.hatenablog.com/entry/2022/05/11/073000
https://qiita.com/ymdymd/items/312c9f554d4ffb1f8dc6

[Backend]

## To run

poetry run python manage.py runserver 0.0.0.0:8000

## To generate schema

poetry run python manage.py spectacular --file schema.yaml

## Mock

https://docs.stoplight.io/docs/prism/9528b5a8272c0-dynamic-response-generation-with-faker
https://blog.tech-monex.com/entry/2022/12/23/100208

## スキーマ生成に関して

https://speakerdeck.com/shihono/djangocongress-jp-2022?slide=74

## Serializer 関連 要チェック

https://thinkami.hatenablog.com/entry/2022/12/13/215625

## Decorator

https://hiroki-sawano.hatenablog.com/entry/django-pre-request-and-post-response-decorators

[Frontend]

## Codegen

https://zenn.dev/nixieminton/articles/e3a2f48d4e8e34

## Install graphviz && dep-graph

https://self-development.info/ubuntu%E3%81%B8%E3%81%AEgraphviz%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB/

https://engineerblog.mynavi.jp/technology/monorepo/
