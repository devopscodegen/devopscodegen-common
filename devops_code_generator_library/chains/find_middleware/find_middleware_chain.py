"""
This module contains the create_find_middleware_chain function which
returns the find_middleware_chain corresponding to the language and dependency management tool
"""

from importlib.resources import files
from langchain_core.prompts import ChatPromptTemplate
from devops_code_generator_library.devops_code_generator_output_parser import (
    DevopsCodeGeneratorOutputParser,
)


def create_find_middleware_chain(llm, language, dependency_management_tool):
    """
    This function returns the find_middleware_chain
    corresponding to the language and dependency management tool
    """

    templates_package = "devops_code_generator_library.templates.find_middleware"

    middlewares = (
        files(templates_package)
        .joinpath(language, dependency_management_tool, "middlewares.txt")
        .read_text(encoding="utf-8")
    )

    return (
        ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You will be provided with below information
- contents of dependency manifest {dependency_manifest} enclosed within ```{dependency_manifest}_begin and ```{dependency_manifest}_end delimiters.
- {language} middlewares enclosed within ```middlewares_begin and ```middlewares_end delimiters.
Your task is to select the correct middleware using only the provided information.
Middleware should be enclosed within ```middleware_begin and ```middleware_end delimiters.
If more than one {language} middleware are possible, then select the most specific instead of the most generic.
Before selecting the middleware, explain your reasoning.
Your reasoning should be enclosed within ```reasoning_begin and ```reasoning_end delimiters.
""",
                ),
                (
                    "human",
                    """```{dependency_manifest}_begin
{dependency_manifest_content}
```{dependency_manifest}_end

```{language}_middlewares_begin
{middlewares}
```{language}_middlewares_end
""",
                ),
            ]
        ).partial(middlewares=middlewares)
        | llm
        | DevopsCodeGeneratorOutputParser()
    ).with_config(run_name="find_middleware_chain")
