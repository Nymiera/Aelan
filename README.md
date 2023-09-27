---
license: apache-2.0
pipeline_tag: text-generation
---

# Model Card for Mistral-7B-Instruct-v0.1

The Mistral-7B-Instruct-v0.1 Large Language Model (LLM) is a instruct fine-tuned version of [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) generative text model with 7 billion parameters.

For full details of this model please read our [Release blog post](https://mistral.ai/news/announcing-mistral-7b-v0.1/)

## Instruction format

In order to leverage instruction fine-tuning, your prompt should be surrounded by `[INST]` and `[\INST] tokens. The very first instruction should begin with a begin of sentence id. The next instructions should not. The assistant generation will be ended by the end-of-sentence token id.

E.g.

```bash
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("[mistralai/](https://huggingface.co/mistralai/Mistral-7B-v0.1)Mistral-7B-Instruct-v0.1")
instructions = ["[INST] What is your favourite condiment? [/INST]", 
								"[INST] Do you have mayonnaise recipes? [/INST]", 
								"[INST] This is healthy, right? [/INST]"]

encodeds = [tokenizer.encode(instruction, add_special_tokens=i==0) 
						for i, instruction in enumerate(instructions)]
```

## Model Architecture
This instruction model is based on Mistral-7B-v0.1, a transformer model with the following architecture choices:
- Grouped-Query Attention
- Sliding-Window Attention
- Byte-fallback BPE tokenizer

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lélio Renard Lavaud, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed.