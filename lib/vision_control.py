from typing import Optional, Type

# from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools import BaseTool

from lib.vision_caption import VisionPositionScheme
from lib.vision_caption import VisionCaptionTool


class VisionControl(BaseTool):
    name = "camera_position_control_tool"
    description = "useful when you want to control the camera position, it can be front/left/right/forward/back."
    args_schema: Type[VisionPositionScheme] = VisionPositionScheme

    def _run(self, position: str) -> str:
    # def _run(self, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the tool."""
        vision = VisionCaptionTool()
        # vision.run(position)
        return f"The camera have turn {position} success, {vision.run(position)}"


    async def _arun(self) -> str:
        # async def _arun(self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("camera_position_control_tool does not support async")