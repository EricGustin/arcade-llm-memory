from arcade.sdk import ToolCatalog
from arcade.sdk.eval import (
    EvalRubric,
    EvalSuite,
    ExpectedToolCall,
    SimilarityCritic,
    tool_eval,
)

import arcade_memory
from arcade_memory.tools.store import search_summarized_information, store_summarized_information

# Evaluation rubric
rubric = EvalRubric(
    fail_threshold=0.85,
    warn_threshold=0.95,
)


catalog = ToolCatalog()
catalog.add_module(arcade_memory)


@tool_eval()
def memory_eval_suite() -> EvalSuite:
    suite = EvalSuite(
        name="memory Tools Evaluation",
        system_message=(
            "You are an AI assistant with access to memory tools. "
            "Use them to help the user with their tasks."
        ),
        catalog=catalog,
        rubric=rubric,
    )

    suite.add_case(
        name="Search summarized information",
        user_message="Search for information about the user's friend.",
        expected_tool_calls=[
            ExpectedToolCall(func=search_summarized_information, args={"query_text": "John Doe"}),
        ],
        rubric=rubric,
        critics=[
            SimilarityCritic(critic_field="query_text", weight=0.5),
        ],
    )

    return suite
