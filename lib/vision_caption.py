from typing import Optional, Type

# from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from pydantic import BaseModel, Extra, root_validator

class VisionPositionScheme(BaseModel):
    position: str = Field(description="should be the camera position")

class VisionCaptionTool(BaseTool):
    name = "vision_caption_tool"
    description = "useful when you want to check what you see in front of you, " \
                  "it ONLY show the vision in front of you, you can not see the left/right/back position."
    args_schema: Type[VisionPositionScheme] = VisionPositionScheme

    def _run(self, position:str) -> str:
    # def _run(self, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the tool."""
        return "A man sitting in front of the computer and doing some work"

    async def _arun(self) -> str:
        # async def _arun(self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("vision_caption_tool does not support async")