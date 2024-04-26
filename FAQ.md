## 独立的 python 环境

#### 创建环境
```
python3 -m venv env
```
#### 启用环境
```
source env/bin/activate
```
#### 安装依赖
```
pip install -r requirements.txt
```
#### 关闭环境
```
deactivate
```
#### vscode 环境设置

vscode 左下角选择 python interpreter

## 清除 torch 缓存
```
import torch
torch.cuda.empty_cache()
```

## huggingface 下载的模型目录
```
~/.cache/huggingface/hub
```
