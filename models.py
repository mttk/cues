"""Model registry — kept free of torch/transformers so analysis/backfill
scripts can look up `thinking` (needed by parsing.classify_parse) without
pulling in a model-loading stack. hint_eval.py imports MODELS/
THINKING_MODELS from here for both this metadata and actual model loading
(its own load_model/generate, which do need torch).

`enable_thinking` is only meaningful for Qwen3 hybrid checkpoints (passed
to apply_chat_template); OLMo-Think and R1-distill think natively. `thinking`
drives classify_parse's behavior (fallback disabled, think_unclosed
tracked) — see parsing.classify_parse's docstring for why the fallback
manufactures uptake for these models specifically.
"""

MODELS = {
    "olmo3-7b-instruct":  dict(hf_id="allenai/Olmo-3-7B-Instruct", thinking=False),
    "olmo3-7b-think":     dict(hf_id="allenai/Olmo-3-7B-Think", thinking=True),
    "qwen3-8b-think":     dict(hf_id="Qwen/Qwen3-8B", enable_thinking=True, thinking=True),
    "qwen3-8b-nothink":   dict(hf_id="Qwen/Qwen3-8B", enable_thinking=False, thinking=False),
    "r1-distill-qwen-7b": dict(hf_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B", thinking=True),
}

# Models that think (natively, or via enable_thinking) — long CoTs on
# gsm_mc/agieval risk running past --max-new-tokens before emitting the
# final "Answer: X", collapsing the parse rate. Derived from MODELS so the
# two can't drift apart.
THINKING_MODELS = {name for name, cfg in MODELS.items() if cfg.get("thinking")}
