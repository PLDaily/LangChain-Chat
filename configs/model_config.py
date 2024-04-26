import torch.cuda
import torch.backends


embedding_model_dict = {
    "text2vec": "/mnt/workspace/.cache/modelscope/thomas/text2vec-large-chinese",
}

# Embedding model name
EMBEDDING_MODEL = "text2vec"

# Embedding running device
EMBEDDING_DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

# supported LLM models
llm_model_dict = {
    "chatglm3-6b": "/mnt/workspace/.cache/modelscope/ZhipuAI/chatglm3-6b",
}

# LLM model name
LLM_MODEL = "chatglm3-6b"

# LLM running device
LLM_DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
