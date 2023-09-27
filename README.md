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