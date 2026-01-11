from enum import Enum
class TaskState(Enum):
    COLLECT_PROFILE = "collect_profile"
    COLLECT_DOCUMENTS = "collect_documents"
    VALIDATE = "validate"
    REVIEW = "review"
    COMPLETE = "complete"