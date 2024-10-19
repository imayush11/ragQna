# query_engine/llm_service.py
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import ServiceContext
from llama_index.core.prompts.prompts import SimpleInputPrompt


def create_llm_service():
    """Creates and configures the LLM service."""
    
    system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version)
    - StableLM is a helpful and harmless open-source AI language model developed by StabilityAI.
    - StableLM is excited to help the user but will refuse anything harmful.
    """
    
    query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")
    
    llm = HuggingFaceLLM(
        context_window=4096,
        max_new_tokens=256,
        generate_kwargs={"temperature": 0.7, "do_sample": False},
        system_prompt=system_prompt,
        query_wrapper_prompt=query_wrapper_prompt,
        tokenizer_name="StabilityAI/stablelm-tuned-alpha-3b",
        model_name="StabilityAI/stablelm-tuned-alpha-3b",
        device_map="auto",
        stopping_ids=[50278, 50279, 50277, 1, 0],
        tokenizer_kwargs={"max_length": 4096},
    )
    
    return llm


def create_service_context(llm, chunk_size=1024):
    """Creates and configures the service context for the index."""
    return ServiceContext.from_defaults(chunk_size=chunk_size, llm=llm, embed_model="local")


