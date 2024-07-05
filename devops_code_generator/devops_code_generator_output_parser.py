"""
Parse a list of model Generations into a python dictionary
"""

import re

from typing import Any, List

from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import BaseCumulativeTransformOutputParser
from langchain_core.outputs import Generation


class DevopsCodeGeneratorOutputParser(BaseCumulativeTransformOutputParser[Any]):
    """
    Parse a list of model Generations into a python dictionary
    """

    def parse_result(self, result: List[Generation], *, partial: bool = False) -> Any:
        """
        Parse a list of model Generations into a python dictionary
        """
        try:
            if len(result) != 1:
                raise NotImplementedError(
                    "This output parser can only be used with a single generation."
                )
            text = result[0].text
            text = text.strip()
            pattern = r"```(\w+)_begin\s*(.*?)\s*```(\w+)_end"
            matches = re.findall(pattern, text, re.DOTALL)
            if partial and matches:
                matches = matches[-1:]
            v_dict = {}
            for match in matches:
                if match[0] == match[2]:
                    v_dict[match[0]] = match[1].strip()
            if v_dict:
                return v_dict
            if partial:
                return None
            return text
        except Exception as e:
            raise OutputParserException(error=e, llm_output=text) from e

    def parse(self, text: str) -> Any:
        """Parse the output of an LLM call to a JSON object.

        Args:
            text: The output of the LLM call.

        Returns:
            The parsed JSON object.
        """
        return self.parse_result([Generation(text=text)])

    @property
    def _type(self) -> str:
        return "devops_code_generator_output_parser"
