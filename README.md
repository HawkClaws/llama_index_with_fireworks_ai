# llama_indexでfireworks.aiのLLM使用するサンプル

## 変更点

### MODELに対応する値を追加

そのまま実行すると、各ライブラリのMODEL変数に`fireworks.ai`で使用するモデル名が無いのでエラーが起きる
かなり暫定的な対処方法となるが、それらの変数に使用するMODELの情報を追加する

追加対象のライブラリ及び、変数

- `tiktoken`
    - `tiktoken.model.MODEL_TO_ENCODING`

- `llama_index`
    - `llama_index.llms.openai_utils.ALL_AVAILABLE_MODELS`

### 出力トークン数の設定

`max_tokens`をデフォルトから変更する
（変更しないとレスポンス文章がめっちゃ短くなってしまう）

```python
llm = OpenAI(api_base=API_BASE, api_key=API_KEY, model=MODEL, max_tokens=50)
```
