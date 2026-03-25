from typing import Optional, Any
from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class TreeNode:
    value: Any
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None
