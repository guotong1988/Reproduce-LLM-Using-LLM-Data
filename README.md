# Build-LLM-Using-LLM-Data
Build LLM/MLLM From Scratch Using Only LLM/MLLM Data Distillation

## Chat Test
start vLLM server
```
python3 -m vllm.entrypoints.openai.api_server \
  --model /the_model_path/ \
  --host 0.0.0.0 \
  --port 8000
```
do request
```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "/the_model_path/",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "你好"}
    ],
    "temperature": 0.7,
    "max_tokens": 4096
  }'
```

## Eval Results
| **Base Model**   | **Train Dataset** | **ceval** | **mmlu** | 
| ----------- | ----------- | ----------- | ----------- |
| Qwen3-32B-Base  | [Chinese](https://modelscope.cn/datasets/guotong1988/distill-deepseekV3.2-48w-dataset), Non-thinking, 3 Epoch | 0.7077 | 0.8105 |
| Qwen3-32B-Base  | [Chinese + English](https://modelscope.cn/datasets/guotong1988/distill-deepseekV3.2-48w-dataset), Non-thinking, 3 Epoch | 0.7154 | |
